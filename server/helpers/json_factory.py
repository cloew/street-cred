from calculation import CategoryScore, MetricScore, StreetCreditScore
from data import Metric

from kao_json import JsonFactory, AsObj, ViaAttr

jsonFactory = JsonFactory({CategoryScore:AsObj(name=ViaAttr(), description=ViaAttr(), score=ViaAttr(), metric_scores=ViaAttr()),
                           MetricScore:AsObj(name=ViaAttr(), description=ViaAttr(), score=ViaAttr()),
                           StreetCreditScore:AsObj(category_scores=ViaAttr(), score=ViaAttr())})

toJson = jsonFactory.toJson
