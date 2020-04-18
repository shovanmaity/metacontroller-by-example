from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Controller(BaseHTTPRequestHandler):

    def do_POST(self):
        observed = json.loads(self.rfile.read(
            int(self.headers.get("content-length"))))

        ping = observed["object"]

        name = ping.get("spec", {}).get("name", "Unknown")

        pong = [
            {
                "apiVersion": "example.com/v1",
                "kind": "Pong",
                "metadata": {
                    "name": ping["metadata"]["name"]
                },
                "spec": {
                    "message": "Hello %s !!" % name
                }
            }
        ]

        # Generate desired children
        desired = {
            "attachments": pong,
            "annotations": {
                "controller": "metacontroller"
            }
        }

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(desired).encode())


HTTPServer(("", 8080), Controller).serve_forever()
