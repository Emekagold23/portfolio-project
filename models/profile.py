from app import db

class Profile(db.Model):
    __tablename__ = 'profiles'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    skills = db.Column(db.String(255), nullable=False)
    experience = db.Column(db.String(255))
    hourly_rate = db.Column(db.Float)
    availability = db.Column(db.String(255))  # e.g., 'Monday-Friday 9am-5pm'

    user = db.relationship('User', back_populates='profile')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'skills': self.skills,
            'experience': self.experience,
            'hourly_rate': self.hourly_rate,
            'availability': self.availability
        }
    
    def __repr__(self):
        return f'<Profile {self.user_id}>'