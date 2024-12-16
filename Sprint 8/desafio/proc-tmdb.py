import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import col, current_date
from awsglue.dynamicframe import DynamicFrame

glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session

args = getResolvedOptions(sys.argv, ['RAW_PATH', 'TRUSTED_PATH', 'DATABASE_NAME', 'TABLE_NAME'])


raw_path = args['RAW_PATH']
trusted_path = args['TRUSTED_PATH']

dynamic_frame = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [raw_path]},
    format="json"
)

df = dynamic_frame.toDF()

df_cleaned = df.withColumnRenamed("original_title", "title").withColumn("partition_date", current_date())

dynamic_frame_cleaned = DynamicFrame.fromDF(df_cleaned, glueContext, "dynamic_frame_cleaned")
glueContext.write_dynamic_frame.from_options(
    frame=dynamic_frame_cleaned,
    connection_type="s3",
    connection_options={
        "path": trusted_path,
        "partitionKeys": ["partition_date"]
    },
    format="parquet"
)
glueContext.create_dynamic_frame.from_catalog(
    database=args['DATABASE_NAME'],
    table_name=args['TABLE_NAME']
)

print("Processamento de dados TMDB concluído.")
