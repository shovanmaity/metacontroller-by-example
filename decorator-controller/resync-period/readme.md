### Concept
By default, your sync hook will only be called when something changes in one of the resources you’re watching, or when the local cache is flushed. The `resyncPeriodSeconds` value specifies how often to do this. Each time it triggers, Metacontroller will send sync hook requests for all objects of the parent resource type, with the latest observed values of all the necessary objects.

### Prerequisite

Make sure metacontroller is [installed](https://github.com/shovanmaity/metacontroller-by-example/tree/master/metacontroller).

Make sure you are inside `decorator-controller/resync-period` directory.

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

Create a ping cr. Find the sample `Ping` is [here](https://github.com/shovanmaity/metacontroller-by-example/blob/master/decorator-controller/resync-period/deploy/ping.yaml).
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

Check the logs of python file execution.

### Cleanup

```bash
kubectl delete ping -A --all
kubectl delete -f deploy/controller.yaml
kubectl delete -f deploy/crd.yaml
# Stop the python files execution.
```
