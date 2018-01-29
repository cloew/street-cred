from data import MetricsFactory
from calculation import MetricScore, StreetCreditScore, StreetCreditScoreCalculator

from kao_json import JsonFactory, AsObj, ViaAttr

class GetScore:
    """Controller to get a score"""

    def perform():
        """ Calculate a score from avaliable metrics and return to user """
        score_calculator = StreetCreditScoreCalculator()
        calculated_score = score_calculator.calculate()
        # print(calculated_score.metric_scores)
        return(str(calculated_score.score))
