Make sure metacontroller is [installed](https://github.com/shovanmaity/metacontroller-by-example/tree/master/metacontroller).

Edit the deploy/controller.yaml and update it with your IP
```yaml
spec:
  hooks:
    sync:
      webhook:
        url: http://192.168.1.15:8080/sync
```
Apply the artifacts present in deploy folder.
```bash
kubectl apply -f crd.yaml
kubectl apply -f controller.yaml
```
Run the Go file
```bash
go run sync.go
```
Create a new ping. You can edit `ping.yaml` and apply that. One sample `Ping` is here.
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
1. Stop the go file execution.
2. kubectl delete -f controller.yaml
3. kubectl delete -f crd.yaml
```