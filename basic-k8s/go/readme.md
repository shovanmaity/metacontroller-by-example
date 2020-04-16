Make sure metacontroller is [installed](https://github.com/shovanmaity/metacontroller-by-example/tree/master/metacontroller).

Make sure you are inside `basic-k8s/go` directory.

Apply the crd present in `deploy` folder.
```bash
kubectl apply -f ../deploy/crd.yaml
```
Apply the controller  for `Ping`
```bash
kubectl apply -f controller.yaml
```
Create a new ping. You can edit `ping.yaml` and apply that. One sample `Ping` is [here](https://github.com/shovanmaity/metacontroller-by-example/blob/master/basic/deploy/ping.yaml).
```yaml
apiVersion: example.com/v1
kind: Ping
metadata:
  name: shovan
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
kubectl delete -f controller.yaml
kubectl delete -f ../deploy/crd.yaml
```
