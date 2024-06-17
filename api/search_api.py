from flask import Blueprint, request, jsonify
from utils.auth_utils import token_required
from services.search_service import SearchService

search_api = Blueprint('search_api', __name__)

@search_api.route('/search', methods=['GET'])
@token_required
def search(user_id):
    query = request.args.get('query', '')
    results = SearchService.search(query)
    return jsonify(results), 200