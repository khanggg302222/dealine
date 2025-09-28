from fastapi import HTTPException
from model import User
from schema import format_user
import repository

# logic to return for client
def add_user(user: User):
    data = user.dict()
    result = repository.insert_user(data)
    #  # put lại user add from DB = id born
    new_user_raw = repository.get_user_by_id(str(result.inserted_id))
    return format_user(new_user_raw)

def get_users():
    all_users = repository.get_all_users()
    return [format_user(user) for user in all_users]

def update_user(user_id: str, user: User):
    result = repository.update_user_by_id(user_id, user.dict())
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    # put lại verson new befor when update
    updated_user_raw = repository.get_user_by_id(user_id)
    return format_user(updated_user_raw)

def delete_user(user_id: str):
    result = repository.delete_user_by_id(user_id)
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "Deletion successful"}
