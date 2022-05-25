from resume import NLJ, shields_badges
from resume.badges import devicons_badges
from resume.salutations import typed_salutations

def skills_badges(company=None):
    return NLJ(devicons_badges(company))
def define_env(env):
    env.variables['skills_badges'] = skills_badges
    env.variables['typed_salutations'] = typed_salutations
