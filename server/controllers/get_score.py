from data import Metric, MetricsFactory
from calculation import MetricScore, StreetCreditScore, StreetCreditScoreCalculator

from ..helpers import toJson

import json

class GetScore:
    """Controller to get a score"""

    def perform():
        """ Calculate a score from avaliable metrics and return to user """
        score_calculator = StreetCreditScoreCalculator()
        calculated_score = score_calculator.calculate()
        return(json.dumps({"result":toJson(calculated_score)}))
