from models import db, User, Location

class GeolocationService:
    @staticmethod
    def update_location(data):
        user_id = data.get('user_id')
        address = data.get('address')
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        user = User.query.get(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        location = Location(
            address=address,
            latitude=latitude,
            longitude=longitude
        )
        db.session.add(location)
        db.session.commit()

        return location.to_dict()
