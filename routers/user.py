from fastapi import APIRouter, Response
from pydantic import BaseModel

# Create an instance with a different name than the class
router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.get("/")
def get_user():
    # Dummy function to simulate user retrieval
    return {"username": "johndoe"}

@router.get("/{user_id}")
def get_user_by_id(user_id: int):
    # Dummy function to simulate user retrieval by ID
    return {"user_id": user_id, "username": "johndoe"}

class User(BaseModel):
    firstname: str
    lastname: str
    email: str
    

@router.post("/")
def create_user(response: Response, user: User):
    # Dummy function to simulate user creation
    response.set_cookie(key="user", value=user.email)
    return {"message": "User created successfully", "user": user}