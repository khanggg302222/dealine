# This is the User model definition file used for FastAPI and MongoDB.
from pydantic import BaseModel
class User(BaseModel):
    name: str
    email: str
    age: int


