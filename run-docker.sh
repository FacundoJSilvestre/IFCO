#!/bin/bash

# Create output folder if not existed
mkdir -p source/outputs

# Build docker image
docker build -t my-spark-app .

# Run the docker and obtain the volumens as output
docker run -v $(pwd)/source/outputs:/app/source/outputs my-spark-app