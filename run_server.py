from server import server

application = server.app

if __name__ == '__main__':
	server.run(debug=True)
