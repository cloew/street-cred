
class MetricScore:
    """ Represents a particular Metric's Score """
    
    @classmethod
    def from_metric(cls, metric):
        """ Build a Metric Score from the given Metric """
        return cls(metric, metric.calculate())
    
    def __init__(self, metric, score):
        """ Initialize with the metric and score """
        self.metric = metric
        self.score = score
        
