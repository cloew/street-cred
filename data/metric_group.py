import random

class MetricGroup:
    """ Represents a Group metrics that can be selected from """
    
    def __init__(self, metric_count_range, metrics):
        """ Initialize the Metric Group """
        self.metric_count_range = metric_count_range
        self.metrics = metrics
        
    def pick_metrics(self):
        """ Return the randomly selected metrics """
        number_to_pick = self.metric_count_range.pick_value()
        return random.sample(self.metrics, number_to_pick)
