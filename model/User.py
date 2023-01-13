from Player import *

class User(Player):
    def __init__(self):
        Player.__init__(self)
        self.username = ''

    def set_name(self, name):
        self.username = name

    def get_name(self):
        return self.username