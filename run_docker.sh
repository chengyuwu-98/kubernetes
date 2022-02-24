#!/usr/bin/env bash

# Build image
docker build -t flask-regression:latest .

# List docker images
docker image ls

#Push image to Google Container Registry (GCR) 
docker tag flask-regression gcr.io/fastapi-340818/flask-regression

docker push gcr.io/fastapi-340818/flask-regression


# Push image to Docker Hub

dockerpath="cw4441/linearregression"

echo "Docker ID and Image: $dockerpath"
docker login &&\
    docker image tag flask-regression $dockerpath

docker image push $dockerpath 


# Run flask app
docker run -p 8080:8080 flask-regression

