import random

class ValueRange:
    """ Helper class to pick a value in a certain range """
    
    def __init__(self, *, low, high):
        """ Initialize the range with the lowest and highest possible values """
        self.low = low
        self.high = high
        
    def pick_value(self):
        """ Pick a random value from the range """
        return random.randint(self.low, self.high)
