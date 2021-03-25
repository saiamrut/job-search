"""Datbase model for Job Source"""
from config import db


class JobSource(db.Model):
    __tablename__ = "job_sources"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)

    def __repr__(self):
        return f"JobSource('{self.id}','{self.name}')"
