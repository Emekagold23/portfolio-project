from models import db
from models import User, Job, Report

class AdminService:
    @staticmethod
    def get_all_users():
        users = User.query.all()
        return [user.to_dict() for user in users]

    @staticmethod
    def get_all_jobs():
        jobs = Job.query.all()
        return [job.to_dict() for job in jobs]

    @staticmethod
    def get_all_reports():
        reports = Report.query.all()
        return [report.to_dict() for report in reports]

    @staticmethod
    def create_report(data):
        new_report = Report(
            user_id=data['user_id'],
            job_id=data.get('job_id'),
            message=data['message'],
            status=data.get('status', 'pending')
        )
        db.session.add(new_report)
        db.session.commit()
        return new_report.to_dict()
