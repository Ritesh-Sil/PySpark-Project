# To work with environment variables ,  we will use os module
import os

# import pprint as pp
#
# pp.pprint(dict(os.environ))


# Set the environment variables
os.environ['env'] = 'Test'
os.environ['header'] = 'True'
os.environ['inferSchema'] = 'True'

# Get the environment variables
env = os.environ['env']
header = os.environ['header']
inferSchema = os.environ['inferSchema']

# Set the other variables
appName = "USA Prescriber Research Report"
currentPath = os.getcwd()
staging_dim_city = currentPath+'\\staging\\'
staging_fact = currentPath+'\\staging\\'
