""" 
    Title: mongodb_test.py
    Author: Isaac Jakubo
    Date: 25 November 2021
    Description: Test the program for connecting to a 
                 MongoDB Atlas cluster
"""

#Importing The Required modules
from pymongo import MongoClient

#Creating the variable containing the MongoDB connection string
url = mongodb+srv://admin:admin@cluster0.bh3s1.mongodb.net/pytech

#Creating variable to connect to MongoDB cluster
client = MongoClient(url)

#Creating variable to for connecting to the Pytech database
db = client.pytech

#Printing the selected collections from the database and then exiting 
print("\n -- Pytech COllection List -- ")
print(db.list_collection_names())
input("\n   End of program, press any key to exit...")
