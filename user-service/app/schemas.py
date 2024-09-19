# schemas.py
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    creation_time: datetime

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
