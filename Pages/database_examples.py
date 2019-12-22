from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('localhost', 27017)
db = client['Book_Store']

collection = db["books"]

# C.R.U.D

# Create
# collection.insert_one({
#     "title": "The Two Towers",
#     "author": "J. R. R. Tolkien",
# })

# find/retrieve
# print( list( collection.find() ))
# print( list( collection.find({"author":"J. R. R. Tolkien"}) ))

# update
# collection.update_one(
#     {"_id": ObjectId("5dff88f8298f0f4320dd4d8f")},
#     {"$set": {"author": "J. R. R. Tolkien"}}
# )

# delete
collection.delete_one({"_id": ObjectId("5dff88af2eac1c29eec4c708")})