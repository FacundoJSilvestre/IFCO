from pyspark.sql import SparkSession
import os
from transformations.transform_order import transform_orders
from transformations.transform_invoicing import trasnform_invoices
from transformations.transform_orders_invoicing import transform_orders_invoices
from transformations.transform_company_salers import transformation_company_sales

def main():
    # Create spark session for this test.
    spark = SparkSession.builder.appName("task5").getOrCreate()
    # Set the path for reading the file.
    current_path = os.path.abspath(__file__)
    father_path = os.path.dirname(current_path)
    rooth_path = os.path.dirname(father_path)
    csv_path = os.path.join(rooth_path, "data-engineering-test/resources/orders.csv")
    # Read the orders.csv.
    df = spark.read.csv(csv_path, header=True,sep=";", inferSchema=True)
    # Tranform the orders for the desire schema.
    df_orders = transform_orders(df)

    # Read the json invoicing.
    json_path = os.path.join(rooth_path, "data-engineering-test/resources/invoicing_data.json")
    df_invoicing = trasnform_invoices(json_path, spark)

    # Join orders and invoicing
    df = transform_orders_invoices(df_orders, df_invoicing)
    # Task 
    df_final = transformation_company_sales(df)
    # Define the route of the output.
    csv_final_path = os.path.join(rooth_path, 'source/outputs/task5.csv')
    # write the dataframe into csv
    df_final.write.mode("overwrite").csv(csv_final_path, header=True)

if __name__ == '__main__':
    main()