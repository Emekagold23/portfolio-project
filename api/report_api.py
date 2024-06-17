from flask import Blueprint, request, jsonify
from utils.auth_utils import token_required
from services.report_service import ReportService

report_api = Blueprint('report_api', __name__)

@report_api.route('/reports', methods=['POST'])
@token_required
def submit_report(user_id):
    data = request.get_json()
    if not data or 'subject' not in data or 'description' not in data:
        return jsonify({'error': 'Subject and description are required'}), 400
    report = ReportService.submit_report(user_id, data['subject'], data['description'])
    if report:
        return jsonify(report), 201
    return jsonify({'error': 'Report could not be created'}), 500

@report_api.route('/reports/<int:report_id>', methods=['GET'])
@token_required
def get_report(user_id, report_id):
    report = ReportService.get_report(report_id)
    if report:
        return jsonify(report), 200
    return jsonify({'error': 'Report not found'}), 404

@report_api.route('/reports', methods=['GET'])
@token_required
def get_all_reports(user_id):
    reports = ReportService.get_all_reports()
    return jsonify(reports), 200

@report_api.route('/reports/<int:report_id>', methods=['DELETE'])
@token_required
def delete_report(user_id, report_id):
    result = ReportService.delete_report(report_id)
    if result:
        return jsonify({'message': 'Report deleted successfully'}), 200
    return jsonify({'error': 'Report not found'}), 404