import dlt
from pyspark.sql.functions import *

@dlt.table(
    name = "scd_stg"
)

def scd1_stg():
    df = spark.readStream.table("my_first_catalog.bronze.source")
    return df

dlt.create_streaming_table(
    name = "scd1_table"
)

dlt.create_auto_cdc_flow(
    source= "scd_stg",
    target = "scd1_table",
    keys= ["product_id"],
    sequence_by=col("process_date"),
    stored_as_scd_type = 1


)


dlt.create_streaming_table(
    name = "scd3_table"
)

dlt.create_auto_cdc_flow(
    source= "scd_stg",
    target = "scd3_table",
    keys= ["product_id"],
    sequence_by=col("process_date"),
    stored_as_scd_type = 2,
    except_column_list=["process_date"]


)