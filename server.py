from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
server_address = ('0.0.0.0', 8081)    
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
print('The Server is Running...')
httpd.serve_forever()
