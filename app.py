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
    # Create an instance of the Flask class with static file settings
    app = Flask(__name__, static_url_path='/static', static_folder='static')

    # Set configuration
    config_name = config_name or os.getenv('FLASK_CONFIG', 'default')
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    
    login_manager.login_view = 'user_routes.login'
    login_manager.login_message_category = 'info'
    
    # Import blueprints and register them
    from routes.user_routes import user_routes
    from routes.job_routes import job_routes
    from routes.payment_routes import payment_routes
    from routes.geolocation_routes import geolocation_bp as geolocation_routes
    from routes.notification_routes import notification_routes
    from routes.admin_routes import admin_routes
    from routes.message_routes import message_routes
    from routes.review_routes import review_routes
    from routes.search_routes import search_routes
    from routes.report_routes import report_routes
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
    app.register_blueprint(user_routes, url_prefix='/user')
    app.register_blueprint(job_routes, url_prefix='/jobs')
    app.register_blueprint(payment_routes, url_prefix='/payments')
    app.register_blueprint(geolocation_routes, url_prefix='/geolocation')
    app.register_blueprint(notification_routes, url_prefix='/notifications')
    app.register_blueprint(admin_routes, url_prefix='/admin')
    app.register_blueprint(message_routes, url_prefix='/messages')
    app.register_blueprint(review_routes, url_prefix='/reviews')
    app.register_blueprint(search_routes, url_prefix='/search')
    app.register_blueprint(report_routes, url_prefix='/reports')

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
        db.create_all()  # Create tables if they don't exist

    # Home route
    @app.route('/')
    def home():
        # Replace 1 with your dynamic booking ID
        booking_id = 1
        return render_template('index.html', booking_id=booking_id)
    
    @app.route('/worker-connection/find')
    def worker_connection_find():
        return render_template('worker_connection_find.html')

    @app.route('/worker-connection/reviews')
    def worker_reviews():
        return render_template('worker_reviews.html')

    @app.route('/worker-connection/profiles')
    def worker_profiles():
        return render_template('worker_profiles.html')

    @app.route('/project-management/planning')
    def project_planning():
        return render_template('project_planning.html')

    @app.route('/project-management/tools-resources')
    def tools_resources():
        return render_template('tools_resources.html')

    @app.route('/project-management/tips')
    def project_tips():
        return render_template('project_tips.html')

    @app.route('/diy-guidance/step-by-step-guides')
    def step_by_step_guides():
        return render_template('step_by_step_guides.html')

    @app.route('/diy-guidance/videos')
    def diy_videos():
        return render_template('diy_videos.html')

    @app.route('/diy-guidance/materials-tools')
    def materials_tools():
        return render_template('materials_tools.html')

    @app.route('/safety-resources/tips')
    def safety_tips():
        return render_template('safety_tips.html')

    @app.route('/safety-resources/emergency-contacts')
    def emergency_contacts():
        return render_template('emergency_contacts.html')
    
    @app.route('/safety-resources/safety_videos')
    def safety_videos():
        return render_template('safety_videos.html')

    @app.route('/safety-resources/equipment')
    def safety_equipment():
        return render_template('safety_equipment.html')

    @app.route('/home-maintenance/tips')
    def maintenance_tips():
        return render_template('maintenance_tips.html')

    @app.route('/home-maintenance/seasonal-checklists')
    def seasonal_checklists():
        return render_template('seasonal_checklists.html')

    @app.route('/home-maintenance/inspections')
    def home_inspections():
        return render_template('home_inspections.html')

    @app.route('/repair-installation/guides')
    def repair_guides():
        return render_template('repair_guides.html')

    @app.route('/repair-installation/tips')
    def installation_tips():
        return render_template('installation_tips.html')

    @app.route('/repair-installation/professional-help')
    def professional_help():
        return render_template('professional_help.html')

    @app.route('/consultation-services/book')
    def book_consultation():
        return render_template('book_consultation.html')

    @app.route('/consultation-services/types')
    def consultation_types():
        return render_template('consultation_types.html')

    @app.route('/consultation-services/profiles')
    def expert_profiles():
        return render_template('expert_profiles.html')

    @app.route('/about-Us')
    def about_us():
        return render_template('About_us.html')

    @app.route('/testimonials')
    def testimonials():
        return render_template('testimonials.html')

    @app.route('/commnity_forums')
    def community_forums():
        return render_template('community_forums.html')
    
    @app.route('/services')
    def services():
        return render_template('services.html')

    @app.route('/signup_worker')
    def signup_worker():
        return render_template('signup_worker.html')

    @app.route('/signup_client')
    def signup_client():
        return render_template('signup_client.html')

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