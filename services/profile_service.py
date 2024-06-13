from app.models import db, Profile

class ProfileService:
    @staticmethod
    def update_profile(user, data):
        profile = user.profile
        if not profile:
            profile = Profile(user_id=user.id)
            db.session.add(profile)
        
        profile.skills = data.get('skills')
        profile.experience = data.get('experience')
        profile.hourly_rate = data.get('hourly_rate')
        profile.availability = data.get('availability')
        
        db.session.commit()
        return profile.to_dict()