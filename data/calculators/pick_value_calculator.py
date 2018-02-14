from .score_context import ScoreContext
from ..range import ValueRange

from jinja2 import Environment

score_environment = Environment()

class PickValueCalculator:
    """ Helper class to calculate a Score based on a calculation involving a value picked from a certain range """
    
    def __init__(self, *, high, low=0, score_expr=None):
        """ Initialize with the low and high thresholds """
        self.range = ValueRange(low=low, high=high)
        self.score_expr = score_expr
        
    def calculate(self):
        """ Calculate the score """
        value = self.range.pick_value()
        score = score_environment.compile_expression(self.score_expr)(value=value) if self.score_expr else value
        return ScoreContext(score, value=value)
