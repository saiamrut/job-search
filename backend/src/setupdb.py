import json
from pathlib import Path
from config import db
from models.JobSource import JobSource
from models.JobRoot import JobRoot
from models.JobBoard import JobBoard
from models.JobOpportunity import JobOpportunity

import csv
from seedops.populate_db import populate_job_source, populate_job_boards, populate_job_oppportunities

# db.create_all()
# populate_job_source()
# populate_job_boards()
# populate_job_oppportunities()
# db.session.commit()
