Make sure metacontroller is [installed](https://github.com/shovanmaity/metacontroller-by-example/tree/master/metacontroller).

Make sure you are inside `basic-k8s/js` directory.

Apply the crd present in `deploy` folder.
```bash
kubectl apply -f ../deploy/crd.yaml
```
Apply the controller for `Ping`. I am deploying it in `metacontroller` namespace. You can deploy it in any namespace. For that, you have to edit `controller.yaml`.
```bash
kubectl apply -f controller.yaml
```
Wait for controller pod to come in running state.

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
Check `Pong` is created or not and validate the `spec.message` using `kubectl get pong -A -o=jsonpath='{range .items[*]}{@.spec.message}{"\n"}{end}'`. `Pong` cr will be created in the same namespace in which `Ping` cr is present.
```bash
kubectl get pong -A -o yaml
```
### Cleanup
```bash
kubectl delete ping -A --all
kubectl delete -f controller.yaml
kubectl delete -f ../deploy/crd.yaml
```
