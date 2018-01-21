from data import MetricsFactory

class GetScore:
    """Controller to get a score"""

    def perform():
        """ Calculate a score from avaliable metrics and return to user """
        #TODO: Get metrics and calculate score.        
        this_metric = '{"name": "foo", "description": "bar"}'
        return('{"score": 85}')
