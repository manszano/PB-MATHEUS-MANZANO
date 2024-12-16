import sys
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

raw_path = sys.argv[1]  
trusted_path = sys.argv[2] 

df = spark.read.csv(raw_path, header=True)

df.write.mode("overwrite").parquet(trusted_path)