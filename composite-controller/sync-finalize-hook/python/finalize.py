from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Controller(BaseHTTPRequestHandler):

    def do_POST(self):
        observed = json.loads(self.rfile.read(
            int(self.headers.get("content-length"))))
        observed_pong_map = observed["children"].get(
            "Pong.example.com/v1", {})

        finalized = len(observed_pong_map) == 0
        desired = {
            "finalized": finalized
        }

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(desired).encode())


HTTPServer(("", 9090), Controller).serve_forever()
