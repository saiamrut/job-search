import csv
from pathlib import Path
from sqlalchemy import func
from models.JobOpportunity import JobOpportunity
from models.JobRoot import JobRoot
from models.JobSource import JobSource
from collections import defaultdict


def generate_job_source_resolution_data():
    """Generates job source resolution data in csv file"""
    job_opportunities = JobOpportunity.query.all()
    filepath = Path(__file__).parent / "utils" / \
        "job_source_resolution_data.csv"
    fields = ["id", "Job Title", "Company Name", "Job Url", "Job Source"]
    with open(filepath, 'w') as f:
        wtr = csv.writer(f)
        rows = [[jo.id, jo.job_title, jo.company_name, jo.job_url,
                 _get_job_source_name(jo.job_root_id)] for jo in job_opportunities]
        wtr.writerow(fields)
        wtr.writerows(rows)


def generate_job_source_to_job_opportunities_count():
    """Generates job source resolution map"""
    job_sources = JobOpportunity.query.with_entities(JobOpportunity.job_root_id, func.count(
        JobOpportunity.job_root_id)).group_by(JobOpportunity.job_root_id).all()
    sources = defaultdict(int)
    for root_id, count in job_sources:
        name = _get_job_source_name(root_id)
        sources[name] += count
    print(sources)


def _get_job_source_name(job_root_id):
    """Returns job source name for a given job root id"""
    jr = JobRoot.query.filter_by(id=job_root_id).first()
    js = JobSource.query.filter_by(id=jr.job_source_id).first()
    return js.name
