# schemas.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TodoBase(BaseModel):
    """Base schema for TodoItem."""
    title: str
    description: str
    completed: bool = False

class TodoCreate(TodoBase):
    """Schema for creating a new todo item."""
    # You can include additional fields here if needed

class TodoUpdate(BaseModel):
    """Schema for updating an existing todo item."""
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class TodoResponse(TodoBase):
    """Schema for todo item response."""
    id: int
    creation_time: datetime
    completion_time: Optional[datetime] = None

    class Config:
        orm_mode = True
