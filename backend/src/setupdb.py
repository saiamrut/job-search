"""Sets up main database"""
from config import db
from models.JobSource import JobSource
from models.JobRoot import JobRoot
from models.JobBoard import JobBoard
from models.JobOpportunity import JobOpportunity
from seedops.populate_db import populate_job_source, populate_job_boards, populate_job_oppportunities


def seed_database():
    """Creates and populates database with given data"""
    db.create_all()
    populate_job_source()
    populate_job_boards()
    populate_job_oppportunities()
    db.session.commit()
