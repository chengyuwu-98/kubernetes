#!/usr/bin/env bash
# This file used for building kubernetes clusters and services for the first time. After running this
# file, kubernetes services will be automatically update with cloudbuild.yaml. 

# Build clusters
gcloud config set compute/zone us-central1-a

gcloud container clusters create regression

gcloud container clusters get-credentials regression

# Build services
kubectl create deployment first-server --image=gcr.io/fastapi-340818/flask-regression

kubectl expose deployment first-server --type=LoadBalancer --port 8080

# Get pods
kubectl get pods

# Run the services
kubectl get service