from .metric_score import MetricScore
from .street_credit_score import StreetCreditScore

from data import MetricsFactory

class StreetCreditScoreCalculator:
    """ Helper class to calculate a Person's Credit Score """
        
    def calculate(self):
        """ Return the Street Credit Score """
        metrics = MetricsFactory.loadAll()
        scores = []
        for metric in metrics:
            metric_score = MetricScore(metric=metric, score=200)
            scores.append(metric_score)
        return StreetCreditScore(scores)
        