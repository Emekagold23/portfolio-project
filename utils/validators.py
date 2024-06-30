from wtforms.validators import ValidationError
from models import User

def email_not_registered(form, field):
    if User.query.filter_by(email=field.data).first():
        raise ValidationError('Email is already registered.')