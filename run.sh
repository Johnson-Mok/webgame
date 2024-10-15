#!/bin/bash

# Define your container and image name
IMAGE_NAME="streamlit-quiz-app"
CONTAINER_NAME="streamlit-quiz-container"
PORT=8501

# Check if a container with the same name is already running
if [ "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
    echo "Stopping and removing the existing container..."
    docker stop $CONTAINER_NAME
    docker rm $CONTAINER_NAME
else
    echo "No container with the name $CONTAINER_NAME running yet."
fi

# Check if the image exists and remove it if it does
if [[ "$(docker images -q $IMAGE_NAME 2> /dev/null)" != "" ]]; then
    echo "Stop and removing the existing Docker image..."
    docker rmi -f $IMAGE_NAME
fi

# Build the Docker image
echo "Building the Docker image..."
docker build -t $IMAGE_NAME .

# Run the Docker container
echo "Running the Docker container..."
docker run -d -p $PORT:8501 --name $CONTAINER_NAME $IMAGE_NAME

echo "The application is now running at http://localhost:$PORT"