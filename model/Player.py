class Player:

    def __init__(self, username):
        self.score = 0
        self.tmp_score = 0
        self.username = username

    def my_score(self):
        return self.score
    
    def my_tmp_score(self):
        return self.tmp_score

    def reset_score(self):
        self.tmp_score = 0
    
    def add_score(self):
        self.score += self. tmp_score