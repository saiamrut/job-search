"""Database model for Job Opportunity"""
from config import db


class JobOpportunity(db.Model):
    __tablename__ = "job_opportunities"

    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(250), nullable=False, server_default="")
    company_name = db.Column(db.String(200), nullable=False, server_default="")
    job_url = db.Column(db.String(500), nullable=False, server_default="")
    job_root_id = db.Column(
        db.Integer, db.ForeignKey('job_roots.id'), index=True)

    def __repr__(self):
        return f"JobOpportunity('{self.id}','{self.job_title}','{self.company_name}','{self.job_url}','{self.job_root_id}')"
