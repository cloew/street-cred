from .score_in_range import ScoreInRange

from kao_factory import Factory, FieldArg
        
CalculatorFactory = Factory(ScoreInRange, low=FieldArg("low"), high=FieldArg("high"))
