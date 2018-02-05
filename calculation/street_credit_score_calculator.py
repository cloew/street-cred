from .metric_score import MetricScore
from .street_credit_score import StreetCreditScore

from data import Metric, MetricsFactory
from data.calculators.score_context import ScoreContext

from cached_property import cached_property

class StreetCreditScoreCalculator:
    """ Helper class to calculate a Person's Credit Score """
    MIN_SCORE = 300
        
    def calculate(self):
        """ Return the Street Credit Score """
        metrics = MetricsFactory.loadAll()
        
        scores = [self.being_alive_metric_score]
        for metric in metrics:
            metric_score = MetricScore.from_metric(metric)
            scores.append(metric_score)
        
        total_score = StreetCreditScore(scores)
        self.apply_pity_metric_if_necessary(total_score)
        return total_score
        
    def apply_pity_metric_if_necessary(self, total_score):
        """ Apply the Pity Score if necessary """
        if total_score.score < self.MIN_SCORE:
            pity_metric_score = self.get_pity_metric_score(total_score.score)
            total_score.add_score(pity_metric_score)
        
    @cached_property
    def being_alive_metric_score(self):
        """ Return the Being Alive Metric Score """
        metric = Metric("Being alive.", "Congratulations on not being dead! This entitles you to 300 Street Cred!", calculator=None)
        return MetricScore(metric, ScoreContext(self.MIN_SCORE))
        
    def get_pity_metric_score(self, current_score):
        """ Return the Pity Metric Score """
        metric = Metric("Pity Points.", "Seriously! Somehow you're street cred is lower than a newborn baby. Uh, I guess here's some pity points so you can at least match them...", calculator=None)
        return MetricScore(metric, ScoreContext(self.MIN_SCORE - current_score))
    