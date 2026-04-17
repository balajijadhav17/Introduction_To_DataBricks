import dlt
from pyspark.sql.functions import * 

# CREATE A STREAMING VIEW
@dlt.table(
    name = "autovolume_table"
)

def autovolume_table():
    df = spark.readStream.format("cloudFiles")\
        .option("cloudFiles.format","csv")\
        .load("/Volumes/my_first_catalog/bronze/autoloader_volume/raw/")
    return df

# CREATE A STREAMING VIEW

@dlt.table(
    name = "autovolume_table_enr"
)

def autovolume_table_enr():
    df=spark.read.table("autovolume_table")
    df=df.withColumn("flag",lit("Yes"))

    return df












