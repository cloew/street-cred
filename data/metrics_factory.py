from .metric import Metric
from .calculators import CalculatorFactory

from kao_factory import DataBoundFactory, Factory, FieldArg
from kao_factory.Source.json_source import JsonSource

METRICS_FILENAME = "metrics.json"
        
simpleFactory = Factory(Metric, FieldArg("name"), FieldArg("description"), calculator=CalculatorFactory.LoadArg("calculator"))
        
MetricsFactory = DataBoundFactory(simpleFactory, JsonSource(METRICS_FILENAME))
