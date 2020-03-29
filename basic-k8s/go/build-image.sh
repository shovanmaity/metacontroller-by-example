#!/bin/bash
set -ex
rm sample-controller | true

CGO_ENABLED=0 go mod tidy
CGO_ENABLED=0 go build -i -ldflags "-X main.VERSION=$VERSION" -o sample-controller .

docker build -t quay.io/shovanmaity/metacontroller-by-example:go-v1.0 .

rm sample-controller
