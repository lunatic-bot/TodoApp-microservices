# app/schemas.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Schema for creating a notification
class NotificationCreate(BaseModel):
    user_id: int
    message: str

# Schema for notification response
class NotificationResponse(BaseModel):
    id: int
    user_id: int
    message: str
    status: str
    created_at: datetime
    sent_at: Optional[datetime] = None

    class Config:
        orm_mode = True
