# IFCO Data Engineering Challenge

This project implements a data processing pipeline for the IFCO challenge, focusing on order processing, sales analysis, and commission calculations using PySpark.

## Project Overview

The project consists of six main tasks that process and analyze sales and order data, with each task building upon the previous ones to create a comprehensive data pipeline.

## Project Structure

```
IFCO/
├── data-engineering-test/          # Main project directory
    ├── resources/                  # Input data files
        ├── invoicing_data.json     # Invoice data
        ├── orders.csv             # Orders data
    ├── source/                    # Source code directory
        ├── outputs/               # Generated output files
        ├── test/                  # Test files
            ├── __init__.py
            ├── test_*.py          # Various test files for each transformation
        ├── transformations/       # Data transformation modules
            ├── __init__.py
            ├── transform_*.py     # Various transformation implementations
        ├── utils.py              # Utility functions
    ├── task_*.py                 # Task implementation files
├── Dockerfile                    # Docker configuration
├── requirements.txt              # Python dependencies
├── run-docker.sh                # Docker execution script
├── run_tests.sh                 # Test execution script
└── setup.py                     # Package setup configuration
```

## Key Components

### Data Transformations
- `transform_orders.py`: Processes raw order data
- `transform_invoicing.py`: Handles invoice data processing
- `transform_commissions_salers.py`: Calculates sales commissions
- `transform_company_salers.py`: Analyzes company-salesperson relationships
- `transform_orders_invoicing.py`: Combines order and invoice data

### Tasks
1. `task_1.py`: Initial data processing and cleaning
2. `task_2.py`: Sales analysis and metrics calculation
3. `task_3.py`: Commission computation
4. `task_4.py`: Company performance analysis
5. `task_5.py`: Advanced sales metrics
6. `task_6.py`: Final reporting and visualization

### Testing
The `test/` directory contains comprehensive unit tests for each transformation:
- `test_transformation_orders.py`
- `test_transformation_invoices.py`
- `test_transformation_commission_salers.py`
- And more...

# IFCO Data Engineering Challenge

[Previous sections remain the same until Setup and Installation]

## Quick Start

The easiest way to run the application is using the provided `run-docker.sh` script:

```bash
# Give execution permissions to the script
chmod +x run-docker.sh

# Run the application
./run-docker.sh
```

This script will:
1. Create necessary directories
2. Build the Docker image if it doesn't exist
3. Run the container with proper volume mounting
4. Execute all tests and tasks
5. Save outputs to your local `data-engineering-test/source/outputs` directory

For Windows users:
```powershell
# Using PowerShell
.\run-docker.sh

# Or using Command Prompt
bash run-docker.sh
```

### Manual Setup

If you prefer to run the commands manually, you can:

```bash
# Build the Docker image
docker build -t ifco-data-engineering .

# Run the container
docker run -v $(pwd)/data-engineering-test/source/outputs:/app/data-engineering-test/source/outputs ifco-data-engineering
```

[Rest of the README remains the same...]

## Script Contents

For reference, here's what the `run-docker.sh` script contains:

```bash
#!/bin/bash

# Create outputs directory if it doesn't exist
mkdir -p data-engineering-test/source/outputs

# Build Docker image
echo "Building Docker image..."
docker build -t ifco-data-engineering .

# Run container with volume mount
echo "Running container..."
docker run -v $(pwd)/data-engineering-test/source/outputs:/app/data-engineering-test/source/outputs ifco-data-engineering

echo "Process completed. Check the outputs directory for results."
```

This script ensures all necessary directories exist and handles the Docker build and run process automatically.

[Rest of the documentation continues...]