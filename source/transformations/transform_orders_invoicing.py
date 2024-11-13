from pyspark.sql import DataFrame

def transform_orders_invoices(df_orders: DataFrame, df_invoices:DataFrame) -> DataFrame:
    """Return the join between df_orders & df_invoices with final columns and the desire columns.

    Args:
        df_orders (DataFrame): Orders.
        df_invoices (DataFrame): Invoices.

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
            - invoices_id (string): Unique identifier for the invoice
            - grossValue (float): Gross amount of the invoice converted to monetary units 
            - vat (int): VAT percentage applied
            
    """
    df_final = df_orders.join(df_invoices, df_orders.order_id == df_invoices.orderIdInvoices, how='inner')

    return df_final.select(
        "order_id",
        "date",
        "company_id",
        "company_name",
        "crate_type",
        "contact_full_name",
        "contact_address",
        "salesowners",
        "invoices_id",
        "grossValue",
        "vat"
    )