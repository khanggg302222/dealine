#output 
# Format MongoDB data to return to client
def format_user(user_raw) -> dict:
    return {
        "id": str(user_raw["_id"]),   
        "name": user_raw["name"],
        "email": user_raw["email"],
        "age": user_raw["age"]
    }
