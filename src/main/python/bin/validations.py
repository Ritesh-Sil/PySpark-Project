def get_curr_date(spark):
    try:
        opDf = spark.sql(""" select current_date """)
        print("Validating the output : "+str(opD.collect()))


    except Exception as e:
        print("Fix the error : "+str(e))
        # Send errors back to the parent script --> raise
        raise
    else:
        print("Validation Successful...")