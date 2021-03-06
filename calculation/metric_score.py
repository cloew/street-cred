from .metric_environment import MetricEnvironment
from proxy_attrs import proxy_for

@proxy_for('score_context', ['score'])
class MetricScore:
    """ Represents a particular Metric's Score """
    
    @classmethod
    def from_metric(cls, metric):
        """ Build a Metric Score from the given Metric """
        return cls(metric, metric.calculate())
    
    def __init__(self, metric, score_context):
        """ Initialize with the metric and score """
        self.metric = metric
        self.score_context = score_context
        
    @property
    def name(self):
        """ The name for this Metric """
        return MetricEnvironment.render(self.metric.name, self.score_context)
        
    @property
    def description(self):
        """ The description for this Metric """
        return MetricEnvironment.render(self.metric.description, self.score_context)
