from flask import Blueprint, render_template, request, redirect, url_for
from models import Job, db

job_routes = Blueprint('job_routes', __name__)

@job_routes.route('/jobs', methods=['GET'])
def jobs_page():
    jobs = Job.query.all()
    return render_template('jobs.html', jobs=jobs)

@job_routes.route('/jobs/<int:job_id>', methods=['GET'])
def job_page(job_id):
    job = Job.query.get_or_404(job_id)
    return render_template('job.html', job=job)

@job_routes.route('/jobs/create', methods=['GET', 'POST'])
def create_job_page():
    if request.method == 'POST':
        data = request.form
        new_job = Job(
            title=data['title'],
            description=data['description'],
            user_id=data['user_id']
        )
        db.session.add(new_job)
        db.session.commit()
        return redirect(url_for('job_routes.jobs_page'))
    return render_template('create_job.html')











from flask import Blueprint, render_template, request, redirect, url_for
from models import Job, db
from forms import JobForm

job_routes = Blueprint('job_routes', __name__)

@job_routes.route('/jobs', methods=['GET'])
def jobs_page():
    jobs = Job.query.all()
    return render_template('jobs.html', jobs=jobs)

@job_routes.route('/jobs/<int:job_id>', methods=['GET'])
def job_page(job_id):
    job = Job.query.get_or_404(job_id)
    return render_template('job.html', job=job)

@job_routes.route('/jobs/create', methods=['GET', 'POST'])
def create_job_page():
    form = JobForm()
    if form.validate_on_submit():
        new_job = Job(
            title=form.title.data,
            description=form.description.data,
            client_id=current_user.id,  # Assuming you use Flask-Login for current_user
            budget=form.budget.data
        )
        db.session.add(new_job)
        db.session.commit()
        return redirect(url_for('job_routes.jobs_page'))
    return render_template('create_job.html', form=form)
