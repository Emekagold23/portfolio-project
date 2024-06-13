from models import User
from models import db
import uuid
from datetime import datetime, timedelta

class AuthService:
    @staticmethod
    def request_password_reset(email):
        # Logic to generate a password reset token and send it via email
        user = User.query.filter_by(email=email).first()
        if user:
            token = str(uuid.uuid4())
            # Store token in a database or send via email
            print(f'Password reset token for {email}: {token}')

    @staticmethod
    def reset_password(token, new_password):
        # Logic to reset the password using the token
        # This example assumes the token is stored and associated with a user
        user = User.verify_reset_token(token)
        if user:
            user.password_hash = new_password  # Assume hashing happens here
            db.session.commit()
            print(f'Password reset for user: {user.email}')

    @staticmethod
    def verify_account(token):
        # Logic to verify the account using the token
        user = User.verify_verification_token(token)
        if user:
            user.is_verified = True
            db.session.commit()
            print(f'Account verified for user: {user.email}')




from models.user import User
from app import db

class AuthService:
    @staticmethod
    def register_user(username, email, password):
        if User.query.filter_by(email=email).first() is not None:
            return None
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
    @staticmethod
    def authenticate_user(email, password):
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            return user
        return None



from models.user import User
from app import db

class AuthService:
    @staticmethod
    def register_user(first_name, last_name, email, password, role):
        if User.query.filter_by(email=email).first() is not None:
            return None
        new_user = User(first_name=first_name, last_name=last_name, email=email, role=role)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
    @staticmethod
    def authenticate_user(email, password):
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            return user
        return None




# app/services/auth_service.py
from models.user import User
from app import db

class AuthService:
    @staticmethod
    def register_user(first_name, last_name, email, password, role):
        if User.query.filter_by(email=email).first() is not None:
            return None
        new_user = User(first_name=first_name, last_name=last_name, email=email, role=role)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
    @staticmethod
    def authenticate_user(email, password):
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            return user
        return None
