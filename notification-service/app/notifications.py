# app/notifications.py

from typing import Optional
from datetime import datetime
from sqlalchemy.orm import Session
from app.models import Notification

def send_notification(db: Session, notification_id: int):
    """Simulate sending a notification."""
    notification = db.query(Notification).filter(Notification.id == notification_id).first()

    if notification:
        try:
            # Here you would implement the actual sending logic (e.g., email, SMS)
            print(f"Sending notification to user {notification.user_id}: {notification.message}")
            
            # Update the notification status and sent time
            notification.status = "sent"
            notification.sent_at = datetime.utcnow()
            db.commit()
        except Exception as e:
            notification.status = "failed"
            db.commit()
            print(f"Failed to send notification: {str(e)}")
    else:
        print(f"Notification with ID {notification_id} not found.")
