If you do not want a reconcile all the objects then that can be done using annotation selector of `DecoratorController`.

Update URL in the [controller](https://github.com/shovanmaity/metacontroller-by-example/blob/master/decorator-controller/annotation-selector/deploy/controller.yaml) in deploy folder.
```yaml
spec:
  hooks:
    sync:
      webhook:
        url: http://192.168.1.15:8080/sync
```
Apply the artifacts
```bash
# make sure you are in metacontroller-by-example/decorator-controller/annotation-selector this directory.
kubectl apply -f deploy/crd.yaml
kubectl apply -f deploy/controller.yaml
```
Execute python file
```bash
python3 python/sync.py
```
Sample `Ping` is [here](https://github.com/shovanmaity/metacontroller-by-example/blob/master/decorator-controller/annotation-selector/deploy/ping.yaml).

Try

- Try to get pong and there will be no pong. Then annotate the ping object according to your controller file.
  ```yaml
      annotationSelector:
        matchAnnotations:
          include: "true"
        #matchExpressions:
        #- key: include
          #operator: Exists
  ```
- Now try to get pong object you will be able to get a pong object.
- Remove the annotation in the ping object and then edit it(`.spec.name`) changes will not be reflected in the pong object.
- Add the annotation back and the adit the ping object(`.spec.name`) changes will be reflected in the pong object.
