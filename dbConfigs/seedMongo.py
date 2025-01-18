import pymongo
from pymongo import MongoClient
import json

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/') # Replace with your connection string
db = client['refreshMongodb'] # Replace with your database name
collection = db['your_collection_name'] # Replace with your collection name

collection_name = 'your_collection_name'  # Replace with your collection name

# Create the collection if it doesn't exist
if collection_name not in db.list_collection_names():
    db.create_collection(collection_name)

# Sample data
seed_data = [
    {"name": "John Doe", "age": 30, "city": "New York"},
    {"name": "Jane Smith", "age": 25, "city": "Los Angeles"},
    {"name": "Peter Jones", "age": 35, "city": "Chicago"}
]

# Insert data into the collection
collection.insert_many(seed_data)

# Get all documents
documents = collection.find()

# Iterate over the documents and print them
for document in documents:
    print(document)