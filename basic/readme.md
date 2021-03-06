### Overview

In this section, I will discuss on how you can run these controllers locally. One prerequisite is your local machine’s IP must be reachable from the Kubernetes cluster in which the `metacontroller` is running. You can use some tools like local-tunnel to get a public URL. I am using [k3s](https://k3s.io) in my local setup and my local machine’s IP is reachable from any pod. If meta-controller is not installed then you need to [install](https://github.com/shovanmaity/metacontroller-by-example/tree/master/metacontroller) it.

In these examples I will use 2 crds `Ping` and `Pong`. For custom resource `Ping` I will create a controller. `Ping` cr will contain name and other details. Controller will create a `Pong` resource for each `Ping`. In `Pong` cr you can find a greeting message.

### Example Controller
- [Go](https://github.com/shovanmaity/metacontroller-by-example/tree/master/basic/go)
- [Python](https://github.com/shovanmaity/metacontroller-by-example/tree/master/basic/python)
- [JavaScript](https://github.com/shovanmaity/metacontroller-by-example/tree/master/basic/js)
