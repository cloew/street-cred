from .metric_score import MetricScore

import random

class MetricCalculator:
    """ Helper class to calculate Metrics """
    
    def calculate(self, metric):
        """ Calculate the score for the given metric """
        score = random.randint(0, 200)
        return MetricScore(metric, score)
