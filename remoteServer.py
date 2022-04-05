from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import threading

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):

        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        message = json.loads(self.rfile.read(content_length))
        print(message)
        self._set_response()
        self.wfile.write(str(message).encode('utf-8'))

    def runServer(self):
            self.updateThread = threading.Thread(target=self.serve)
            self.updateThread.daemon = True
            self.updateThread.start()
            print("[INFO] HTTP server thread started....")

def serve():
            with HTTPServer((hostName, serverPort), MyServer) as webServer:
                try:
                    print("Server running...")
                    webServer.serve_forever()
                except KeyboardInterrupt:
                    pass

                webServer.server_close()
                print("Server stopped.")

if __name__ == "__main__":
    serve()