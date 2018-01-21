from routes import routes

from kao_flask import Server

server = Server(__name__, routes=routes)

if __name__ == '__main__':
	server.run(debug=True)
