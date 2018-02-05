from data import Metric, MetricsFactory
from calculation import MetricScore, StreetCreditScore, StreetCreditScoreCalculator

from ..helpers import toJson

class GetScore:
    """Controller to get a score"""

    def perform():
        """ Calculate a score from avaliable metrics and return to user """
        score_calculator = StreetCreditScoreCalculator()
        calculated_score = score_calculator.calculate()
        return(str({'result':toJson(calculated_score)}))
