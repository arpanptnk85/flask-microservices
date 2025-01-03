# flask-microservices-k8-cluster

Commands for to run the service on darwin/linux
    1. minikube start
    2. eval $(minikube -p minikube docker-env)
    3. kubectl apply -f deploy/deployment.yml
    4. kubectl get services (webapp-service must be present)
    5. kubectl get pods (webapp-....-....)
    6. minikube service webapp-service
