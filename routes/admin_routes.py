from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Admin
from flask_login import login_required, current_user

admin_routes = Blueprint('admin_routes', __name__)

@admin_routes.route('/admin', methods=['GET'])
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        flash('You do not have permission to access this page.', 'danger')
        return redirect(url_for('main.index'))
    admins = Admin.query.all()
    return render_template('admin_dashboard.html', admins=admins)

@admin_routes.route('/admin/create', methods=['GET', 'POST'])
@login_required
def create_admin():
    if not current_user.is_admin:
        flash('You do not have permission to access this page.', 'danger')
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        data = request.form
        new_admin = Admin(
            username=data['username'],
            email=data['email']
        )
        new_admin.set_password(data['password'])
        db.session.add(new_admin)
        db.session.commit()
        flash('Admin created successfully!', 'success')
        return redirect(url_for('admin_routes.admin_dashboard'))
    
    return render_template('create_admin.html')

@admin_routes.route('/admin/<int:admin_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_admin(admin_id):
    if not current_user.is_admin:
        flash('You do not have permission to access this page.', 'danger')
        return redirect(url_for('main.index'))
    
    admin = Admin.query.get_or_404(admin_id)
    
    if request.method == 'POST':
        data = request.form
        admin.username = data.get('username', admin.username)
        admin.email = data.get('email', admin.email)
        if 'password' in data and data['password']:
            admin.set_password(data['password'])
        db.session.commit()
        flash('Admin updated successfully!', 'success')
        return redirect(url_for('admin_routes.admin_dashboard'))
    
    return render_template('edit_admin.html', admin=admin)

@admin_routes.route('/admin/<int:admin_id>/delete', methods=['POST'])
@login_required
def delete_admin(admin_id):
    if not current_user.is_admin:
        flash('You do not have permission to access this page.', 'danger')
        return redirect(url_for('main.index'))
    
    admin = Admin.query.get_or_404(admin_id)
    db.session.delete(admin)
    db.session.commit()
    flash('Admin deleted successfully!', 'success')
    return redirect(url_for('admin_routes.admin_dashboard'))

