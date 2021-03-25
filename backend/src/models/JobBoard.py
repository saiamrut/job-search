"""Database model for Job Board"""
from config import db


class JobBoard(db.Model):
    __tablename__ = "job_boards"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    rating = db.Column(db.String(50), nullable=False, server_default="")
    job_root_id = db.Column(
        db.Integer, db.ForeignKey('job_roots.id'), index=True)
    logo_file = db.Column(db.String(500), nullable=False, server_default="")
    description = db.Column(db.Text, nullable=False, server_default="")

    def __repr__(self):
        return f"JobBoard('{self.name}','{self.rating}','{self.root_domain}', '{self.logo_file}','{self.description}')"
