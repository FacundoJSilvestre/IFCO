from pyspark.sql import DataFrame
from pyspark.sql import functions as F

def transform_commission_salers(df:DataFrame) -> DataFrame:
    """Transform the orders invoicing into the sales owners and their respected commissions.

    Args:
        df (DataFrame): orders invoicing

    Returns:
        DataFrame columns: 
            - sales_owner (string): Sale owner who has orders with invoicing.
            - commission_percentage (float): Commission per order with invoicing.

    """
    # Convert salesowners into an ArrayType column.
    df = df.withColumn("sales_owners", F.split("salesowners", ","))
    # Explode the column into rows of salers_owners and their position in the list.
    df = df.select("grossValue", F.posexplode(df.sales_owners).alias("sales_position", "sales_owner"))
    # Calculate the commissions of the salers.
    df = df.withColumn(
        "commission_percentage",
        F.when(F.col("sales_position") == 0, F.col("grossValue") * 0.060)   # Main Owner: 6%
         .when(F.col("sales_position") == 1, F.col("grossValue") * 0.025)    # Co-owner 1: 2.5%
         .when(F.col("sales_position") == 2, F.col("grossValue") * 0.0095)   # Co-owner 2: 0.95%
         .otherwise(0.0)
    )

    return df.groupBy('sales_owner').agg(F.sum('commission_percentage').alias("commission_percentage")).orderBy("commission_percentage", ascending=False)