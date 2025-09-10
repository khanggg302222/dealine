# connect to MongoDB
from pymongo import MongoClient
connect_mongo = MongoClient("mongodb://localhost:27017/")
db = connect_mongo["user_db"]
users_collection = db["users"]
