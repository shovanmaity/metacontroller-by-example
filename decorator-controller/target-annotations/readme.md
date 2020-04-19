### Concept

A map of key-value pairs for annotations to set on the target object. You can specify this in the response of sync hook.

### Prerequisite

Make sure metacontroller is [installed](https://github.com/shovanmaity/metacontroller-by-example/tree/master/metacontroller).

Make sure you are inside `decorator-controller/target-annotations` directory.

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

Execute python files
```bash
python3 python/sync.py
```

Create a ping cr. Find the sample `Ping` is [here](https://github.com/shovanmaity/metacontroller-by-example/blob/master/decorator-controller/target-annotations/deploy/ping.yaml).
```bash
cat <<EOF | kubectl apply -f -
apiVersion: example.com/v1
kind: Ping
metadata:
  name: shovan
  annotations:
    name: shovan
spec:
  name: Shovan Maity
EOF
```

Check the status of ping cr
```yaml
kubectl get ping -A -o=jsonpath='{range .items[*]}{@.metadata.annotations}{"\n"}{end}'
```

### Cleanup

```bash
kubectl delete ping -A --all
kubectl delete -f deploy/controller.yaml
kubectl delete -f deploy/crd.yaml
# Stop the python files execution.
```
