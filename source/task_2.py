from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import os
from transformations.transform_order import transform_orders

def main():
    # Create spark session for this test.
    spark = SparkSession.builder.appName("task2").getOrCreate()
    # Set the path for reading the file.
    current_path = os.path.abspath(__file__)
    father_path = os.path.dirname(current_path)
    rooth_path = os.path.dirname(father_path)
    csv_path = os.path.join(rooth_path, "data-engineering-test/resources/orders.csv")
    # Read the orders.csv.
    df = spark.read.csv(csv_path, header=True,sep=";", inferSchema=True)
    # Tranform the orders for the desire schema.
    df_final = transform_orders(df)

    # Task 2
    df_final = df_final.select('order_id', 'contact_full_name')
    # Define the route of the output.
    csv_final_path = os.path.join(rooth_path, 'source/outputs/task2.csv')
    # write the dataframe into csv
    df_final.write.mode("overwrite").csv(csv_final_path, header=True)

if __name__ == '__main__':
    main()