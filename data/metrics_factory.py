from .metric import Metric

class MetricsFactory:
    """ Helper class to load the Existing Metrics """
    
    def load_all(self):
        """ Return all the available Metrics """
        return [
            Metric("Prefers exactly 49 slices of pepperoni on a pizza.", "The perfect amount! (Proven by SCIENCE!)"),
            Metric("Uses Facebook.", "Seriously?! You know who uses Facebook? Your parents. And their parents. And Grumpy Cat!"),
            Metric("Saved a baby from an alligator by punching it in the face.", "We're gonna level with you. We have no idea if this happened, but it sounded AWESOME!!! And everybody's talking about so we figured we'd give it to ya."),
        ]
        
MetricsFactory = MetricsFactory()
