from .metric_environment import MetricEnvironment
from proxy_attrs import proxy_for

@proxy_for('scoreContext', ['score'])
class MetricScore:
    """ Represents a particular Metric's Score """
    
    @classmethod
    def from_metric(cls, metric):
        """ Build a Metric Score from the given Metric """
        return cls(metric, metric.calculate())
    
    def __init__(self, metric, scoreContext):
        """ Initialize with the metric and score """
        self.metric = metric
        self.scoreContext = scoreContext
        
    @property
    def name(self):
        """ The name for this Metric """
        return MetricEnvironment.render(self.metric.name, self.scoreContext)
        
    @property
    def description(self):
        """ The description for this Metric """
        return MetricEnvironment.render(self.metric.description, self.scoreContext)
