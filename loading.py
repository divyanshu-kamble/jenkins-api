import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
import json
import pandas as pd

spark=SparkSession.builder.appName('apidata').getOrCreate()

raw_df = spark.read.json("/Users/dkamble.intern/Documents/jenkins-data/weather.json")
# raw_df.printSchema()
explode_df = raw_df.selectExpr("latitude","longitude","timezone_abbreviation", "hourly.time","hourly.temperature_2m")

explore_df = raw_df.selectExpr("hourly.time", "hourly.temperature_2m")
# explore_df.show()
# exp = explore_df.selectExpr("explode(time) as timezone", "explode(temperature_2m)")
explodedDF = explore_df.withColumn("timestamp", explode('time')).withColumn("temperature", explode('temperature_2m'))
#
mycsv = explodedDF.select('timestamp','temperature')

df = mycsv.toPandas()


df.to_csv("/Users/dkamble.intern/Documents/jenkins-data/csv_file/weather.csv", index=False)