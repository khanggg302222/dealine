#where the user/application calls API
from fastapi import FastAPI
from model import User
import service


from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Cho phép frontend call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def trang_chu():
    return {"thong_diep": "Chào mừng đến API Quản Lý Người Dùng với MongoDB"}

@app.post("/users")
def create_user(user: User):
    return service.add_user(user)

@app.get("/users")
def read_users():
    return service.get_users()

@app.put("/users/{user_id}")
def update_user(user_id: str, user: User):
    return service.update_user(user_id, user)

@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    return service.delete_user(user_id)
