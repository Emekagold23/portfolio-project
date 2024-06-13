from models import db, Message

class MessagingService:
    @staticmethod
    def send_message(data):
        new_message = Message(
            sender_id=data['sender_id'],
            recipient_id=data['recipient_id'],
            content=data['content'],
            timestamp=data.get('timestamp', datetime.utcnow())
        )
        db.session.add(new_message)
        db.session.commit()
        return new_message.to_dict()

    @staticmethod
    def get_message(message_id):
        message = Message.query.get(message_id)
        if message:
            return message.to_dict()
        return None

    @staticmethod
    def get_messages_by_user(user_id):
        messages = Message.query.filter(
            (Message.sender_id == user_id) | (Message.recipient_id == user_id)
        ).all()
        return [message.to_dict() for message in messages]
