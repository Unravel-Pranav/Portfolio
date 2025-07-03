from pydantic import BaseModel, EmailStr
from typing import Optional


# For creating a new user
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    is_admin: Optional[bool] = False


# For returning user details (e.g., after login or fetch)
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_admin: bool

    class Config:
        orm_mode = True


# For login form (only username/email and password)
class UserLogin(BaseModel):
    username: str
    password: str
