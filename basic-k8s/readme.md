### Overview

In this section, I will discuss on how you can run these controllers in the Kubernetes environment. If meta-controller is not installed then you need to [install](https://github.com/shovanmaity/metacontroller-by-example/tree/master/metacontroller) it.

In these examples I will use 2 crds `Ping` and `Pong`. For custom resource `Ping` I will create a controller. `Ping` cr will contain name and other details. Controller will create a `Pong` resource for each `Ping`. In `Pong` cr you can find a greeting message.

### Example Controller
- [Go](https://github.com/shovanmaity/metacontroller-by-example/tree/master/basic-k8s/go)
- [Python](https://github.com/shovanmaity/metacontroller-by-example/tree/master/basic-k8s/python)
- [JavaScript](https://github.com/shovanmaity/metacontroller-by-example/tree/master/basic-k8s/js)
