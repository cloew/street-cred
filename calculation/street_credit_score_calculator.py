from .metric_calculator import MetricCalculator
from .metric_score import MetricScore
from .street_credit_score import StreetCreditScore

from data import Metric, MetricsFactory

from cached_property import cached_property

class StreetCreditScoreCalculator:
    """ Helper class to calculate a Person's Credit Score """
        
    def calculate(self):
        """ Return the Street Credit Score """
        metrics = MetricsFactory.loadAll()
        metricCalculator = MetricCalculator()
        scores = [self.being_alive_metric]
        for metric in metrics:
            metric_score = metricCalculator.calculate(metric)
            scores.append(metric_score)
        return StreetCreditScore(scores)
        
    @cached_property
    def being_alive_metric(self):
        """ Return the Being Alive Metric Score """
        metric = Metric("Being alive.", "Congratulations on not being dead! This entitles you to 300 Street Cred!", calculator=None)
        return MetricScore(metric, 300)
    