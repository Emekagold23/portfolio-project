from models import db
from models import Notification

class NotificationService:
    @staticmethod
    def get_notifications(user_id):
        notifications = Notification.query.filter_by(user_id=user_id).all()
        return [notification.to_dict() for notification in notifications]

    @staticmethod
    def delete_notification(notification_id):
        notification = Notification.query.get(notification_id)
        if notification:
            db.session.delete(notification)
            db.session.commit()
            return True
        return False

    @staticmethod
    def create_notification(data):
        new_notification = Notification(
            user_id=data['user_id'],
            message=data['message'],
            read=data.get('read', False)
        )
        db.session.add(new_notification)
        db.session.commit()
        return new_notification.to_dict()