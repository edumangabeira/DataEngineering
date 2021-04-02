from pyspark.sql import SparkSession
import pandas as pd
import matplotlib
from pyspark.sql.functions import split
from pyspark.sql.functions import udf
from pyspark.sql.types import MapType, StringType
from pyspark.sql.functions import desc
from pyspark.sql.functions import expr

spark = SparkSession.builder.getOrCreate()
dfLog = spark.read.text("data/NASA_access_log_Jul95.gz")

# see the schema
# dfLog.printSchema()

# number of lines
# dfLog.count()

# show
# dfLog.show(5, truncate=False)

# pandas show
# pd.set_option('max_colwidth', 200)
# dfLog.limit(5).toPandas()


########## Simple parsing with split
dfArrays = dfLog.withColumn("tokenized", split("value", " "))
# dfArrays.limit(10).toPandas()


########## Custom parsing UDF
@udf(MapType(StringType(),StringType()))
def parseUDF(line):
    import re
    pattern = '^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+)\s*(\S*)" \d{3} (\S+)'
    match = re.search(pattern, line)
    if match is None:
        return (line, 0)
    size_field = match.group(9)
    if size_field == '-':
        size = 0
    else:
        size = match.group(9)
    return {
        "host"          : match.group(1),
        "client_identd" : match.group(2),
        "user_id"       : match.group(3),
        "date_time"     : match.group(4),
        "method"        : match.group(5),
        "endpoint"      : match.group(6),
        "protocol"      : match.group(7),
        "response_code" : int(match.group(8)),
        "content_size"  : size
    }
dfParsed = dfLog.withColumn("parsed", parseUDF("value"))
# check df
# dfParsed.limit(10).toPandas()


########## Clean df
fields = ["host", "client_identd","user_id", "date_time", "method", "endpoint", "protocol", "response_code", "content_size"]
exprs = [ "parsed['{}'] as {}".format(field,field) for field in fields]
dfClean = dfParsed.selectExpr(*exprs)

# popular hosts
# dfClean.groupBy("host").count().orderBy(desc("count")).limit(10).toPandas()

# popular content
# dfClean.groupBy("endpoint").count().orderBy(desc("count")).limit(10).toPandas()

##########Large Files


dfCleanTyped = dfClean.withColumn("content_size_bytes", expr("cast(content_size  as int)"))

dfCleanTyped.createOrReplaceTempView("cleantypedlog")
spark.sql("""
select endpoint, content_size
from cleantypedlog 
order by content_size_bytes desc
""").limit(10).toPandas()
