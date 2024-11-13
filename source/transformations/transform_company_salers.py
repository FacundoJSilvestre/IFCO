from pyspark.sql import DataFrame
from pyspark.sql import functions as F

def transformation_company_sales(df:DataFrame) -> DataFrame:
    """Transform the orders invoicing into the company and their sales owners.

    Args:
        df (DataFrame): orders invoicing

    Returns:
        DataFrame columns: 
            - company_id (string): Unique identifier for the company
            - company_name (string): Name of the company
            - sales_owners (array): Sales owner assigned to the order.
    """
    # Convert salesowners into an ArrayType column.
    df = df.withColumn("sales_owners", F.split("salesowners", ","))
    # Explode the column sales_owners for each individual value.
    df = df.withColumn("sales_owners", F.explode("sales_owners"))
    # Select a list of words that we have to remove
    words_to_remove = ["co", "ltd", "inc", "gmbh", "sa"]
    words_regex = "|".join([r"\b" + word + r"\b" for word in words_to_remove])

    # Remove non-letter characters except spaces
    df = df.withColumn("company_name", F.regexp_replace(F.lower(F.col("company_name")), r"[^A-Za-z\s]", ""))

    # Remove specified words and trim any extra spaces that might remain
    df = df.withColumn("company_name", F.regexp_replace(F.col("company_name"), words_regex, ""))
    df = df.withColumn("company_name", F.trim(F.col("company_name")))
    # Group by company_name 'cause so company_id are duplicated and agg on a list of sales_owners.
    df = df.groupBy( "company_name").agg(F.collect_list("sales_owners").alias("sales_owners"))
    
    df = df.withColumn("salers", F.concat_ws(", ", F.col("sales_owners")))

    return df.select("company_name", "salers")