import unittest
from pyspark.sql import SparkSession
from pyspark.sql import types as T
from ..transformations.transform_orders import transform_orders 
from tests.utils import DataFrameTestUtils

class TransformOrdersTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spark = SparkSession.builder.appName("test_transformation_orders").getOrCreate()
        
        cls.data = [
            (
                "f47ac10b-58cc-4372-a567-0e02b2c3d479",  # order_id
                "29.01.22",  # date
                "1e2b47e6-499e-41c6-91d3-09d12dddfbbd",  # company_id
                "Fresh Fruits Co",  # company_name
                "Plastic",  # crate_type
                '[{ "contact_name":"Curtis", "contact_surname":"Jackson", "city":"Chicago", "cp": "12345"}]',  # contact_data
                "Leonard Cohen, Luke Skywalker, Ammy Winehouse"  # sales_owners
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
        
        # Create DataFrame
        cls.df = cls.spark.createDataFrame(cls.data, schema=cls.columns)
        cls.df = transform_orders(cls.df)
        
        cls.schema = T.StructType([
            T.StructField("order_id", T.StringType(), True),
            T.StructField("date", T.StringType(), True),
            T.StructField("company_id", T.StringType(), True),
            T.StructField("company_name", T.StringType(), True),
            T.StructField("crate_type", T.StringType(), True),
            T.StructField("contact_name", T.StringType(), True),
            T.StructField("contact_surname", T.StringType(), True),
            T.StructField("city", T.StringType(), True),
            T.StructField("cp", T.StringType(), True),
            T.StructField("contact_full_name", T.StringType(), True),
            T.StructField("contact_address", T.StringType(), True),
            T.StructField("salesowners", T.StringType(), True)
        ])
        
        cls.df_expected = cls.spark.createDataFrame(
            [{
                "order_id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
                "date": "29.01.22",
                "company_id": "1e2b47e6-499e-41c6-91d3-09d12dddfbbd",
                "company_name": "Fresh Fruits Co",
                "crate_type": "Plastic",
                "contact_name": "Curtis",
                "contact_surname": "Jackson",
                "city": "Chicago",
                "cp": "12345",
                "contact_full_name": "Curtis Jackson",
                "contact_address": "Chicago 12345",
                "salesowners": "Leonard Cohen, Luke Skywalker, Ammy Winehouse"
            }],
            schema=cls.schema
        )

    def test_transform_order(self):
        DataFrameTestUtils.compare_dataframes(self.df_expected, self.df)

if __name__ == '__main__':
    unittest.main()