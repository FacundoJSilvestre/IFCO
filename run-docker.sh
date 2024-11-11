#!/bin/bash

# Create output folder if not existed
mkdir -p data-engineering-test/source/outputs

# Build docker image
docker build -t my-spark-app .

# Run the docker and obtain the volumens as output
docker run -v $(pwd)/data-engineering-test/source/outputs:/app/data-engineering-test/source/outputs my-spark-app