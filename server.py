from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

server = SimpleJSONRPCServer(('localhost', 3030))
server.register_function(pow)
server.register_function(lambda x,y: x+y, 'add')
server.register_function(lambda x: x, 'ping')
server.serve_forever()
