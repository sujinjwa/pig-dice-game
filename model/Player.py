class Player:
    def __init__(self):
        self.score = 0
        self.tmp_score = 0

    def get_score(self):
        return self.score
    
    def get_tmp_score(self):
        return self.tmp_score

    def reset_tmp_score(self):
        self.tmp_score = 0
    
    def reset_score(self):
        self.score = 0
    
    def add_score(self):
        self.score += self.tmp_score