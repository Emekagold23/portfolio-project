from flask import Blueprint, render_template, request, redirect, url_for
from models import Notification, db

notification_routes = Blueprint('notification_routes', __name__)

@notification_routes.route('/notifications', methods=['GET'])
def notifications_page():
    notifications = Notification.query.all()
    return render_template('notifications.html', notifications=notifications)

@notification_routes.route('/notifications/<int:notification_id>', methods=['GET'])
def notification_page(notification_id):
    notification = Notification.query.get_or_404(notification_id)
    return render_template('notification.html', notification=notification)

@notification_routes.route('/notifications/create', methods=['GET', 'POST'])
def create_notification_page():
    if request.method == 'POST':
        data = request.form
        new_notification = Notification(
            user_id=data['user_id'],
            message=data['message'],
            read=data.get('read', False)
        )
        db.session.add(new_notification)
        db.session.commit()
        return redirect(url_for('notification_routes.notifications_page'))
    return render_template('create_notification.html')
