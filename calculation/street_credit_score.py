
class StreetCreditScore:
    """ Represents a person's calculated Street Credit Score """
    
    def __init__(self, metric_scores):
        """ Initialize with the MetricScores """
        self.metric_scores = metric_scores
        
    @property
    def score(self):
        """ Return the total Street Credit Score """
        return sum(metric_score.score for metric_score in self.metric_scores)
        