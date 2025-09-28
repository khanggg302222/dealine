#file access DB
from config import users_collection
from bson import ObjectId

def insert_user(user_data: dict):
    return users_collection.insert_one(user_data)

def get_all_users():
    return users_collection.find()

def update_user_by_id(user_id: str, user_data: dict):
    return users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": user_data}
    )

def delete_user_by_id(user_id: str):
    return users_collection.delete_one({"_id": ObjectId(user_id)})

def get_user_by_id(user_id):
    # check the data and then process it
    if isinstance(user_id, str):
        return users_collection.find_one({"_id": ObjectId(user_id)})
    else:
        return users_collection.find_one({"_id": user_id})

