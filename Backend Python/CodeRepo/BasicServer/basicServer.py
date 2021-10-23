from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime
import json

hostName = "localhost"
serverPort = 8080
time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<img><head><title>Basic Python Server</title></head>", "utf-8"))
        self.wfile.write(bytes("<h1>Welcome to the Matrix, Neo</h1>", "utf-8"))
        self.wfile.write(bytes("<h3>Current time: %s</h3>" % time, "utf-8"))
        self.wfile.write(bytes("<p>You're up late tonight</p>", "utf-8"))
        self.wfile.write(bytes('<button><a href="/zion">Take the Red Pill...</a></button>', 'utf-8'))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), Server)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try: 
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
