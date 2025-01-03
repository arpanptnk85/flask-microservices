# Flask Microservices on Kubernetes Cluster

This project demonstrates deploying a simple Flask application as a microservice on a Kubernetes cluster.

## Requirements

* **Python:** Required for application development and Docker image building.
* **Docker:** Used to containerize the Flask application.
* **Kubernetes/Minikube:** Kubernetes is the container orchestration system, and Minikube provides a local Kubernetes cluster for development and testing.
* **Helm:** A package manager for Kubernetes, used to simplify application deployment.

## Running the Application

1. **Start Minikube:**
   ```bash
   minikube start

2. **Set up Docker Environment:**
   ```bash
   eval $(minikube -p minikube docker-env)

3. **Deploy Application:**
   ```bash
   kubectl apply -f deploy/deployment.yml

4. **Verify Deployment:**
   ```bash
   kubectl get services  # Check for the 'webapp-service' 
   kubectl get pods     # Check for pods with 'webapp' in their names

5. **Access the WebApp:**
   ```bash
   minikube service webapp-service
