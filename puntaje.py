class Score:
    def __init__(self):
        self.score = 0
        self.fails = 0
        self.hit = 0    

    @property
    def Current_score(self):
        return self.score
    
    @property
    def Fails(self):
        return self.fails    
    @Fails.setter
    def Fails(self, n_fail):
        self.fails = n_fail
    

    @property
    def Hit(self):
        return self.hit
    @Hit.setter
    def Hit(self,n_hit):
        self.hit = n_hit

    
    def Add_points(self,n_points):
        self.score += n_points
    
    def Add_fail(self,n_fail):
        self.fails += n_fail

    def Add_hit(self, n_hit):
        self.hit += n_hit