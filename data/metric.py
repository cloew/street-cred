
class Metric:
    """ Represents a Metric for calculating the Street Credit Score """
    
    def __init__(self, name, description):
        """ Initialize with the name and description """
        self.name = name
        self.description = description

    def __repr__(self):
        """ Return the String Representation of the Metric """
        return "<Metric({}, {})>".format(self.name, self.description)
        