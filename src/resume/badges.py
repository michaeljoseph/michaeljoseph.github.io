from datetime import timedelta
from collections import namedtuple

from pybadges import badge
from requests_cache import CachedSession

from . import load_resume


IMG_ALT = '![{i.text}]({i.image_url}){{ height={i.height} width={i.width} }}'
Image = namedtuple('Image', 'text image_url height width')

IMG_ALT_LINK = '[![{i.text}]({i.image_url}){{ {i.align} }}]({i.link})'
ImageLink = namedtuple('ImageLink', 'link text image_url align')
def stack_over_flair():
    return IMG_ALT_LINK.format(i=ImageLink(
        link='http://stackoverflow.com/users/5549/michaeljoseph',
        text="michaeljoseph's Stack Overflow profile",
        image_url='http://stackoverflow.com/users/flair/5549.png',
        align='width=208p height=58px',
    ))


JSDELIVR_DEVICONS = "https://cdn.jsdelivr.net/gh/devicons/devicon@master/icons"

DEVICONS_GITHUB = "https://github.com/devicons/devicon/raw/master/devicon.json"
DevIcon = namedtuple('DevIcon', 'name tags svg_url color')
Skill = namedtuple('Skill', 'name keywords level')

class HttpClient(CachedSession):
    def __init__(self, expire_after=None):
        CachedSession.__init__(self,
            cache_name='michaeljoseph.dev',
            use_temp=True,
            expire_after=timedelta(minutes=30) if expire_after is None else expire_after,
        )

def devicons():
    return {
        icon['name']: DevIcon(
            icon['name'],
            icon['tags'],
            f"{JSDELIVR_DEVICONS}/{icon['name']}/{icon['name']}-{icon['versions']['svg'][0]}.svg",
            icon['color'],
        )
        for icon in HttpClient().get(DEVICONS_GITHUB).json()
    }

def devicons_badges(company=None):
    skills_by_company = {
        job['id']: job['skills'].split()
        for job in load_resume()['work']
    }
    # log.debug(company, skills_by_company.keys(), company in skills_by_company)

    if company is None or company not in skills_by_company:
        unique_skills = set()
        for all_skills in skills_by_company.values():
            unique_skills |= set(all_skills)
        skills = list(unique_skills)
    else:
        skills = skills_by_company[company]

    # log.debug(company, skills)

    icons = devicons()
    return [
        IMG_ALT.format(i=Image(
            text=skill,
            image_url=icons[skill].svg_url,
            height='30px',
            width='80px',
            # align='height=20px width=20px',
            # align='height=28px width=77px',
        ))
        for skill in skills
        if skill in icons
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