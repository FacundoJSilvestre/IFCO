from pyspark.sql import DataFrame
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