from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl


httpd = HTTPServer(('', 4443), SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket (httpd.socket, 
         certfile='cert.pem',
         keyfile="key.pem", server_side=True)

print("Listening at https://127.0.0.1:4443/ . . .", flush=True)
httpd.serve_forever()
