# insure there is only 1 installation of python.
# pip install pymongo
# install mongodb
# run mongodb 
# run script
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create a database named 'mydatabase'
mydb = client["refreshMongodb"]