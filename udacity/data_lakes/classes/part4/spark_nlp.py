# !pip install spark-nlp==1.7.3
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from com.johnsnowlabs.nlp.pretrained.pipeline.en import BasicPipeline as bp
from pyspark.sql.functions import desc


pd.set_option('max_colwidth', 800)

### Create a spark context that includes a 3rd party jar for NLP
spark = SparkSession.builder \
    .config("spark.jars.packages", "JohnSnowLabs:spark-nlp:1.8.2") \
    .getOrCreate()

### Read multiple files in a dir as one Dataframe
dataPath = "./*.json"
df = spark.read.json(dataPath)
# print(df.count())
# df.printSchema()


### Deal with Struct type to query subfields
title = "data.title"
author = "data.author"

df_author_title = df.select(author, title)
# df_author_title.limit(10).toPandas().style.hide_index()

### Implements the equivalent of flatMap in dataframes
df_word_count = df.select(F.explode(F.split(title,"\\s+")).alias("word")).groupBy("word").count().orderBy(F.desc("count"))
# dfWordCount.limit(10).toPandas()

### Use an NLP libary to do Part-of-Speech Tagging
df_annotated = bp.annotate(df_author_title, "title")
# df_annotated.printSchema()

### Deal with Map type to query subfields
# df_POS = df_annotated.select("text", "pos.metadata", "pos.result")
df_POS = df_annotated.select(F.explode("pos").alias("pos"))
# df_POS.limit(10).toPandas()

### Keep only proper nouns NNP or NNPS
nnp_filter = "pos.result = 'NNP' or pos.result = 'NNPS' "
df_NNP = df_POS.where(nnp_filter)

### Extract columns form a map in a col
df_word_tag = df_NNP.selectExpr("pos.metadata['word'] as word", "pos.result as tag")
# df_word_tag.limit(10).toPandas()
df_word_tag.groupBy("word").count().orderBy(desc("count")).show()