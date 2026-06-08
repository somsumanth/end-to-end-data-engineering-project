from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("BronzeLayer").getOrCreate()

df = spark.read.csv(
    "/raw/customer_data.csv",
    header=True,
    inferSchema=True
)

df.write.format("delta") \
    .mode("overwrite") \
    .save("/bronze/customer_data")

print("Bronze Layer Load Completed")
