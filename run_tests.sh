#!/bin/bash

# Establecer que el script falle si hay algún error
set -e

# Directorio de trabajo
cd /app/data-engineering-test/source

# Ejecutar todos los tests
echo "Running tests..."
python -m pytest test/ -v

# Si los tests pasan, ejecutar las tasks en secuencia
if [ $? -eq 0 ]; then
    echo "Tests passed successfully. Running tasks..."
    
    # Ejecutar tasks en secuencia
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