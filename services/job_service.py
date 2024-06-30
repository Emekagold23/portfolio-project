from models import db, Job

class JobService:

    @staticmethod
    def create_job(data):
        job = Job(**data)
        db.session.add(job)
        db.session.commit()
        return job.to_dict()

    @staticmethod
    def get_job(job_id):
        job = Job.query.get(job_id)
        return job.to_dict() if job else None

    @staticmethod
    def update_job(job_id, data):
        job = Job.query.get(job_id)
        if not job:
            return None
        for key, value in data.items():
            setattr(job, key, value)
        db.session.commit()
        return job.to_dict()

    @staticmethod
    def delete_job(job_id):
        job = Job.query.get(job_id)
        if not job:
            return False
        db.session.delete(job)
        db.session.commit()
        return True

    @staticmethod
    def get_all_jobs():
        jobs = Job.query.all()
        return [job.to_dict() for job in jobs]
