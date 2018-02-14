from .score_context import ScoreContext
from ..range import ValueRange

class ScoreInRange:
    """ Helper class to calculate a Score within a particular range """
    
    def __init__(self, *, high, low=0):
        """ Initialize with the low and high thresholds """
        self.range = ValueRange(low=low, high=high)
        
    def calculate(self):
        """ Calculate the score """
        return ScoreContext(self.range.pick_value())
