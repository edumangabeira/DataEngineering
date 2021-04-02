from pyspark.sql import SparkSession


spark = SparkSession \
    .builder \
    .appName("Wrangling Data") \
    .getOrCreate()
path = "data/sparkify_log_small.json"
user_log = spark.read.json(path)


# question 1
user_log.select(["page"]).where(user_log.userId == "").groupby(["page"]).count().collect()

# question 3
user_log.filter(user_log.gender == 'F') \
    .select('userId', 'gender') \
    .dropDuplicates() \
    .count()

# question 4
user_log.filter(user_log.page == 'NextSong') \
    .select('Artist') \
    .groupBy('Artist') \
    .agg({'Artist':'count'}) \
    .withColumnRenamed('count(Artist)', 'Artistcount') \
    .sort(desc('Artistcount')) \
    .show(1)

# question 5
function = udf(lambda ishome : int(ishome == 'Home'), IntegerType())

user_window = Window \
    .partitionBy('userID') \
    .orderBy(desc('ts')) \
    .rangeBetween(Window.unboundedPreceding, 0)

cusum = user_log.filter((user_log.page == 'NextSong') | (user_log.page == 'Home')) \
    .select('userID', 'page', 'ts') \
    .withColumn('homevisit', function(col('page'))) \
    .withColumn('period', Fsum('homevisit').over(user_window))

cusum.filter((cusum.page == 'NextSong')) \
    .groupBy('userID', 'period') \
    .agg({'period':'count'}) \
    .agg({'count(period)':'avg'}).show()