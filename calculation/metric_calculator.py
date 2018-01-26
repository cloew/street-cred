from .metric_score import MetricScore

class MetricCalculator:
    """ Helper class to calculate Metrics """
    
    def calculate(self, metric):
        """ Calculate the score for the given metric """
        return MetricScore(metric, metric.calculate())
