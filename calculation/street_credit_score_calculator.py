from .category_score import CategoryScore
from .metric_score import MetricScore
from .street_credit_score import StreetCreditScore

from data import MetricCategory, Metric, MetricsFactory
from data.calculators.score_context import ScoreContext

from cached_property import cached_property

class StreetCreditScoreCalculator:
    """ Helper class to calculate a Person's Credit Score """
    MIN_SCORE = 300
        
    def calculate(self):
        """ Return the Street Credit Score """
        categories = MetricsFactory.loadAll()
        category_scores = [self.build_category_score(category) for category in categories]
        
        total_score = StreetCreditScore(category_scores)
        self.apply_pity_metric_if_necessary(total_score)
        return total_score

    def build_category_score(self, category):
        """ Build the Score for the given Category """
        metrics = []
        for group in category.metric_groups:
            metrics += group.pick_metrics()

        scores = []
        for metric in metrics:
            metric_score = MetricScore.from_metric(metric)
            scores.append(metric_score)

        return CategoryScore(category, scores)
        
    def apply_pity_metric_if_necessary(self, total_score):
        """ Apply the Pity Score if necessary """
        if total_score.score < self.MIN_SCORE:
            pity_category_score = self.get_pity_category_score(total_score)
            total_score.add_score(pity_category_score)
        
    def get_pity_category_score(self, total_score):
        """ Return the Pity Metric Category Score """
        category = MetricCategory('Pity Points', "Points awarded for having less Street Cred than a corpse (but don't feel too bad, zombies are pretty cool)", [])
        pity_metric_score = self.get_pity_metric_score(total_score.score)
        return CategoryScore(category, [pity_metric_score])
        
    def get_pity_metric_score(self, current_score):
        """ Return the Pity Metric Score """
        metric = Metric("Pity Points.", "Seriously! Somehow you're street cred is lower than a newborn baby. Uh, I guess here's some pity points so you can at least match them...", calculator=None)
        return MetricScore(metric, ScoreContext(self.MIN_SCORE - current_score))
    