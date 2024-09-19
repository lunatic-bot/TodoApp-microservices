# models.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class TodoItem(Base):
    """Represents a todo item."""
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    completed = Column(Boolean, default=False)
    creation_time = Column(DateTime, default=datetime.utcnow)
    completion_time = Column(DateTime, nullable=True)

    # Define relationship to User model if applicable
    # user_id = Column(Integer, ForeignKey("users.id"))
    # owner = relationship("User", back_populates="todos")
