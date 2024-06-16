from flask_mail import Message
from app import mail

def send_email(to, subject, template):
    msg = Message(subject, recipients=[to], html=template, sender='your_email@example.com')
    mail.send(msg)