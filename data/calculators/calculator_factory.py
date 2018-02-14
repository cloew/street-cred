from .fixed_score import FixedScore
from .pick_value_calculator import PickValueCalculator
from .score_in_range import ScoreInRange
from ..range import RangeArg

from kao_factory import Factory, FieldArg, TypedFactory
        
CalculatorFactory = TypedFactory('type', {
    'FIXED':Factory(FixedScore, FieldArg("score")),
    'PICK VALUE':Factory(PickValueCalculator, RangeArg("range"), score_expr=FieldArg("score")),
    'IN RANGE':Factory(ScoreInRange, RangeArg("range")),
})
