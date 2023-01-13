class User():
    def __init__(self):
        self.username = ''
        self.score = 0
        self.tmp_score = 0

    def set_name(self, name):
        self.username = name

    def get_name(self):
        return self.username
    
    def set_score(self, score):
        self.tmp_score += score
    
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