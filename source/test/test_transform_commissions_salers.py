import unittest
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql import types as T
from transformations.transform_order import transform_orders
from transformations.transform_invoicing import trasnform_invoices
from transformations.transform_orders_invoicing import transform_orders_invoices
from transformations.transform_commissions_salers import transform_commission_salers
import os
from chispa.dataframe_comparer import assert_df_equality

class DataFrameTestUtils:
    @staticmethod
    def compare_dataframes(expected_df: DataFrame, actual_df: DataFrame) -> None:
        """
        Compare two PySpark DataFrames for equality.
        
        Args:
            expected_df: The expected DataFrame
            actual_df: The actual DataFrame to compare against the expected one
        """
        # Convert both DataFrames to lists of rows and sort them for comparison
        assert_df_equality(expected_df, actual_df)

class TransformOrdersTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spark = SparkSession.builder.appName("test_transformation_invoicing").getOrCreate()
        # Read test_invoicing_data and create df_invoicing
        cls.file_path = os.path.abspath(__file__)
        cls.father_path = os.path.dirname(cls.file_path)
        cls.json_path = os.path.join(cls.father_path, 'test_invoicing_data.json')
        cls.df_invoicing = trasnform_invoices(cls.json_path, cls.spark)
        # Create df_orders
        cls.data = [
            (
                "f47ac10b-58cc-4372-a567-0e02b2c3d479",  # order_id
                "29.01.22",  # date
                "1e2b47e6-499e-41c6-91d3-09d12dddfbbd",  # company_id
                "Fresh Fruits Co",  # company_name
                "Plastic",  # crate_type
                '[{ "contact_name":"Curtis", "contact_surname":"Jackson", "city":"Chicago", "cp": "12345"}]',  # contact_data
                "Leonard Cohen, Luke Skywalker, Ammy Winehouse" 
            )
        ]
        
        cls.columns = [
            "order_id",
            "date",
            "company_id",
            "company_name",
            "crate_type",
            "contact_data",
            "salesowners"
        ]
        
        # Create DataFrame Orders
        cls.df_orders = cls.spark.createDataFrame(cls.data, schema=cls.columns)
        cls.df_orders = transform_orders(cls.df_orders)
        
        # Create DataFrame
        cls.df = transform_orders_invoices(cls.df_orders, cls.df_invoicing)
        cls.df = transform_commission_salers(cls.df)

        # Create Expected DataFrame
        cls.schema = T.StructType([
            T.StructField("sales_owner", T.StringType(), False),
            T.StructField("commission_percentage", T.DoubleType(), True)
        ])

        cls.df_expected = cls.spark.createDataFrame(
            [
                {"sales_owner":"Leonard Cohen","commission_percentage":194.5332},
                {"sales_owner":" Luke Skywalker","commission_percentage":81.0555},
                {"sales_owner":" Ammy Winehouse","commission_percentage":30.80109}
            ],
            schema=cls.schema
        )

    def test_transform_order(self):
        DataFrameTestUtils.compare_dataframes(self.df_expected, self.df)

if __name__ == '__main__':
    unittest.main()