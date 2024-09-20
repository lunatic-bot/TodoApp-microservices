# app/schemas.py

from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# Schema for user registration
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# Schema for user login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Schema for user response
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    creation_time: datetime

    class Config:
        orm_mode = True

# Schema for JWT token
class Token(BaseModel):
    access_token: str
    token_type: str
