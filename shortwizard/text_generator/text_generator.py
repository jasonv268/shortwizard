import random


def get_random_food():
    fonds = ["un kebab", "un tacos","un grec","un macdo","un coca"]

    return random.choice(fonds)


def get_random_hook():

    x = 1

    hooks = [f"Jour {x} pour devenir plus intelligent !",""] 

    return random.choice(hooks)