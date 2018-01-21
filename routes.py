from controllers import GetScore

from kao_flask.endpoint import Endpoint

routes = [Endpoint('/', get=GetScore)]
