from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Controller(BaseHTTPRequestHandler):
  def sync(self, parent, children):
    # Generate the desired child object.
    name = parent.get("spec", {}).get("name","Unknown")
    desired_ping_reply = [
      {
        "apiVersion": "example.com/v1",
        "kind": "Pong",
        "metadata": {
          "name": parent["metadata"]["name"]
        },
        "spec": {
          "message": "Hello %s !!" % name
        }
      }
    ]

    return {"children": desired_ping_reply}

  def do_POST(self):
    # Serve the sync() function as a JSON webhook.
    observed = json.loads(self.rfile.read(int(self.headers.get("content-length"))))
    desired = self.sync(observed["parent"], observed["children"])

    self.send_response(200)
    self.send_header("Content-type", "application/json")
    self.end_headers()
    self.wfile.write(json.dumps(desired).encode())

HTTPServer(("", 8080), Controller).serve_forever()
