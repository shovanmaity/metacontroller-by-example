If you set `spec.generateSelector` to `true` in your CompositeController definition, Metacontroller will do the following:

- When creating children for you, Metacontroller will automatically add a label that points to the parent object’s unique ID `metadata.uid`.
- Metacontroller will not expect each parent object to contain a spec.selector, and will ignore the value even if one is set.

Make sure metacontroller is [installed](https://github.com/shovanmaity/metacontroller-by-example/tree/master/metacontroller).

Make sure you are inside `composite-controller/generate-selector` directory.

Apply the crd.
```bash
kubectl apply -f deploy/crd.yaml
```

### Case-1
Edit the `deploy/case-1/controller.yaml` file and update the URL.
```yaml
spec:
  hooks:
    sync:
      webhook:
        url: http://192.168.1.15:8080/sync
```
Apply the controller.
```bash
kubectl apply -f deploy/case-1/controller.yaml
```
Create a ping cr using -
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
Get the `Pong` cr.
```
kubectl get pong -A -o=jsonpath='{range .items[*]}{@.metadata.labels}{"\n"}{end}'
```

### Cleanup
```
kubectl delete ping -A --all
kubectl delete -f deploy/case-1/controller.yaml
kubectl delete -f deploy/crd.yaml
# Stop the python file execution
```

### Case-2
Edit the `deploy/case-2/controller.yaml` file and update the URL.
```yaml
spec:
  hooks:
    sync:
      webhook:
        url: http://192.168.1.15:8080/sync
```
Apply the controller.
```bash
kubectl apply -f deploy/case-2/controller.yaml
```
Create a ping cr using -
```bash
cat <<EOF | kubectl apply -f -
apiVersion: example.com/v1
kind: Ping
metadata:
  name: shovan
spec:
  name: Shovan Maity
  selector:
    matchLabels:
      name: shovan
EOF
```
Get the `Pong` cr.
```
kubectl get pong -A -o=jsonpath='{range .items[*]}{@.metadata.labels}{"\n"}{end}'
```

### Cleanup
```
kubectl delete ping -A --all
kubectl delete -f deploy/case-2/controller.yaml
kubectl delete -f deploy/crd.yaml
# Stop the python file execution
```
