from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import config
import os

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(config_name=None):
    app = Flask(__name__)

    # Set configuration
    config_name = config_name or os.getenv('FLASK_CONFIG', 'default')
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    
    login_manager.login_view = 'auth_bp.login'
    login_manager.login_message_category = 'info'
    
    # Import blueprints
    from routes import user_bp, job_bp, payment_bp, geolocation_bp, notification_bp, admin_bp, review_bp, search_bp, report_bp, error_bp
    from api.auth_api import auth_bp as api_auth_bp
    from api.job_api import job_api as api_job_bp
    from api.payment_api import payment_api as api_payment_bp
    from api.geolocation_api import geolocation_api as api_geolocation_bp
    from api.notification_api import notification_api as api_notification_bp
    from api.admin_api import admin_api as api_admin_bp
    from api.review_api import review_api as api_review_bp
    from api.search_api import search_api as api_search_bp
    from api.booking_api import booking_api as api_booking_bp
    from api.messaging_api import messaging_api as api_messaging_bp

    # Register blueprints
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(job_bp, url_prefix='/jobs')
    app.register_blueprint(payment_bp, url_prefix='/payments')
    app.register_blueprint(geolocation_bp, url_prefix='/geolocation')
    app.register_blueprint(notification_bp, url_prefix='/notifications')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(review_bp, url_prefix='/reviews')
    app.register_blueprint(search_bp, url_prefix='/search')
    app.register_blueprint(report_bp, url_prefix='/reports')
    app.register_blueprint(error_bp, url_prefix='/errors')

    app.register_blueprint(api_auth_bp, url_prefix='/api/user')
    app.register_blueprint(api_job_bp, url_prefix='/api/jobs')
    app.register_blueprint(api_payment_bp, url_prefix='/api/payments')
    app.register_blueprint(api_geolocation_bp, url_prefix='/api/geolocation')
    app.register_blueprint(api_notification_bp, url_prefix='/api/notifications')
    app.register_blueprint(api_admin_bp, url_prefix='/api/admin')
    app.register_blueprint(api_review_bp, url_prefix='/api/reviews')
    app.register_blueprint(api_search_bp, url_prefix='/api/search')
    app.register_blueprint(api_booking_bp, url_prefix='/api/bookings')
    app.register_blueprint(api_messaging_bp, url_prefix='/api/messaging')

    # Register blueprint for authentication
    from utils.auth_utils import auth_bp as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # Import models here to avoid circular import issues
    with app.app_context():
        from models import User, Admin

    # Home route
    @app.route('/')
    def home():
        return render_template('index.html')

    # Error handling routes
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html'), 500

    return app

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    from models import User  # Import User model here to avoid circular import issues
    return User.query.get(int(user_id))

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)