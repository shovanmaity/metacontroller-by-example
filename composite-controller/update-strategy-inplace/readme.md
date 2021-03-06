### Concept

Metacontroller allows define upgrade strategy for chieldren. For `InPlace` - it immediately updates any children that differ from the desired state.

### Prerequisite

Make sure metacontroller is [installed](https://github.com/shovanmaity/metacontroller-by-example/tree/master/metacontroller).

Make sure you are inside `composite-controller/update-strategy-inplace` directory.

### Do it yourself

Edit the `deploy/controller.yaml` file and update the webhook URL.
```yaml
spec:
  hooks:
    sync:
      webhook:
        url: http://192.168.1.15:8080/sync
```

Apply the crd and controller.
```bash
kubectl apply -f deploy/crd.yaml
kubectl apply -f deploy/controller.yaml
```

Execute python file
```bash
python3 python/sync.py
```

Create a ping cr. Find the sample `Ping` is [here](https://github.com/shovanmaity/metacontroller-by-example/blob/master/composite-controller/update-strategy-inplace/deploy/ping.yaml).
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

Get the `metadata.uid` of the pong cr.
```bash
kubectl get pong -o=jsonpath='{range .items[*]}{@.metadata.uid}{"\n"}{end}'
```

Edit the ping and change the `spec.name` then check `metadata.uid` of the pong cr. It should be same and message should contain updated name.
```bash
kubectl get pong -o=jsonpath='{range .items[*]}{@.spec.message}{"\n"}{end}'
```

### Cleanup

```bash
kubectl delete ping -A --all
kubectl delete -f deploy/controller.yaml
kubectl delete -f deploy/crd.yaml
# Stop the python file execution.
```
