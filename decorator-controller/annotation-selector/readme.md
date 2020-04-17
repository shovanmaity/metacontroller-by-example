If you do not want a reconcile all the objects then that can be done using annotation selector of `DecoratorController`.

Make sure metacontroller is [installed](https://github.com/shovanmaity/metacontroller-by-example/tree/master/metacontroller).

Make sure you are inside `decorator-controller/annotation-selector` directory.

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
Create a ping cr. Find the sample `Ping` is [here](https://github.com/shovanmaity/metacontroller-by-example/blob/master/decorator-controller/annotation-selector/deploy/ping.yaml).
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
Try

- Get pong and there will be no pong. Then annotate the ping object according to your controller.
- Now get pong object you will be able to get a pong cr.
- Remove the annotation in the ping cr and then edit it(`.spec.name`) changes will not be reflected in the pong cr.
- Add the annotation back and the adit the ping object(`.spec.name`) changes will be reflected in the pong cr.

### Cleanup
```bash
kubectl delete ping -A --all
kubectl delete -f deploy/controller.yaml
kubectl delete -f deploy/crd.yaml
# Stop the python file execution.
```
