from flask import Blueprint, render_template, request, redirect, url_for
from app import Report, db

report_routes = Blueprint('report_routes', __name__)

@report_routes.route('/reports', methods=['GET'])
def reports_page():
    reports = Report.query.all()
    return render_template('reports.html', reports=reports)

@report_routes.route('/reports/<int:report_id>', methods=['GET'])
def report_page(report_id):
    report = Report.query.get_or_404(report_id)
    return render_template('report.html', report=report)

@report_routes.route('/reports/create', methods=['GET', 'POST'])
def create_report_page():
    if request.method == 'POST':
        data = request.form
        new_report = Report(
            user_id=data['user_id'],
            subject=data['subject'],
            description=data['description']
        )
        db.session.add(new_report)
        db.session.commit()
        return redirect(url_for('report_routes.reports_page'))
    return render_template('create_report.html')

