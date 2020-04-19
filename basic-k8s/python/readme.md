### Prerequisite

Make sure metacontroller is [installed](https://github.com/shovanmaity/metacontroller-by-example/tree/master/metacontroller).

Make sure you are inside `basic-k8s/python` directory.

### Do it yourself

Apply the crd and controller.
```bash
kubectl apply -f ../deploy/crd.yaml
```

Apply the controller for `Ping`. I am deploying it in `metacontroller` namespace. You can deploy it in any namespace.
```bash
kubectl apply -f controller.yaml
```

Wait for controller pod to come in running state.
```bash
kubectl get pod -n metacontroller
```

Create a ping cr. Find the sample `Ping` is [here](https://github.com/shovanmaity/metacontroller-by-example/blob/master/basic-k8s/deploy/ping.yaml).
```bash
cat <<EOF | kubectl apply -f -
apiVersion: example.com/v1
kind: Ping
metadata:
  name: shovan
spec:
  name: Shovan Maity
EOF
```

Check the `Pong` cr and validate the message. `Pong` cr will be created in the same namespace in which `Ping` cr is present.
```bash
kubectl get pong -A
kubectl get pong -A -o=jsonpath='{range .items[*]}{@.spec.message}{"\n"}{end}'
```

### Cleanup

```bash
kubectl delete ping -A --all
kubectl delete -f controller.yaml
kubectl delete -f ../deploy/crd.yaml
```
