from .fixed_score import FixedScore
from .pick_value_calculator import PickValueCalculator
from .score_in_range import ScoreInRange

from kao_factory import Factory, FieldArg, TypedFactory
        
CalculatorFactory = TypedFactory('type', {
    'FIXED':Factory(FixedScore, FieldArg("score")),
    'PICK VALUE':Factory(PickValueCalculator, low=FieldArg("low"), high=FieldArg("high")),
    'IN RANGE':Factory(ScoreInRange, low=FieldArg("low"), high=FieldArg("high")),
})
