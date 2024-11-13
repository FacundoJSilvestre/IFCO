#!/bin/bash

# Set the scripts fails in case of an error.
set -e

# Work Directory
cd /app/source

# Ejecutar todos los tests
echo "Running tests..."
python -m pytest test/ -v

# Si los tests pasan, ejecutar las tasks en secuencia
if [ $? -eq 0 ]; then
    echo "Tests passed successfully. Running tasks..."
    
    # Execute the task secuencially.
    python task_1.py
    if [ $? -eq 0 ]; then
        python task_2.py
        if [ $? -eq 0 ]; then
            python task_3.py
            if [ $? -eq 0 ]; then
                python task_4.py
                if [ $? -eq 0 ]; then
                    python task_5.py
                fi
            fi
        fi
    fi
else
    echo "Tests failed. Tasks will not be executed."
    exit 1
fi