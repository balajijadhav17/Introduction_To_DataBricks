import dlt

table_name = spark.conf.get("table_name")

exceptation = {"rule1":"product_id is not null",
               "rule2":"category is not null"}

@dlt.table(
    name = "except_table"
)
@dlt.expect_all(exceptation)
def except_table():
    df = spark.read.table(f"my_first_catalog.silver.{table_name}")
    return df
