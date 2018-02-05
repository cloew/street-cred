from .fixed_score import FixedScore
from .score_in_range import ScoreInRange

from kao_factory import Factory, FieldArg, TypedFactory
        
CalculatorFactory = TypedFactory('type', {
    'FIXED':Factory(FixedScore, FieldArg("score")),
    'IN RANGE':Factory(ScoreInRange, low=FieldArg("low"), high=FieldArg("high")),
})
