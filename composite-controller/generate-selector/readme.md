The parent resource of a CompositeController is assumed to have a spec.selector that contains matchLabels and/or matchExpressions. The parent’s label selector determines which child objects a given parent will try to manage, according to the ControllerRef rules. Metacontroller automatically handles orphaning and adoption for you, and will only send you the observed states of children you own.

These rules imply:

1. Children you create must have labels that satisfy the parent’s selector, or else they will be immediately orphaned and you’ll never see them again.
2. If other controllers or users create orphaned objects that match the parent’s selector, Metacontroller will try to adopt them for you.
3. If Metacontroller adopts an object, and you subsequently decline to list that object in your desired list of children, it will get deleted (because you now own it, but said you don’t want it).

More details [here](https://metacontroller.app/api/compositecontroller).

Common step -

Update URL in the [controller](https://github.com/shovanmaity/metacontroller-by-example/blob/master/composite-controller/generate-selector/deploy/controller.yaml) in deploy folder.
```yaml
spec:
  hooks:
    sync:
      webhook:
        url: http://192.168.1.15:8080/sync
```
Apply the artifacts
```bash
# make sure you are in metacontroller-by-example/composite-controller/generate-selector this directory.
kubectl apply -f deploy/crd.yaml
kubectl apply -f deploy/controller.yaml
```
Execute python file
```bash
python3 python/sync.py
```
Sample `Ping` is [here](https://github.com/shovanmaity/metacontroller-by-example/blob/master/composite-controller/generate-selector/deploy/ping-match-labels.yaml) or [here](https://github.com/shovanmaity/metacontroller-by-example/blob/master/composite-controller/generate-selector/deploy/ping-match-expressions.yaml)

Try

- To create some more `Pong` with same label (which label selector present in `Ping`)
- Comment out bellow lines in python script any re run it.
    ```python
    # Comment out below 3 lines to try with other option
    for name, observed_pong in observed_pong_map.items():
      if name != ping["metadata"]["name"]:
        desired.append(observed_pong)
    ```
- Check the status of ping object
    ```yaml
        status:
          observedGeneration: 9511
          replicas: 2
    ```
---
If you set spec.generateSelector to true in your CompositeController definition, Metacontroller will do the following:

- When creating children for you, Metacontroller will automatically add a label that points to the parent object’s unique ID (metadata.uid).
- Metacontroller will not expect each parent object to contain a spec.selector, and will ignore the value even if one is set.

To try this

Hope you cleaned up previously applied artifacts

Update URL in the [controller](https://github.com/shovanmaity/metacontroller-by-example/blob/master/composite-controller/generate-selector/deploy/controller.yaml) in deploy folder.
```yaml
spec:
  hooks:
    sync:
      webhook:
        url: http://192.168.1.15:8080/sync
```

And add the below in controller.yaml
```yaml
spec:
  generateSelector: true
```
Apply the artifacts
```bash
# make sure you are in metacontroller-by-example/composite-controller/generate-selector this directory.
kubectl apply -f deploy/crd.yaml
kubectl apply -f deploy/controller.yaml
```
Comment out bellow lines in python script any re run it.
```python
# Comment out below 3 lines to try with other option
for name, observed_pong in observed_pong_map.items():
  if name != ping["metadata"]["name"]:
    desired.append(observed_pong)
```
Execute python file
```bash
python3 python/sync.py
```
Sample `Ping` is [here](https://github.com/shovanmaity/metacontroller-by-example/blob/master/composite-controller/generate-selector/deploy/ping.yaml). Create a `Ping` and get the `-o yaml` of ping and pong. You will find the difference.