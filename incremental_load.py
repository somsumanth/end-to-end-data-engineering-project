from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("IncrementalLoad").getOrCreate()

new_data = spark.read.csv("/landing/new_customer_data.csv", header=True)

new_data.write.format("delta") \
       .mode("append") \
       .save("/bronze/customer_data")

print("Incremental Load Completed")
