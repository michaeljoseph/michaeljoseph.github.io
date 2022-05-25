from collections import namedtuple
from datetime import timedelta
from functools import partial
import json
import yaml
from pathlib import Path

from requests_cache import CachedSession

from resume.badges import devicons_badges
from resume.salutations import typed_salutations

class HttpClient(CachedSession):
    def __init__(self, expire_after=None):
        CachedSession.__init__(self,
            cache_name='mycull.dev',
            use_temp=True,
            expire_after=timedelta(minutes=30) if expire_after is None else expire_after,
        )

NLJ = partial('\n'.join)
JSDELIVR_DEVICONS = "https://cdn.jsdelivr.net/gh/devicons/devicon@master/icons"
DEVICONS_GITHUB = "https://github.com/devicons/devicon/raw/master/devicon.json"
IMG_ALT = '![{i.text}]({i.image_url}){{ height={i.height} width={i.width} }}'
Image = namedtuple('Image', 'text image_url height width')
DevIcon = namedtuple('DevIcon', 'name tags svg_url color')

DEVICONS_JSON = {
    icon['name']: DevIcon(
        icon['name'],
        icon['tags'],
        f"{JSDELIVR_DEVICONS}/{icon['name']}/{icon['name']}-{icon['versions']['svg'][0]}.svg",
        icon['color'],
    )
    for icon in HttpClient().get(DEVICONS_GITHUB).json()
}

def load_resume(format='yaml', name='resume'):
    return {
        'yaml': yaml.safe_load,
        'json': json.load,
    }[format]((Path.cwd() / f'{name}.{format}').read_text())

def devicons_badges(company=None):
    skills_by_company = {
        job['id']: job['skills'].split()
        for job in load_resume()['work']
    }

    if company is None or company not in skills_by_company:
        unique_skills = set()
        for all_skills in skills_by_company.values():
            unique_skills |= set(all_skills)
        skills = list(unique_skills)
    else:
        skills = skills_by_company[company]

    return [
        IMG_ALT.format(i=Image(
            text=skill,
            image_url=DEVICONS_JSON[skill].svg_url,
            height='30px',
            width='80px',
        ))
        for skill in skills
        if skill in DEVICONS_JSON
    ]

    badges = []
    for skill in skills:
        options = dict(
            left_text=skill,
            left_title=skill,
            right_text='TODO: calc XP',
            right_color='white',
        )

        icon = icons.get(skill)
        if icon:
            options['logo'] = icon.svg
            options['left_color'] = icon.color

        badges.append(badge(**options))

    return badges

def skills_badges(company=None):
    return NLJ(devicons_badges(company))

def define_env(env):
    env.variables['skills_badges'] = skills_badges
    env.variables['typed_salutations'] = typed_salutations
