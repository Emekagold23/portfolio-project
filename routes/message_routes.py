from flask import Blueprint, render_template, request, redirect, url_for
from models import Message, db

message_routes = Blueprint('message_routes', __name__)

@message_routes.route('/messages', methods=['GET'])
def messages_page():
    messages = Message.query.all()
    return render_template('messages.html', messages=messages)

@message_routes.route('/messages/<int:message_id>', methods=['GET'])
def message_page(message_id):
    message = Message.query.get_or_404(message_id)
    return render_template('message.html', message=message)

@message_routes.route('/messages/create', methods=['GET', 'POST'])
def create_message_page():
    if request.method == 'POST':
        data = request.form
        new_message = Message(
            sender_id=data['sender_id'],
            recipient_id=data['recipient_id'],
            content=data['content'],
            timestamp=data.get('timestamp', datetime.utcnow())
        )
        db.session.add(new_message)
        db.session.commit()
        return redirect(url_for('message_routes.messages_page'))
    return render_template('create_message.html')
