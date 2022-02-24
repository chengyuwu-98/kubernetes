# Form Linear Regression 
## Introduction 
The web applciatoin lets users to enter some values (x,y) and uses sklearn-LinearRegression to fit the relationship of these observations. Then it will return a formular of the linear regression y=a*x+b and a graph showing the predicted linear relationship. The application also utilizes Containers and Kubernetes, and use Cloud Build to automatically trigger the update of Kubernetes. \
Users can pull the container image from docker hub and run in their local environment or use any methods mentioned in the 'How to run the app' section to access the application.

<img width="468" alt="1645655614" src="https://user-images.githubusercontent.com/76429734/155420569-59eeb38d-3a84-4718-bc69-ebbbd975f8a5.png">

## Demo 
See the Youtobe Demo https://youtu.be/jCdg3o4H7-Q

## How to run the app
1. Directly go to website https://fastapi-340818.uc.r.appspot.com
2. Run in local : `make install` `python main.py`
3. Run in docker: `./run_docker.sh`
4. Pull image from Docker hub : `docker pull cw4441/linearregression`  `docker run -p 8080:8080 cw4441/linearregression`
5. Run in kubernetes with GKE `./run_kubernetes_GKE.sh`
6. Run in kubernetes with Docker hub `./run_kubernetes_hub.sh`

## Tech Used
Flask \
Container \
Docker hub \
Kubernetes \
Google Kubernetes Engine (GKE) \
Google Container Registry (GCK) \
Google Could Build (Countinous Delivery) \
Linear regression 
