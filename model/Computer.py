import Player
from random import randint


class Computer(Player):

    def __init__(self):
        Player.__init__(self)
        self.chance = 0
    
    def set_chance(self):
        chance = randint(8, 15)
    
    def get_chance(self):
        return self.chance
    