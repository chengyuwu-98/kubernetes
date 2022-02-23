#!/usr/bin/env bash

dockerpath="cw4441/linearregression"

# Run in Docker Hub container with kubernetes
kubectl run flaskservice\
    --image=$dockerpath\
    --port=80 --labels app=flaskservice

# List kubernetes pods
kubectl get pods

# Forward the container port to host
kubectl port-forward flaskservice 8080:8080