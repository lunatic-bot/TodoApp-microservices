# app/routes/notification_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, models, notifications
from app.database import get_db

router = APIRouter(
    prefix="/notifications",
    tags=["notifications"],
)

@router.post("/", response_model=schemas.NotificationResponse)
def create_notification(notification: schemas.NotificationCreate, db: Session = Depends(get_db)):
    """
    Create a new notification for a user.
    """
    new_notification = models.Notification(
        user_id=notification.user_id,
        message=notification.message
    )
    
    db.add(new_notification)
    db.commit()
    db.refresh(new_notification)

    # Optionally, trigger the sending of the notification
    notifications.send_notification(db, new_notification.id)
    
    return new_notification
