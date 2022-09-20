from http.server import HTTPServer, CGIHTTPRequestHandler


class Startup:

    def start(self):
        server_address = ("localhost", 8000)
        print(server_address)
        httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
        httpd.serve_forever()
