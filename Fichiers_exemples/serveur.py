#!/usr/bin/env python3

#!/usr/bin/python

import http.server
import os

PORT = 8888
server_address = ("", PORT)

server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]
print("Serveur actif sur le port :", PORT)
print("Racine du serveur dans",os.getcwd())

httpd = server(server_address, handler)
httpd.serve_forever()