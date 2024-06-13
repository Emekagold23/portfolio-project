from flask import Blueprint

# Define blueprints
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
from .error_routes import *

# Register routes with blueprints
user_bp.register_blueprint(user_bp, url_prefix='/user')
job_bp.register_blueprint(job_bp, url_prefix='/jobs')
payment_bp.register_blueprint(payment_bp, url_prefix='/payments')
geolocation_bp.register_blueprint(geolocation_bp, url_prefix='/geolocation')
notification_bp.register_blueprint(notification_bp, url_prefix='/notifications')
admin_bp.register_blueprint(admin_bp, url_prefix='/admin')
review_bp.register_blueprint(review_bp, url_prefix='/reviews')
search_bp.register_blueprint(search_bp, url_prefix='/search')
report_bp.register_blueprint(report_bp, url_prefix='/reports')
error_bp.register_blueprint(error_bp, url_prefix='/errors')