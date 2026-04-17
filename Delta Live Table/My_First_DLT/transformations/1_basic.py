import dlt
from pyspark.sql.functions import *

@dlt.table(name="sales_stg")
def sales_stg():
    return dlt.read_stream("my_first_catalog.silver.sales_enr")


@dlt.table(name="sales_data")
def sales_data():
    df = dlt.read("sales_stg")
    return df.withColumn(
        "priceAfterDiscount",
        col("total_amount") - col("discount")
    )


@dlt.table(name="sales_cur")
def sales_cur():
    return dlt.read("sales_data")
