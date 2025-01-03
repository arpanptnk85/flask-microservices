# flask-microservices-k8-cluster

Commands for to run the service on darwin/linux
    <li>1. minikube start</li>
    <li>2. eval $(minikube -p minikube docker-env)</li>
    <li>3. kubectl apply -f deploy/deployment.yml</li>
    <li>4. kubectl get services (webapp-service must be present)</li>
    <li>5. kubectl get pods (webapp-....-....)</li>
    <li>6. minikube service webapp-service</li>
