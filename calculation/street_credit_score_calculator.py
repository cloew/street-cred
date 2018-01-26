from .metric_calculator import MetricCalculator
from .street_credit_score import StreetCreditScore

from data import MetricsFactory

class StreetCreditScoreCalculator:
    """ Helper class to calculate a Person's Credit Score """
        
    def calculate(self):
        """ Return the Street Credit Score """
        metrics = MetricsFactory.loadAll()
        metricCalculator = MetricCalculator()
        scores = []
        for metric in metrics:
            metric_score = metricCalculator.calculate(metric)
            scores.append(metric_score)
        return StreetCreditScore(scores)
        