Make sure metacontroller is [installed](https://github.com/shovanmaity/metacontroller-by-example/tree/master/metacontroller).

Apply the artifacts present in [deploy](https://github.com/shovanmaity/metacontroller-by-example/tree/master/basic-k8s/deploy) folder.
```bash
kubectl apply -f https://raw.githubusercontent.com/shovanmaity/metacontroller-by-example/master/basic-k8s/deploy/crd.yaml
```
Apply the [controller](https://github.com/shovanmaity/metacontroller-by-example/blob/master/basic-k8s/js/controller.yaml) for `Ping`
```bash
kubectl apply -f https://raw.githubusercontent.com/shovanmaity/metacontroller-by-example/master/basic-k8s/js/controller.yaml
```
Create a new ping. You can edit `ping.yaml` and apply that. One sample `Ping` is [here](https://github.com/shovanmaity/metacontroller-by-example/blob/master/basic/deploy/ping.yaml).
```yaml
apiVersion: example.com/v1
kind: Ping
metadata:
  name: shovan-maity
spec:
  name: Shovan Maity
```
Check `Pong` is created or not and validate the `spec.message`
```bash
kubectl get pong -o yaml
```
### Cleanup
```bash
kubectl delete ping --all
kubectl delete -f https://raw.githubusercontent.com/shovanmaity/metacontroller-by-example/master/basic-k8s/js/controller.yaml
kubectl delete -f https://raw.githubusercontent.com/shovanmaity/metacontroller-by-example/master/basic-k8s/deploy/crd.yaml
```
