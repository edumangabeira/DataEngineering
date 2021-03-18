import pyspark
from pyspark import SparkConf
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Our first Python Spark SQL example") \
    .getOrCreate()

# check change
# spark.sparkContext.getConf().getAll()

# reads
path = "data/sparkify_log_small.json"
user_log = spark.read.json(path)

# show schema
print('Schema: \n')
user_log.printSchema()
print('\n\n')

print('Description: \n')
user_log.describe()
print('\n\n')

# show dataset by tuples
print('Dataset: \n')
user_log.show(n=1)
print('\n\n')

# show records
print('Records: \n')
user_log.take(5)
print('\n\n')


# writes
out_path = "data/sparkify_log_small.csv"
user_log.write.save(out_path, format="csv", header=True)
user_log_2 = spark.read.csv(out_path, header=True)

# show schema
print('Schema: \n')
user_log2.printSchema()
print('\n\n')

# show records
print('Records: \n')
user_log.take(5)
print('\n\n')

# show collumn top rows
print('userID rows: \n')
user_log_2.select("userID").show()
print('\n\n')
