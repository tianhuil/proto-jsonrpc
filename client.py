import jsonrpclib
import sys

host = sys.argv[1]
if host == 'localhost':
  server = jsonrpclib.Server('http://localhost:5000')
else:
  server = jsonrpclib.Server('https://' + host + '.herokuapp.com:443')

server.add(5,6)
print jsonrpclib.history.request
print jsonrpclib.history.response
server.add(x=5, y=10)
server._notify.add(5,6)
batch = jsonrpclib.MultiCall(server)
batch.add(5, 6)
batch.ping({'key':'value'})
batch._notify.add(4, 30)
results = batch()
for result in results:
  print result
