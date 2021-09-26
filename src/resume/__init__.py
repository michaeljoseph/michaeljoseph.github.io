from itertools import product
from pathlib import Path
import json
import random


def get_resume(format, name='resume'):
    # TODO: load by format
    return (Path.cwd() / f'{name}.{format}').read_text()


def experience_skills(job_id=None):
    skills = {
        'quidco': "+php +laravel +symfony +node.js +python +flask +mkdocs +mysql +kubernetes +helm +docker +tilt +serverless +amazon-aws +cdk +sqs +lambda +alpine-linux",
        'intellection': "+ruby +ruby-on-rails +mysql +amazon-aws +chef +opsworks +docker +ansible",
        'yola': "+python +django +piston +php +java +amazon-aws +ubuntu",
        'sadalbari': "+java +documentation +consulting +finco +insureco +telco +ubuntu",
        'adapt-it': "+python +plone +zope +zodb +rhel +ubuntu",
        'jam-warehouse': "+php +mysql +freebsd +debian +c# +.net +asp.net +iis +python +plone +cms +zope +zodb +rhel",
        'itouch-labs': "+java +ftp +deployment +documentation +testing",
        'itouch-ie': "+php +java +jsp +ivr +4voice +sms +smpp +sybase +er +modelling +dbmodelling +redhat",
        'vodacom': "+holos +oracle +windows",
        'telkom': "+vb6 +msaccess +windows",
    }
    if not job_id or job_id not in skills:
        unique_skills = set()
        for all_skills in skills.values():
            unique_skills |= set(
                [s.strip() for s in all_skills.split('+') if s]
            )
        return unique_skills

    return [s.strip() for s in skills[job_id].split('+') if s]


def salutation_permutations():
    """Say 'Hello, my name is' in a bunch of ways"""
    hellojis = '👋 🌊 🙋 🖖'.split()

    hello = (
        'hello sawubona haai molo dumela'
        'hi yo sup hiya hey howzit hoesit aweh hola heita'
    ).split()
    hello.extend(['whakind eksê', 'hoe lyk it'])

    my_names_are = [
        'my name is',
        'my naam is',
        'igama lami ngu',
        'lebitso la ka ke'
    ]

    salutation_permutations = list(product(
        hellojis, hello, my_names_are
    ))
    random.shuffle(salutation_permutations)

    salutations =  [ 
        f'🤓{emoji} {hello}, {my_name_is} '
        for emoji, hello, my_name_is in salutation_permutations
    ]
    return salutations


TYPED_JS = "https://cdn.jsdelivr.net/npm/typed.js@2.0.12"
def typed_salutations():
    return typed_js('h1', salutation_permutations())

def typed_js(dom_element, things_to_type):
    options = json.dumps(dict(
        smartBackspace=True,
        startDelay=3000,
        showCursor=False,
        typeSpeed=50,
        strings=things_to_type,
    ))
 
    return '\n'.join([
        f'<script src="{TYPED_JS}"></script>',
        f"<script>var typed = new Typed('{dom_element}', {options});</script>",
    ])


BADGE_URL_TEMPLATE = "https://img.shields.io/badge/{badge_name}?style={style}&logo={logo}&logoColor={colour}"
SKILL_BADGE_MAP = {
    # browsers
    # version-control
    'git': 'git-%23F05033',
    'bitbucket': 'bitbucket-%230047B3',
    'github': 'github-%23121011',
    'gitlab': 'gitlab-%23181717',
    # +cvs, subversion, vss

    # languages
    'php': 'PHP-777BB4',
    'python': 'Python-3776AB',
    'node.js': 'Node.js-43853D',
    'c-sharp': 'C%23-239120',
    '.net': '.NET-5C2D91',
    'java': 'Java-ED8B00',
    'ruby': 'Ruby-CC342D',
    'markdown': 'Markdown-000000',
    'gnu-bash': 'Shell_Script-121011',

    # frameworks
    'django': 'Django-092E20',
    'ruby-on-rails': 'Ruby_on_Rails-CC0000',
    'laravel': 'Laravel-FF2D20',
    'flask': 'Flask-000000',

    # databases
    'mysql': 'MySQL-00000F',
    # sqlite, sybase, mssql, oracle

    # hosting
    'amazon-aws': 'Amazon_AWS-232F3E',

    # operating-system
    'windows': 'Windows-0078D6',
    'ubuntu': 'Ubuntu-E95420',
    'alpine-linux': 'Alpine_Linux-0D597F',
    # macos, fedora,
}
# TODO: automate https://github.com/Ileriayo/markdown-badges
# with categories
# language, framework, database

def generate_badge_url(skill):
    if skill not in SKILL_BADGE_MAP:
        return None
    skill_id = SKILL_BADGE_MAP[skill]

    return BADGE_URL_TEMPLATE.format(**dict(zip(
        'badge_name style logo colour'.split(),
        [skill_id, 'for-the-badge', skill, 'white'],
    )))
def skills_badge_urls(company=None):
    badges = [
        generate_badge_url(skill)
        for skill in experience_skills(company)
    ]
    # remove unrecognised skills
    badges = [b for b in badges if b]

    return ' '.join([f'<img src="{url}"/>' for url in badges])



def define_env(env):
    env.variables['skills_badge_urls'] = skills_badge_urls
    env.variables['typed_salutations'] = typed_salutations