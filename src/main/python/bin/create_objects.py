from pyspark.sql import SparkSession

def get_spark_object(env,appName):
    if env == 'Test':
        master = 'local'
    else:
        master = 'yarn'
    spark = SparkSession \
        .builder \
        .master(master) \
        .appName(appName) \
        .getOrCreate()
    return spark