
class MetricCategory:
    """ Represents a larger Category of related Metrics """
    
    def __init__(self, name, description, metric_groups):
        """ Initialize the Metric Category """
        self.name = name
        self.description = description
        self.metric_groups = metric_groups
