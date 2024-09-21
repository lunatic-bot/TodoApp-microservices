# models.py
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from pytz import timezone
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    creation_time = Column(DateTime, default=datetime.now(timezone("Asia/Kolkata")))

    # Optional: Define a relationship with TodoItem if needed
    # todos = relationship("TodoItem", back_populates="owner")
