import dlt

dlt.create_streaming_table(
    name = "append_table"
)

@dlt.append_flow(
    target = "append_table"
)
def flow1():
    df = spark.readStream.format("cloudFiles")\
        .option("cloudFiles.format", "csv")\
        .load("/Volumes/my_first_catalog/bronze/autoloader_volume/flow1/")

    return df

@dlt.append_flow(
    target = "append_table"
)
def flow2():
    df = spark.readStream.format("cloudFiles")\
        .option("cloudFiles.format", "csv")\
        .load("/Volumes/my_first_catalog/bronze/autoloader_volume/flow2/")

    return df


    