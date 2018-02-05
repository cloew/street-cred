from calculation import MetricScore, StreetCreditScore
from data import Metric

from kao_json import JsonFactory, AsObj, ViaAttr

jsonFactory = JsonFactory({Metric:AsObj(name=ViaAttr(), description=ViaAttr()),
                        #    MetricScore:AsObj(metric=ViaAttr(), score=ViaAttr()),
                           StreetCreditScore:AsObj(metric_scores=ViaAttr(), score=ViaAttr())})

toJson = jsonFactory.toJson