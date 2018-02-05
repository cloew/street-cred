from .score_context import ScoreContext

import random

class ScoreInRange:
    """ Helper class to calculate a Score within a particular range """
    
    def __init__(self, *, high, low=0):
        """ Initialize with the low and high thresholds """
        self.low = low
        self.high = high
        
    def calculate(self):
        """ Calculate the score """
        return ScoreContext(random.randint(self.low, self.high))
