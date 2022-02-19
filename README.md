# kubernetes

steps of building kubernetes clusters, deployment, and exposure.

## Building clusters 
step1:
`gcloud config set compute/zone us-central1-a`

step2:
`gcloud container clusters create first`

## Building services
step1:
`kubectl create deployment first-server --image=flask-change:latest`

step2: 
`kubectl expose deployment first-server --type=LoadBalancer --port 8080`

step3:

`kubectl get service`

checking nodes and pods:

`kubectl get nodes`

`kubectl get pods`

describing existing services
`kubectl describe services hello-python-service`

## Delete 
`kubectl delete deployment first-server`
`gcloud container clusters delete first`


