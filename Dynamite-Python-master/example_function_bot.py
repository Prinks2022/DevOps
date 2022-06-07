import random

dynamite = "100"

def make_move(rounds):
    #return 'S'
    print(rounds)
    if dynamite > 0:
        dynamite -= 1
        return 'D'
    options = ['R', 'P', 'S']

    return random.choice(options)