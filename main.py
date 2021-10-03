from resume.badges import skills_badges
from resume.salutations import typed_salutations

def define_env(env):
    env.variables['skills_badges'] = skills_badges
    env.variables['typed_salutations'] = typed_salutations
