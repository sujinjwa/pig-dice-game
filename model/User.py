import Player


class User(Player):
    
    def __init__(self, username):
        Player.__init__(self)
        self.username = username

    def my_name(self):
        return self.username
    
