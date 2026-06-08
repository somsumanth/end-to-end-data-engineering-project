from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SilverLayer").getOrCreate()

df = spark.read.format("delta").load("/bronze/customer_data")

df = df.dropDuplicates()

df = df.na.fill({
    "customer_name": "Unknown"
})

df.write.format("delta") \
    .mode("overwrite") \
    .save("/silver/customer_data")

print("Silver Layer Load Completed")
