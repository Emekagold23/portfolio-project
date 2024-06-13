from models import db
from models import Report

class ReportService:
    @staticmethod
    def submit_report(user_id, subject, description):
        new_report = Report(user_id=user_id, subject=subject, description=description)
        db.session.add(new_report)
        db.session.commit()
        return new_report.to_dict()

    @staticmethod
    def get_report(report_id):
        report = Report.query.get(report_id)
        if report:
            return report.to_dict()
        return None

    @staticmethod
    def get_all_reports():
        reports = Report.query.all()
        return [report.to_dict() for report in reports]

    @staticmethod
    def delete_report(report_id):
        report = Report.query.get(report_id)
        if report:
            db.session.delete(report)
            db.session.commit()
            return True
        return False
