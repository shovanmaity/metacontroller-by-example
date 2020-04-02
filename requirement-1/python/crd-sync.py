from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Controller(BaseHTTPRequestHandler):

    def do_POST(self):

        crd = [
            {
                "apiVersion": "apiextensions.k8s.io/v1beta1",
                "kind": "CustomResourceDefinition",
                "metadata": {
                    "name": "pongs.example.com"
                },
                "spec": {
                    "group": "example.com",
                    "version": "v1",
                    "names": {
                        "kind": "Pong",
                        "singular": "pong",
                        "plural": "pongs"
                    },
                    "scope": "Namespaced"
                }
            }
        ]

        # Generate desired children
        desired = {
            "children": crd
        }

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(desired).encode())


HTTPServer(("", 8080), Controller).serve_forever()
