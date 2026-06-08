from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DataQuality").getOrCreate()

df = spark.read.format("delta").load("/bronze/customer_data")

null_count = df.filter(df.customer_id.isNull()).count()

duplicate_count = df.count() - df.dropDuplicates().count()

print("Null Records:", null_count)
print("Duplicate Records:", duplicate_count)
