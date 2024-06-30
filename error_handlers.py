from flask import Blueprint, jsonify

error_bp = Blueprint('errors', __name__)

@error_bp.app_errorhandler(400)
def bad_request(error):
    response = jsonify({
        'error': 'Bad Request',
        'message': str(error)
    })
    response.status_code = 400
    return response

@error_bp.app_errorhandler(401)
def unauthorized(error):
    response = jsonify({
        'error': 'Unauthorized',
        'message': str(error)
    })
    response.status_code = 401
    return response

@error_bp.app_errorhandler(403)
def forbidden(error):
    response = jsonify({
        'error': 'Forbidden',
        'message': str(error)
    })
    response.status_code = 403
    return response

@error_bp.app_errorhandler(404)
def not_found(error):
    response = jsonify({
        'error': 'Not Found',
        'message': str(error)
    })
    response.status_code = 404
    return response

@error_bp.app_errorhandler(405)
def method_not_allowed(error):
    response = jsonify({
        'error': 'Method Not Allowed',
        'message': str(error)
    })
    response.status_code = 405
    return response

@error_bp.app_errorhandler(500)
def internal_server_error(error):
    response = jsonify({
        'error': 'Internal Server Error',
        'message': str(error)
    })
    response.status_code = 500
    return response

@error_bp.app_errorhandler(Exception)
def handle_exception(error):
    response = jsonify({
        'error': 'Server Error',
        'message': str(error)
    })
    response.status_code = 500
    return response