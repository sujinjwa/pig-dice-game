from random import randint

class Dice:
    def __init__(self):
        self.number = 0

    def roll(self):
        self.number = randint(1, 6)
    
    def get_number(self):
        return self.number