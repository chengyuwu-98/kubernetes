# kubernetes Commands 

steps of building kubernetes clusters, deployment, and exposure.

## Building Dockers
`docker build -t flask-change:latest .`

`docker image ls`

`docker run -p 8080:8080 flask-change`

push to GCR

`docker tag flask-change gcr.io/fastapi-340818/flask-change`

`docker push gcr.io/fastapi-340818/flask-change`
## Building clusters 
step1:
`gcloud config set compute/zone us-central1-a`

step2:
`gcloud container clusters create first`

step3:
`gcloud container clusters get-credentials first`

## Building services
step1:
`kubectl create deployment first-server --image=gcr.io/fastapi-340818/flask-change`

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

`gcloud container clusters delete first --zone=us-central1-a`


