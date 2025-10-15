from backend.config import users_collection
from bson import ObjectId

def create_user(user_data: dict):
    return users_collection.insert_one(user_data)

def get_users(): 
    users = list(users_collection.find())
    for user in users:
        user["id"] = str(user["_id"])
        del user["_id"]
    return users

def get_user(user_id: str): 
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        user["id"] = str(user["_id"])
        del user["_id"]
    return user

def update_user(user_id: str, user_data: dict):
    return users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": user_data})

def delete_user(user_id: str):
    return users_collection.delete_one({"_id": ObjectId(user_id)})