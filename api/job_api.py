from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest, NotFound
from utils.auth import token_required
from services.job_service import JobService

job_api = Blueprint('job_api', __name__)

# Create a new job
@job_api.route('/jobs', methods=['POST'])
@token_required
def create_job():
    data = request.get_json()
    if not data:
        raise BadRequest(description='Invalid input data')
    job = JobService.create_job(data)
    return jsonify(job), 201

# Get a job by ID
@job_api.route('/jobs/<int:job_id>', methods=['GET'])
@token_required
def get_job(job_id):
    job = JobService.get_job(job_id)
    if not job:
        raise NotFound(description='Job not found')
    return jsonify(job)

# Update a job by ID
@job_api.route('/jobs/<int:job_id>', methods=['PUT'])
@token_required
def update_job(job_id):
    data = request.get_json()
    if not data:
        raise BadRequest(description='Invalid input data')
    job = JobService.update_job(job_id, data)
    if not job:
        raise NotFound(description='Job not found')
    return jsonify(job)

# Delete a job by ID
@job_api.route('/jobs/<int:job_id>', methods=['DELETE'])
@token_required
def delete_job(job_id):
    success = JobService.delete_job(job_id)
    if not success:
        raise NotFound(description='Job not found')
    return jsonify({'message': 'Job deleted successfully'})

# Get all jobs
@job_api.route('/jobs', methods=['GET'])
@token_required
def get_jobs():
    jobs = JobService.get_all_jobs()
    return jsonify(jobs)
