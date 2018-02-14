from .metric import Metric
from .metric_group import MetricGroup
from .calculators import CalculatorFactory
from .range import RangeArg

from kao_factory import DataBoundFactory, Factory, FieldArg
from kao_factory.Source.json_source import JsonSource

METRICS_FILENAME = "metrics.json"
        
metricFactory = Factory(Metric, FieldArg("name"), FieldArg("description"), calculator=CalculatorFactory.LoadArg("calculator"))
groupFactory = Factory(MetricGroup, RangeArg("range"), metricFactory.LoadAllArg("metrics"))
        
MetricsFactory = DataBoundFactory(groupFactory, JsonSource(METRICS_FILENAME))
