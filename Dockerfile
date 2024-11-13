# Python Image
FROM python:3.9-slim-buster

# Install Java and required system packages
RUN apt-get update --fix-missing && \
    apt-get install -y --no-install-recommends \
    openjdk-11-jre-headless \
    build-essential \
    curl \
    libssl-dev \
    libffi-dev \
    libjpeg-dev \
    zlib1g-dev \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create the folder outputs if not exists
RUN mkdir -p /app/source/outputs

# Copy all the files
COPY . .

# Install local package in development mode
RUN pip install -e .

# Config PYTHONPATH 
ENV PYTHONPATH="/app/source:${PYTHONPATH}"

# Give permissions to run the script
RUN chmod +x run_tests.sh

# Config the variable
ENV MPLBACKEND=Agg

# Volume for checking output results
VOLUME ["/app/source/outputs"]

# Run the Tests and the Tasks
CMD ["./run_tests.sh"]
