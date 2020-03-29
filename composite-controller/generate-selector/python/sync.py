from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Controller(BaseHTTPRequestHandler):

  def do_POST(self):

    # Observed ping object
    observed = json.loads(self.rfile.read(int(self.headers.get("content-length"))))
    ping = observed["parent"]
    observed_pong_map = observed["children"].get("Pong.example.com/v1",{})

    name = ping.get("spec", {}).get("name","Unknown")

    pong = {
      "apiVersion": "example.com/v1",
      "kind": "Pong",
      "metadata": {
        "name": ping["metadata"]["name"],
        "labels": {
          "name": ping["metadata"]["name"]
        }
      },
      "spec": {
        "message": "Hello %s !!" % name
      }
    }

    desired_children = []

    # Comment out below 3 lines to try with other option
    for name, observed_pong in observed_pong_map.items():
      if name != ping["metadata"]["name"]:
        desired_children.append(observed_pong)

    desired_children.append(pong)

    # Generate desired children
    desired = {
      "children": desired_children,
      "status": {
        "replicas": len(desired_children)
      }
    }

    self.send_response(200)
    self.send_header("Content-type", "application/json")
    self.end_headers()
    self.wfile.write(json.dumps(desired).encode())

HTTPServer(("", 8080), Controller).serve_forever()
