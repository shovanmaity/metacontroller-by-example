# Learn metacontroller APIs by running them in your local system.

Metacontroller is one way to write a Kubernetes controller in any language. It is a Kubernetes controller administration that runs in cluster scope and manages your controllers. It works like the pub-sub model. For your every controller you need to write a controller spec. Once you apply that spec your controller is subscribed to the metacontroller. According to controller spec, the metacontroller triggers `sync` and `finalize` hooks.

You can write your controller logic in any language. Once you subscribe to metacontroller, it makes POST requests with the current state. Your controller needs to respond with the desired state. The metacontroller server then executes a control loop on behalf of your controller and calls `sync` and `finalize` hook functions whenever necessary.

- [Install metacontroller.](https://github.com/shovanmaity/metacontroller-by-example/tree/master/metacontroller)
- [Create basic controller in different languages and run them locally.](https://github.com/shovanmaity/metacontroller-by-example/tree/master/basic)
- [Create basic controller in different languages and run them in Kubernetes environment.](https://github.com/shovanmaity/metacontroller-by-example/tree/master/basic-k8s)
- [Composite controller](https://github.com/shovanmaity/metacontroller-by-example/tree/master/composite-controller)
  - [Example of sync-finalize-hook.](https://github.com/shovanmaity/metacontroller-by-example/tree/master/composite-controller/sync-finalize-hook)
  - [Example of resync-period.](https://github.com/shovanmaity/metacontroller-by-example/tree/master/composite-controller/resync-period)
  - [Example of generate-selector.](https://github.com/shovanmaity/metacontroller-by-example/tree/master/composite-controller/generate-selector)
  - [Example of spec-selector.](https://github.com/shovanmaity/metacontroller-by-example/tree/master/composite-controller/spec-selector)
  - [Example of target-status.](https://github.com/shovanmaity/metacontroller-by-example/tree/master/composite-controller/target-status)
  - [Example of update-strategy-inplace.](https://github.com/shovanmaity/metacontroller-by-example/tree/master/composite-controller/update-strategy-inplace)
  - [Example of update-strategy-ondelete.](https://github.com/shovanmaity/metacontroller-by-example/tree/master/composite-controller/update-strategy-ondelete)
  - [Example of update-strategy-recreate.](https://github.com/shovanmaity/metacontroller-by-example/tree/master/composite-controller/update-strategy-recreate)
  -  [Example of update-strategy-rolling-recreate.](https://github.com/shovanmaity/metacontroller-by-example/tree/master/composite-controller/update-strategy-rolling-recreate)
  - [Example of update-strategy-rolling-inplace.](https://github.com/shovanmaity/metacontroller-by-example/tree/master/composite-controller/update-strategy-rolling-inplace)
- [Decorator controller](https://github.com/shovanmaity/metacontroller-by-example/tree/master/decorator-controller)
  - [Example of sync-finalize-hook.](https://github.com/shovanmaity/metacontroller-by-example/tree/master/decorator-controller/sync-finalize-hook)
  - [Example of resync-period.](https://github.com/shovanmaity/metacontroller-by-example/tree/master/decorator-controller/resync-period)
  - [Example of target-status.](https://github.com/shovanmaity/metacontroller-by-example/tree/master/decorator-controller/target-status)
  - [Example of target-labels.](https://github.com/shovanmaity/metacontroller-by-example/tree/master/decorator-controller/target-labels)
  - [Example of target-annotations.](https://github.com/shovanmaity/metacontroller-by-example/tree/master/decorator-controller/target-annotations)
  - [Example of annotation-selector.](https://github.com/shovanmaity/metacontroller-by-example/tree/master/decorator-controller/annotation-selector)
  - [Example of label-selector.](https://github.com/shovanmaity/metacontroller-by-example/tree/master/decorator-controller/label-selector)
  - [Example of update-strategy-inplace.](https://github.com/shovanmaity/metacontroller-by-example/tree/master/decorator-controller/update-strategy-inplace)
  - [Example of update-strategy-ondelete.](https://github.com/shovanmaity/metacontroller-by-example/tree/master/decorator-controller/update-strategy-ondelete)
  - [Example of update-strategy-recreate.](https://github.com/shovanmaity/metacontroller-by-example/tree/master/decorator-controller/update-strategy-recreate)
