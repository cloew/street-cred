from .routes import routes

from kao_flask import Server

server = Server(__name__, routes=routes)
