Metacontroller allows define upgrade strategy for chieldren. For `Recreate` - It immediately deletes any children that differ from the desired state, and recreate them in the desired state..

Update URL in the [controller](https://github.com/shovanmaity/metacontroller-by-example/blob/master/composite-controller/update-strategy-recreate/deploy/controller.yaml) in deploy folder.
```yaml
spec:
  hooks:
    sync:
      webhook:
        url: http://192.168.1.15:8080/sync
```
Apply the artifacts
```bash
# make sure you are in metacontroller-by-example/composite-controller/update-strategy-recreate this directory.
kubectl apply -f deploy/crd.yaml
kubectl apply -f deploy/controller.yaml
```
Execute python file
```bash
python3 python/sync.py
```
Sample `Ping` is [here](https://github.com/shovanmaity/metacontroller-by-example/blob/master/composite-controller/update-strategy-recreate/deploy/ping.yaml).

Try

- Get the `metadata.uid` of the pong object.
- Edit the ping and change the `spec.name` then check `metadata.uid` of the pong object it should not be same and message should contain updated name.
