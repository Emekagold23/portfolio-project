from app import db
from models import User

class UserService:
    
    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def create_user(first_name, last_name, email, password, role):
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            role=role
        )
        new_user.set_password(password)  # Use the set_password method to hash the password
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def update_user(user, **kwargs):
        for key, value in kwargs.items():
            setattr(user, key, value)
        db.session.commit()
        return user

    @staticmethod
    def delete_user(user):
        db.session.delete(user)
        db.session.commit()
