```
%spark.pyspark
files = sc.textFile("s3://jscaicedomb/datasets/gutenberg-small/*.txt")
wc = files.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
wc.coalesce(1).saveAsTextFile("s3://jscaicedomb/zeppelin/wcout1")
```