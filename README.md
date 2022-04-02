# Form Linear Regression 
## Introduction 
The web applciatoin lets users to enter some values (x,y) and uses sklearn-LinearRegression to fit the relationship of these observations. Then it will return a formula of the linear regression y=a*x+b and a graph showing the predicted linear relationship. The application also utilizes Containers and Kubernetes, and use Cloud Build to automatically trigger the update of Kubernetes. \
Users can pull the container image from docker hub and run in their local environment or use any methods mentioned in the 'How to run the app' section to access the application.

<img width="468" alt="1645655614" src="https://user-images.githubusercontent.com/76429734/155420569-59eeb38d-3a84-4718-bc69-ebbbd975f8a5.png">

## Demo 
See the Youtube Demo https://youtu.be/jCdg3o4H7-Q

## How to run the app
### directly went to deployed website
1. go to website deployed by google cloud app engine https://fastapi-340818.uc.r.appspot.com 
2. or go to website deployed used kubernetes http://35.223.45.38:8080/

### run the app locally
3. Run in local : `make install` `python main.py`
4. Run in docker: `./run_docker.sh`
5. Pull image from Docker hub : `docker pull cw4441/linearregression`  `docker run -p 8080:8080 cw4441/linearregression`
6. Run in kubernetes with GKE `./run_kubernetes_GKE.sh`
7. Run in kubernetes with Docker hub `./run_kubernetes_hub.sh`

## Tech Used
Flask \
Container \
Docker hub \
Kubernetes \
Google Kubernetes Engine (GKE) \
Google Container Registry (GCK) \
Google Could Build (Countinous Delivery) \
Linear regression 

## Process of building containers and kubernetes
# kubernetes

steps of building kubernetes clusters, deployment, and exposure.

## Building Dockers
`docker build -t flask-regression:latest .`

`docker image ls`

`docker run -p 8080:8080 flask-regression`

push to GCR

`docker tag flask-change gcr.io/fastapi-340818/flask-regression`

`docker push gcr.io/fastapi-340818/flask-regression`
## Building clusters 
step1:
`gcloud config set compute/zone us-central1-a`

step2:
`gcloud container clusters create first`

step3:
`gcloud container clusters get-credentials first`

## Building services
step1:
`kubectl create deployment first-server --image=gcr.io/fastapi-340818/flask-regression`

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
