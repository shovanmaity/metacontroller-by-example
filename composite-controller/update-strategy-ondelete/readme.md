### Concept

Metacontroller allows define upgrade strategy for chieldren. For `OnDelete` - it does not update existing children unless they get deleted by some other agent.

### Prerequisite

Make sure metacontroller is [installed](https://github.com/shovanmaity/metacontroller-by-example/tree/master/metacontroller).

Make sure you are inside `composite-controller/update-strategy-ondelete` directory.

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

Create a ping cr. Find the sample `Ping` is [here](https://github.com/shovanmaity/metacontroller-by-example/blob/master/composite-controller/update-strategy-ondelete/deploy/ping.yaml).
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

Edit the ping and change the `spec.name` then check the pong object it's message should not contain updated name
```bash
kubectl get pong -o=jsonpath='{range .items[*]}{@.spec.message}{"\n"}{end}'
```

Delete the pong object then check the pong object it's message should contain updated name.

### Cleanup

```bash
kubectl delete ping -A --all
kubectl delete -f deploy/controller.yaml
kubectl delete -f deploy/crd.yaml
# Stop the python file execution.
```
