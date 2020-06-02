import http.server
import socketserver

port = 1234

h = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("",port),h)
print(("Server is up ...! "),port)
httpd.serve_forever