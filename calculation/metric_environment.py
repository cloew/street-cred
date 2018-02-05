from jinja2 import Environment

metric_environment = Environment()

class MetricEnvironment:
    """ Helper class to facilitate parsing a Metric's name or description in a Score Context """
    
    def render(self, text, score_context):
        """ Render the text in the proper Score Context """
        return metric_environment.from_string(text).render(score_context.data)
        
MetricEnvironment = MetricEnvironment()
