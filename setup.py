from setuptools import setup, find_packages
import os

# Obtener la ruta absoluta del directorio actual
here = os.path.abspath(os.path.dirname(__file__))

setup(
    name="data-engineering-test",
    version="0.1",
    package_dir={"": "source"},
    packages=find_packages(where="source"),
    include_package_data=True,
    install_requires=[
        "pyspark>=3.5.3",
        "pandas>=2.1.1",
        "numpy>=1.26.0",
        "seaborn>=0.13.2",
        "pytest>=7.4.0",
        "pytest-cov>=4.1.0"
    ],
    python_requires=">=3.9",
    # Agregar el directorio source y sus archivos
    package_data={
        "": ["*.json", "*.csv", "*.py"],
    }
)