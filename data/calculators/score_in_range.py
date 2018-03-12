from .score_context import ScoreContext

class ScoreInRange:
    """ Helper class to calculate a Score within a particular range """
    
    def __init__(self, range):
        """ Initialize with the low and high thresholds """
        self.range = range
        
    def calculate(self):
        """ Calculate the score """
        return ScoreContext(self.range.pick_value())
