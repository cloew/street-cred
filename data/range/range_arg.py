from .value_range import ValueRange

from kao_factory import FieldArg

def build_range(data):
    """ Build a Range from a string """
    low, high = data.split(':')
    return ValueRange(low=int(low), high=int(high))

def RangeArg(name):
    """ Helper to build a Range from a string """
    return FieldArg(name, build_range)
    