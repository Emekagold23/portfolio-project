from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workpal.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    # Register blueprints for HTML routes
    from routes.user_routes import user_routes
    from routes.booking_routes import booking_routes
    from routes.report_routes import report_routes
    from routes.payment_routes import payment_routes
    from routes.notification_routes import notification_routes
    from routes.message_routes import message_routes
    from routes.admin_routes import admin_routes
    from routes.geolocation_routes import geolocation_routes
    from routes.job_routes import job_routes
    from routes.review_routes import review_routes

    app.register_blueprint(user_routes, url_prefix='/user')
    app.register_blueprint(booking_routes, url_prefix='/bookings')
    app.register_blueprint(report_routes, url_prefix='/reports')
    app.register_blueprint(payment_routes, url_prefix='/payments')
    app.register_blueprint(notification_routes, url_prefix='/notifications')
    app.register_blueprint(message_routes, url_prefix='/messages')
    app.register_blueprint(admin_routes, url_prefix='/admin')
    app.register_blueprint(geolocation_routes, url_prefix='/geolocations')
    app.register_blueprint(job_routes, url_prefix='/jobs')
    app.register_blueprint(review_routes, url_prefix='/reviews')

    # Register blueprints for API routes
    from api.auth_api import auth_bp
    from api.job_api import job_bp
    from api.payment_api import payment_bp
    from api.geolocation_api import geolocation_bp
    from api.notification_api import notification_bp
    from api.admin_api import admin_bp
    from api.review_api import review_bp
    from api.search_api import search_bp
    from api.booking_api import booking_bp
    from api.messaging_api import messaging_bp

    app.register_blueprint(auth_bp, url_prefix='/api/user')
    app.register_blueprint(job_bp, url_prefix='/api/jobs')
    app.register_blueprint(payment_bp, url_prefix='/api/payments')
    app.register_blueprint(geolocation_bp, url_prefix='/api/geolocation')
    app.register_blueprint(notification_bp, url_prefix='/api/notifications')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    app.register_blueprint(review_bp, url_prefix='/api/reviews')
    app.register_blueprint(search_bp, url_prefix='/api/search')
    app.register_blueprint(booking_bp, url_prefix='/api/bookings')
    app.register_blueprint(messaging_bp, url_prefix='/api/messaging')

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