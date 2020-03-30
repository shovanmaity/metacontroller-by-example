Metacontroller allows define upgrade strategy for chieldren. For `OnDelete` - It will not update existing children unless they get deleted by some other agent.

Update URL in the [controller](https://github.com/shovanmaity/metacontroller-by-example/blob/master/composite-controller/update-strategy-ondelete/deploy/controller.yaml) in deploy folder.
```yaml
spec:
  hooks:
    sync:
      webhook:
        url: http://192.168.1.15:8080/sync
```
Apply the artifacts
```bash
# make sure you are in metacontroller-by-example/composite-controller/update-strategy-ondelete this directory.
kubectl apply -f deploy/crd.yaml
kubectl apply -f deploy/controller.yaml
```
Execute python file
```bash
python3 python/sync.py
```
Sample `Ping` is [here](https://github.com/shovanmaity/metacontroller-by-example/blob/master/composite-controller/update-strategy-ondelete/deploy/ping.yaml).

Try

- Edit the ping and change the `spec.name` then check the pong object it's message should not contain updated name.
- Delete the pong object then check the pong object it's message should contain updated name.
