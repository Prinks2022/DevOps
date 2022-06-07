import random

class MyBot:
    def __init__(self):
        self.opp_dynamite = 100
        self.my_dynamite = 100

    def make_move(self, gamestate):
        if self.opp_dynamite > 0:
            self.opp_dynamite -= 1
            return 'W'
        
        if self.my_dynamite > 0:
            self.my_dynamite -= 1
            return 'D'
        
        options = ['R', 'P', 'S']

        return random.choice(options)