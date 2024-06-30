from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from models import db, User
from flask_login import login_user, logout_user, login_required

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/signup/client', methods=['GET', 'POST'])
def signup_client():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if not email or not password:
            flash('Email and Password are required!', 'danger')
            return redirect(url_for('user_routes.signup_client'))

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email address already exists', 'danger')
            return redirect(url_for('user_routes.signup_client'))

        if password != confirm_password:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('user_routes.signup_client'))

        new_user = User(
            email=email,
            first_name=first_name,
            last_name=last_name,
            role='client',
            password_hash=generate_password_hash(password)
        )

        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        flash('Account created successfully!', 'success')
        return redirect(url_for('user_routes.profile'))

    return render_template('signup_client.html')

@user_routes.route('/signup/worker', methods=['GET', 'POST'])
def signup_worker():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if not email or not password:
            flash('Email and Password are required!', 'danger')
            return redirect(url_for('user_routes.signup_worker'))

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email address already exists', 'danger')
            return redirect(url_for('user_routes.signup_worker'))

        if password != confirm_password:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('user_routes.signup_worker'))

        new_user = User(
            email=email,
            first_name=first_name,
            last_name=last_name,
            role='worker',
            password_hash=generate_password_hash(password)
        )

        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        flash('Account created successfully!', 'success')
        return redirect(url_for('user_routes.profile'))

    return render_template('signup_worker.html')

@user_routes.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@user_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if not user or not user.check_password(password):
            flash('Invalid email or password', 'danger')
            return redirect(url_for('user_routes.login'))

        login_user(user)
        flash('Login successful!', 'success')
        return redirect(url_for('user_routes.profile'))

    return render_template('login.html')

@user_routes.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('user_routes.login'))