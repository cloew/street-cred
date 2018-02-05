from .score_context import ScoreContext
from .value_range import ValueRange

class PickValueCalculator:
    """ Helper class to calculate a Score based on a calculation involving a value picked from a certain range """
    
    def __init__(self, *, high, low=0):
        """ Initialize with the low and high thresholds """
        self.range = ValueRange(low=low, high=high)
        
    def calculate(self):
        """ Calculate the score """
        value = self.range.pick_value()
        return ScoreContext(value, value=value)
