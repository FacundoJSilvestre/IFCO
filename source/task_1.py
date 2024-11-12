from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import types as T
import os

def main():
    # Create spark session for this test

    current_path = os.getcwd()
    father_path = os.path.dirname(current_path)
    csv_path = os.path.join(father_path, "data-engineering-test/resources/orders.csv")
