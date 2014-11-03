from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
import os

port = int(os.environ.get("PORT", 5000))

server = SimpleJSONRPCServer(('0.0.0.0', port))
server.register_function(pow)
server.register_function(lambda x,y: x+y, 'add')
server.register_function(lambda x: x, 'ping')
server.serve_forever()
