from flask import Blueprint

# Initialize the blueprints
user_bp = Blueprint('user', __name__)
job_bp = Blueprint('job', __name__)
payment_bp = Blueprint('payment', __name__)
geolocation_bp = Blueprint('geolocation', __name__)
notification_bp = Blueprint('notification', __name__)
admin_bp = Blueprint('admin', __name__)
review_bp = Blueprint('review', __name__)
search_bp = Blueprint('search', __name__)
report_bp = Blueprint('report', __name__)
error_bp = Blueprint('error', __name__)

# Import and register routes
from .user_routes import *
from .job_routes import *
from .payment_routes import *
from .geolocation_routes import *
from .notification_routes import *
from .admin_routes import *
from .review_routes import *
from .search_routes import *
from .report_routes import *