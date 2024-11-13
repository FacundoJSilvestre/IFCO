from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import types as T
from pyspark.sql import functions as F
import json

invoice_schema = T.StructType([
    T.StructField("id", T.StringType(), True),
    T.StructField("orderId", T.StringType(), True),
    T.StructField("companyId", T.StringType(), True),
    T.StructField("grossValue", T.StringType(), True),
    T.StructField("vat", T.StringType(), True)
])

def trasnform_invoices(path:str, spark:SparkSession) -> DataFrame:
    """Read and generate the Invoices Dataframe.

    Args:
        path (str): Path of the invoices JSON.

    Returns:
        DataFrame coluns:
            - id (str): Unique identifier for the invoice
            - orderIdInvoices (str): Associated order identifier
            - companyIdInvoices (str): Company identifier
            - grossValue (float): Gross amount of the invoice converted to monetary units 
            - vat (int): VAT percentage applied
    """
    with open(path, "r") as file:
        data = json.load(file)

    df_invoices = spark.createDataFrame(data['data']['invoices'], schema=invoice_schema)

    return ( df_invoices
            .select(
                F.col("id").alias('invoices_id'),
                F.col("orderId").alias("orderIdInvoices"),
                F.col("companyId").alias("companyIdInvoices"),
                F.round(F.col("grossValue").cast("float")/100, 2).alias("grossValue"),
                F.col("vat").cast('int')
            )
        )
    

