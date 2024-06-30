from flask import Blueprint, render_template, request
from models import User, Profile

search_routes = Blueprint('search_routes', __name__)

@search_routes.route('/search', methods=['GET'])
def search_page():
    return render_template('search.html')

@search_routes.route('/search/results', methods=['GET'])
def search_results():
    skill = request.args.get('skill')
    if not skill:
        return jsonify({'error': 'Please provide a skill to search for'}), 400
    
    workers = User.query.join(Profile).filter(Profile.skills.ilike(f'%{skill}%')).all()
    workers_data = [{
        'id': worker.id,
        'username': worker.username,
        'email': worker.email,
        'skills': worker.profile.skills
    } for worker in workers]
    
    return jsonify(workers_data), 200