from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("GoldLayer").getOrCreate()

df = spark.read.format("delta").load("/silver/customer_data")

gold_df = df.groupBy("country") \
            .count()

gold_df.write.format("delta") \
       .mode("overwrite") \
       .save("/gold/customer_summary")

print("Gold Layer Load Completed")
