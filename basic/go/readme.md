Make sure metacontroller is [installed](https://github.com/shovanmaity/metacontroller-by-example/tree/master/metacontroller).

Edit the deploy/controller.yaml and update the URL.
```yaml
spec:
  hooks:
    sync:
      webhook:
        url: http://192.168.1.15:8080/sync
```
Apply the artifacts present in [deploy](https://github.com/shovanmaity/metacontroller-by-example/tree/master/basic/deploy) folder.
```bash
kubectl delete -f https://raw.githubusercontent.com/shovanmaity/metacontroller-by-example/master/basic/deploy/controller.yaml
kubectl delete -f https://raw.githubusercontent.com/shovanmaity/metacontroller-by-example/master/basic/deploy/crd.yaml
```
Run the Go file
```bash
go run sync.go
```
Create a new ping. You can edit `ping.yaml` and apply that. One sample `Ping` is [here](https://github.com/shovanmaity/metacontroller-by-example/blob/master/basic/deploy/ping.yaml).
```yaml
apiVersion: example.com/v1
kind: Ping
metadata:
  name: shovan-maity
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
# Stop the go file execution.
kubectl delete -f https://raw.githubusercontent.com/shovanmaity/metacontroller-by-example/master/basic/deploy/controller.yaml
kubectl delete -f https://raw.githubusercontent.com/shovanmaity/metacontroller-by-example/master/basic/deploy/crd.yaml
```
