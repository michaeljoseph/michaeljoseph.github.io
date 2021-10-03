from itertools import product
import json
import random


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
def typed_salutations():
    return typed_js('h1', salutation_permutations())

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
