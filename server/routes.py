from .controllers import GetScore

from kao_flask.endpoint import Endpoint
from kao_flask.controllers.html_controller import HTMLController

routes = [Endpoint('/', get=HTMLController('server/templates/index.html')),
          Endpoint('/api/score', get=GetScore)]
