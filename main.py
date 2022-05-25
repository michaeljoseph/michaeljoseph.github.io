import json
import random
import yaml

from collections import namedtuple
from datetime import timedelta
from functools import partial
from itertools import product
from pathlib import Path

import requests

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
    for icon in requests.get(DEVICONS_GITHUB).json()
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

def salutation_permutations():
    """Say 'Hello, my name is' in a bunch of ways"""
    hellojis = '👋 🌊 🙋 🖖'.split()
    # https://www.babbel.com/en/magazine/how-to-say-hello-in-10-different-languages
    hello = """
        hi yo oi
        sup hey olá hoi hai hej
        ciao hiya aweh hola haai molo 
        heita hello salut ahlan 
        howzit hoesit dumela halløj goddag 
        sawubona 
    """.split()
    hello.extend(['whakind eksê', 'hoe lyk it'])
    hello = 'hi yo sup hiya hey haai aweh hola molo haai'.split()
    # my_names_are = ['my name is', 'my naam is', 'igama lami ngu']
    popeyes = ["i'm ", "ek is ", "ngingu", "ke "]
    amongst_our_names = "michael michel mikhail mihály mícheál michele michal miguel mihail michiel mikel mihangel mícheál mikkel".split()

    # https://smodin.io/translate-one-text-into-multiple-languages

    salutation_permutations = list(product(
        hellojis, hello, popeyes, amongst_our_names
    ))
    random.shuffle(salutation_permutations)

    salutations =  [ 
        f'🤓{emoji}{hello}, {my_name_is}{me}'
        for emoji, hello, my_name_is, me in salutation_permutations
    ]
    return salutations

TYPED_JS = "https://cdn.jsdelivr.net/npm/typed.js@2.0.12"
TYPED_TEMPLATE = """
<script src="{js_url}"></script>
<script>
    var typed = new Typed('{dom_element}', {options});
</script>
"""

def typed_js(dom_element, things_to_type):
    options = json.dumps(dict(
        startDelay=3000,
        smartDelete=True,
        showCursor=False,
        typeSpeed=50,
        strings=things_to_type,
    ))
    return TYPED_TEMPLATE.format(
        js_url=TYPED_JS,
        dom_element=dom_element,
        options=options
    )

def skills_badges(company=None):
    return NLJ(devicons_badges(company))

def typed_salutations():
    return typed_js('h1', salutation_permutations())

def define_env(env):
    env.variables['skills_badges'] = skills_badges
    env.variables['typed_salutations'] = typed_salutations
