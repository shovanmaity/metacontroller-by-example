### Concept

`DecoratorController` contains 2 hooks `sync` and `finalize`.

The `sync` hook is how you specify which children to create/maintain for a given parent – in other words, your desired state. After you return your desired state, Metacontroller begins to take action to converge towards it – creating, deleting, and updating objects as appropriate.

Sync Hook Request
- `controller` - The whole `DecoratorController` cr, like - `kubectl get decoratorcontroller <name> -o json`.
- `parent` - The parent object, like `kubectl get <parent-resource> <parent-name> -o json`.
- `attachments` - An associative array of child objects that already exist.
- `finalizing` - This is always false for the sync hook.

Sync Hook Response
- `labels` - A map of key-value pairs for labels to set on the target object.
- `annotations` - A map of key-value pairs for annotations to set on the target object.
- `status` - A JSON object that will completely replace the status field within the parent object.
- `attachments` - A list of JSON objects representing all the desired children for this parent object.
- `resyncAfterSeconds` - Set the delay (in seconds, as a float) before an optional, one-time, per-object resync.

The `finalize` hook is useful for doing ordered teardown of children. Metacontroller will add a finalizer to the parent object, which will prevent it from being deleted until your hook has had a chance to run and the response indicates that you’re done cleaning up. To perform ordered teardown, you can generate children just like you would for sync, but omit some children from the desired state depending on the observed set of children that are left. For example, if you observe [A,B,C], generate only [A,B] as your desired state; if you observe [A,B], generate only [A]; if you observe [A], return an empty desired list [].

Finalize Hook Request
- `controller` - The whole `DecoratorController` cr, like - `kubectl get decoratorcontroller <name> -o json`.
- `parent` - The parent object, like `kubectl get <parent-resource> <parent-name> -o json`.
- `attachments` - An associative array of child objects that already exist.
- `finalizing` - This is always true for the sync hook.

Finalize Hook Response
- `labels` - A map of key-value pairs for labels to set on the target object.
- `annotations` - A map of key-value pairs for annotations to set on the target object.
- `status` - A JSON object that will completely replace the status field within the parent object.
- `attachments` - A list of JSON objects representing all the desired children for this parent object.
- `resyncAfterSeconds` - Set the delay (in seconds, as a float) before an optional, one-time, per-object resync.
- `finalized` -	A boolean indicating whether you are done finalizing.

### Prerequisite

Make sure metacontroller is [installed](https://github.com/shovanmaity/metacontroller-by-example/tree/master/metacontroller).

Make sure you are inside `decorator-controller/sync-finalize-hook` directory.

Edit the `deploy/controller.yaml` file and update the webhook URL.
```yaml
spec:
  hooks:
    sync:
      webhook:
        url: http://192.168.1.15:8080/sync
    finalize:
      webhook:
        url: http://192.168.1.15:9090/sync
```

Apply the crd and controller.
```bash
kubectl apply -f deploy/crd.yaml
kubectl apply -f deploy/controller.yaml
```

Execute python files
```bash
python3 python/sync.py
python3 python/finalize.py
```

Create a ping cr. Find the sample `Ping` is [here](https://github.com/shovanmaity/metacontroller-by-example/blob/master/decorator-controller/sync-finalize-hook/deploy/ping.yaml).
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

Get the `metadata.finalizers` of the ping cr.
```bash
kubectl get ping -o=jsonpath='{range .items[*]}{@.metadata.finalizers}{"\n"}{end}'
```

Delete the `Ping` cr.
```bash
kubectl delete ping -A --all
```

List `Pong` cr.
```bash
kubectl get ping -A
```

### Cleanup

```bash
kubectl delete -f deploy/controller.yaml
kubectl delete -f deploy/crd.yaml
# Stop the python files execution.
```
