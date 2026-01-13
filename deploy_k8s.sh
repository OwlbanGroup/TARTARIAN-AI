#!/bin/bash

# Build Docker image
docker build -t tartarian-api:latest .

# Apply Kubernetes manifests
kubectl apply -f k8s/deployment.yml
kubectl apply -f k8s/service.yml
kubectl apply -f k8s/hpa.yml

echo "Tartarian API scaled and deployed to Kubernetes."
