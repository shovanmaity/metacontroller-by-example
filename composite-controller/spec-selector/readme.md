### Concept

The parent resource of a `CompositeController` is assumed to have a `spec.selector` that contains `matchLabels` and/or `matchExpressions`. The parent’s label selector determines which child objects a given parent will try to manage, according to the ControllerRef rules. Metacontroller automatically handles orphaning and adoption for you, and will only send you the observed states of children you own.

These rules imply:

1. Children you create must have labels that satisfy the parent’s selector, or else they will be immediately orphaned and you’ll never see them again.
2. If other controllers or users create orphaned objects that match the parent’s selector, Metacontroller will try to adopt them for you.
3. If Metacontroller adopts an object, and you subsequently decline to list that object in your desired list of children, it will get deleted.

### Prerequisite

Make sure metacontroller is [installed](https://github.com/shovanmaity/metacontroller-by-example/tree/master/metacontroller).

Make sure you are inside `composite-controller/spec-selector` directory.

### Do it yourself

Edit the `deploy/controller.yaml` file and update the URL.
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

Create a ping cr using -
```bash
cat <<EOF | kubectl apply -f -
apiVersion: example.com/v1
kind: Ping
metadata:
  name: shovan
  labels:
    name: shovan
spec:
  name: Shovan Maity
  selector:
    matchExpressions:
      - key: name
        operator: In
        values:
          - shovan
EOF
```

Or
```bash
cat <<EOF | kubectl apply -f -
apiVersion: example.com/v1
kind: Ping
metadata:
  name: shovan
  labels:
    name: shovan
spec:
  name: Shovan Maity
  selector:
    matchLabels:
      name: shovan
EOF
```

### Case-1

Execute python file.
```bash
python3 python/case-1/sync.py
```

Check for pong cr. You will not find any pong as we are not setting label in pong cr in python code `case-1/sync.py`.
```bash
kubectl get pong -A
```

### Case-2

Stop the python file execution and execute another python file
```bash
python3 python/case-2/sync.py
```

Check for pong cr. You will find one pong.
```bash
kubectl get pong -A
```

Run the below command and saw the output
```
kubectl get pong -A -o=jsonpath='{range .items[*]}{@.metadata.ownerReferences}{"\n"}{end}'
kubectl get ping -A -o=jsonpath='{range .items[*]}{@.status.replicas}{"\n"}{end}'
```

Create a new pong with same label
```bash
cat <<EOF | kubectl apply -f -
apiVersion: example.com/v1
kind: Pong
metadata:
  labels:
    name: shovan
  name: shovan-tmp
  namespace: default
spec:
  message: Hello Shovan Maity !!
EOF
```

Run the below command and saw the output
```
kubectl get pong -A -o=jsonpath='{range .items[*]}{@.metadata.ownerReferences}{"\n"}{end}'
kubectl get ping -A -o=jsonpath='{range .items[*]}{@.status.replicas}{"\n"}{end}'
```

Remove the label from newly created pong cr
```bash
kubectl label pong shovan-tmp name-
```

Run the below command and saw the output
```
kubectl get pong -A -o=jsonpath='{range .items[*]}{@.metadata.ownerReferences}{"\n"}{end}'
kubectl get ping -A -o=jsonpath='{range .items[*]}{@.status.replicas}{"\n"}{end}'
```

Delete the new pong cr
```bash
kubectl delete pong shovan-tmp
```

### Case-3

Stop the python file execution and execute another python file
```bash
python3 python/case-3/sync.py
```

Check the pong cr
```bash
kubectl get pong -A
```

Check the ping cr's replicas
```bash
kubectl get ping -A -o=jsonpath='{range .items[*]}{@.status.replicas}{"\n"}{end}'
```

Create a new pong with same label
```bash
cat <<EOF | kubectl apply -f -
apiVersion: example.com/v1
kind: Pong
metadata:
  labels:
    name: shovan
  name: shovan-tmp
  namespace: default
spec:
  message: Hello Shovan Maity !!
EOF
```

Check the ping cr's replicas
```bash
kubectl get ping -A -o=jsonpath='{range .items[*]}{@.status.replicas}{"\n"}{end}'
```

It will be 1, newly created pong cr will be deleted as python code in `case-3/ping.py` declines to list that cr.

### Cleanup

```
kubectl delete ping -A --all
kubectl delete -f deploy/controller.yaml
kubectl delete -f deploy/crd.yaml
# Stop the python file execution
```
