from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from app import db

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        current_user.first_name = request.form.get('first_name')
        current_user.last_name = request.form.get('last_name')
        current_user.email = request.form.get('email')
        
        db.session.commit()
        flash('Profile updated', 'success')
    
    return render_template('auth/profile.html', user=current_user)






from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from app import db
from app.models import Profile

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        # Update user information
        current_user.username = request.form.get('username')
        current_user.email = request.form.get('email')
        
        # Update profile information
        profile = current_user.profile
        if not profile:
            profile = Profile(user_id=current_user.id)
            db.session.add(profile)
        
        profile.skills = request.form.get('skills')
        profile.experience = request.form.get('experience')
        profile.hourly_rate = request.form.get('hourly_rate')
        profile.availability = request.form.get('availability')
        
        db.session.commit()
        flash('Profile updated', 'success')
        return redirect(url_for('profile.profile'))
    
    return render_template('profile.html', user=current_user)