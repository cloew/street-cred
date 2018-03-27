from proxy_attrs import proxy_for

@proxy_for('category', ['name'])
class CategoryScore:
    """ Represents a person's calculated Street Credit Score in a particular Category """
    
    def __init__(self, category, metric_scores):
        """ Initialize with the MetricScores """
        self.category = category
        self.metric_scores = metric_scores
        
    @property
    def score(self):
        """ Return the total Street Credit Score """
        return sum(metric_score.score for metric_score in self.metric_scores)
        