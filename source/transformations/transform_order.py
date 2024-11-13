from pyspark.sql import DataFrame
from pyspark.sql import functions as F
from pyspark.sql import types as T

schema_contact = T.ArrayType(T.StructType([
    T.StructField("contact_name", T.StringType(), True),
    T.StructField("contact_surname", T.StringType(), True),
    T.StructField("city", T.StringType(), True),
    T.StructField("cp", T.StringType(), True)
]))

def transform_orders(df:DataFrame) -> DataFrame:
    """Transform orders Dataframe from read dataframe CSV into a formated one.

    Args:
        df (DataFrame): orders.csv

    Returns:
        DataFrame columns:
            - order_id (string): Unique identifier for the order
            - date (string): Date when the order was created
            - company_id (string): Unique identifier for the company
            - company_name (string): Name of the company
            - crate_type (string): Type of crate used in the order
            - contact_full_name (string): Full name of the contact person (non-null)
            - contact_address (string): Contact's address (non-null)
            - salesowners (string): Sales owner assigned to the order

    """
    #Clean the dataset.
    df = (df
            .withColumn("cleaned_json",F.regexp_replace(F.col("contact_data"),"^['\"]|['\"]$",""))
            .withColumn("cleaned_json", F.regexp_replace(F.col("cleaned_json"),'""','"'))
        )
    # The column cleaned_json it is passed the schema to cast the datatypes.
    df = df.withColumn(
        "parsed_json",
        F.from_json(F.col("cleaned_json"), schema_contact)
    )
    # Explode all the values include the null into new rows from each array.
    df = df.withColumn(
        "exploded_json",
        F.explode_outer(F.col("parsed_json"))
        )
    # Select final columns and create the columns contact_full_name & contact_address.
    df_final = df.select(
        "order_id",
        "date",
        "company_id",
        "company_name",
        "crate_type",
        F.concat(
            F.coalesce(F.col("exploded_json.contact_name"), F.lit("John")),
            F.lit(" "),
            F.coalesce(F.col("exploded_json.contact_surname"), F.lit("Doe"))
        ).alias("contact_full_name"),
        F.concat(
            F.coalesce(F.col("exploded_json.city"), F.lit("Unknown")),
            F.lit(" "),
            F.coalesce(F.col("exploded_json.cp"), F.lit("UNK00")).cast("string")
        ).alias("contact_address"),
        "salesowners"
    )
    return df_final