from flask import Blueprint, request, jsonify
from app import db, Admin
from flask_login import login_required, current_user

admin_api = Blueprint('admin_api', __name__)

@admin_api.route('/admins', methods=['GET'])
@login_required
def get_admins():
    if not current_user.is_admin:
        return jsonify({'error': 'Unauthorized access'}), 403
    admins = Admin.query.all()
    return jsonify([admin.to_dict() for admin in admins])

@admin_api.route('/admins', methods=['POST'])
@login_required
def create_admin():
    if not current_user.is_admin:
        return jsonify({'error': 'Unauthorized access'}), 403
    
    data = request.json
    new_admin = Admin(
        username=data['username'],
        email=data['email']
    )
    new_admin.set_password(data['password'])
    db.session.add(new_admin)
    db.session.commit()
    return jsonify(new_admin.to_dict()), 201

@admin_api.route('/admins/<int:admin_id>', methods=['GET'])
@login_required
def get_admin(admin_id):
    if not current_user.is_admin:
        return jsonify({'error': 'Unauthorized access'}), 403
    
    admin = Admin.query.get(admin_id)
    if admin:
        return jsonify(admin.to_dict())
    else:
        return jsonify({'message': 'Admin not found'}), 404

@admin_api.route('/admins/<int:admin_id>', methods=['PUT'])
@login_required
def update_admin(admin_id):
    if not current_user.is_admin:
        return jsonify({'error': 'Unauthorized access'}), 403
    
    admin = Admin.query.get(admin_id)
    if admin:
        data = request.json
        admin.username = data.get('username', admin.username)
        admin.email = data.get('email', admin.email)
        if 'password' in data and data['password']:
            admin.set_password(data['password'])
        db.session.commit()
        return jsonify(admin.to_dict())
    else:
        return jsonify({'message': 'Admin not found'}), 404

@admin_api.route('/admins/<int:admin_id>', methods=['DELETE'])
@login_required
def delete_admin(admin_id):
    if not current_user.is_admin:
        return jsonify({'error': 'Unauthorized access'}), 403
    
    admin = Admin.query.get(admin_id)
    if admin:
        db.session.delete(admin)
        db.session.commit()
        return jsonify({'message': 'Admin deleted'})
    else:
        return jsonify({'message': 'Admin not found'}), 404
