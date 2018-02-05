
class FixedScore:
    """ Helper class to calculate a Score that is fixed to a certain value """
    
    def __init__(self, score):
        """ Initialize with the fixed score """
        self.score = score
        
    def calculate(self):
        """ Calculate the score """
        return self.score
