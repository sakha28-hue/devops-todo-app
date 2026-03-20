 #!/bin/bash

echo "===== Deploying Todo App ====="

IMAGE="sakha1651/todo-app:latest"
CONTAINER="todo-app"

echo "Pulling latest image from Docker Hub..."
docker pull $IMAGE

echo "Stopping old container..."
docker stop $CONTAINER 2>/dev/null
docker rm $CONTAINER 2>/dev/null

echo "Starting new container..."
docker run -d \
  -p 5000:5000 \
  --name $CONTAINER \
  --restart always \
  $IMAGE

echo "===== Deployment Complete ====="
docker ps
