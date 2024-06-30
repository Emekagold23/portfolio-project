from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .job import Job
from .profile import Profile
from .payments import Payment
from .geolocation import Geolocation
from .notification import Notification
from .booking import Booking
from .message import Message
from .review import Review
from .report import Report
from .admin import Admin