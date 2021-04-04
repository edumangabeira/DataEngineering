from pyspark.sql import SparkSession
import os
import configparser
import pyspark.sql.functions as F
from pyspark.sql.types import StructType  as R
from pyspark.sql.types import StructField as Fld
from pyspark.sql.types import DoubleType  as Dbl
from pyspark.sql.types import StringType  as Str
from pyspark.sql.types import IntegerType as Int
from pyspark.sql.types import FldDateType as Date

config = configparser.ConfigParser()

# Normally this file should be in ~/.aws/credentials
config.read_file(open('aws/credentials.cfg'))


### Create spark session with hadoop-aws package
os.environ["AWS_ACCESS_KEY_ID"]= config['AWS']['AWS_ACCESS_KEY_ID']
os.environ["AWS_SECRET_ACCESS_KEY"]= config['AWS']['AWS_SECRET_ACCESS_KEY']

spark = SparkSession.builder\
                     .config("spark.jars.packages","org.apache.hadoop:hadoop-aws:2.7.0")\
                     .getOrCreate()

df = spark.read.csv("s3a://udacity-dend/pagila/payment/payment.csv")
# df.printSchema()
# df.show(5)


### Infer schema, fix header and separator
df = spark.read.csv("s3a://udacity-dend/pagila/payment/payment.csv",sep=";", inferSchema=True, header=True)
# df.printSchema()
# df.show(5)

### Fix the data
df_payment = df.withColumns("payment_date", F.to_timestamp("payment_date"))
# df_payment.show(5)

### Extract the month
df_payment = df.withColumns("payment_date", F.month("payment_date"))

### Compute aggregate revenue per month
df_payment.createOrReplaceTempView("payment")
spark.sql("""
    SELECT month, sum(amount) as revenue
    FROM payment
    GROUP BY month
    ORDER BY revenue DESC
""").show()

### Fix the schema
payment_schema = R({
    Fld("payment_id", Int()),
    Fld("customer_id", Int()),
    Fld("staff_id", Int()),
    Fld("rental_id", Int()),
    Fld("amount", Dbl()),
    Fld("payment_date", Date()),
})


df_payment_with_schema = spark.read.csv("s3a://udacity-labs/pagila/payment/payment.csv", \
	sep =";", \
	schema = payment_schema, \
	header = True)

# df_payment_with_schema.printSchema()

df_payment_with_schema.createOrReplaceTempView("payment")
spark.sql("""
	SELECT month(payment_date) as m, sum(amount) as revenue
	FROM payment
	GROUP BY m
	ORDER BY revenue DESC
""").show()
