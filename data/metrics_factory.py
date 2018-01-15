from .metric import Metric

from kao_factory import DataBoundFactory, Factory, FieldArg
from kao_factory.Source.json_source import JsonSource

METRICS_FILENAME = "metrics.json"
        
simpleFactory = Factory(Metric, FieldArg("name"), FieldArg("description"))
        
MetricsFactory = DataBoundFactory(simpleFactory, JsonSource(METRICS_FILENAME))
