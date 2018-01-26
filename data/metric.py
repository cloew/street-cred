from proxy_attrs import proxy_for

@proxy_for('calculator', ['calculate'])
class Metric:
    """ Represents a Metric for calculating the Street Credit Score """
    
    def __init__(self, name, description, *, calculator):
        """ Initialize with the name and description """
        self.name = name
        self.description = description
        self.calculator = calculator

    def __repr__(self):
        """ Return the String Representation of the Metric """
        return "<Metric({}, {})>".format(self.name, self.description)
        