# This script is used for running the scripts in a pipeline.
# #print(__name__) ## Prints the name of the current module : __main__
import get_all_variables as gav
import create_objects as co
from validations import get_curr_date
import sys
import logging

def main():
    try:
        #Get all the variables including the Envirionment variables
        #print(gav.appName)

        #Get all the Spark objects
        spark = co.get_spark_object(gav.env,gav.appName)
        print("Spark object is created....")
        get_curr_date(spark)
            #Validate the Spark objects
            #Implement logging
            #Implement error handling techniques.

        #Initiate the data ingestion script
            #Load the city file
            #Load the fact file
            #Validate
            #logging
            #Error Handling

        #Data Preprocessing
            #Perform Data Cleaning operation
            #Validate
            #Set up logging
            #Set up error handling

        # Data Transformation steps
            # Do all the necessary tranformation logics
            # Validate
            # Set up logging
            # Set up error handling
    except Exception as e :
        print(e)
        sys.exit(1)

#It is the starting point of the project
if __name__ == "__main__" :
    main()