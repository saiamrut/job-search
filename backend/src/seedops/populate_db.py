"""Populates database with given sample values"""
import json
import tldextract
import csv
from pathlib import Path
from config import db
from models.JobBoard import JobBoard
from models.JobOpportunity import JobOpportunity
from models.JobSource import JobSource
from models.JobRoot import JobRoot


def populate_job_source():
    """Populates Job Source table with values to be used later"""
    for source in ["Company Website", "Unknown"]:
        js = JobSource(name=source)
        _add_model_to_db(js)


def populate_job_boards():
    """Populates Job Board table with given sample values"""

    # Extract data from JSON file
    fpath = Path(__file__).parent / "job_boards.json"
    with open(fpath) as f:
        data = json.load(f)
    for jb in data["job_boards"]:

        # Add Job Source name to job source table
        js = JobSource(name=jb["name"])
        _add_model_to_db(js)

        # Create job root record
        jr = JobRoot(root_domain=str(jb["root_domain"]), job_source_id=js.id)
        _add_model_to_db(jr)

        # Create job board record using job root id created above
        jobBoard = JobBoard(name=jb["name"], rating=jb["rating"], job_root_id=jr.id,
                            logo_file=jb["logo_file"], description=jb["description"])
        _add_model_to_db(jobBoard)


def populate_job_oppportunities():
    """Populates job opportunities"""

    # Extract job opportunities data from csv file
    fpath = Path(__file__).parent / "job_opportunities.csv"
    with open(fpath, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            id = int(row[0])
            job_title, company_name, job_url = map(str, row[1:])

            # Resolve job root id for each job opportunity
            job_source_resolver(id, job_title, company_name, job_url)


def job_source_resolver(id, job_title, company_name, job_url):
    """ Resolves job source for each job opportunity"""

    root_domain = _get_root_domain(job_url)
    jr = JobRoot.query.filter_by(root_domain=root_domain).first()
    if jr:
        # Job root exists, resolves to job source in known job boards
        resolve_job_to_known_job_source(
            id, job_title, company_name, job_url, jr.id)
    else:
        domain_name = _get_domain_name(job_url)
        if company_name.startswith(domain_name) or domain_name.startswith(company_name):
            # Job url domain matches company name
            resolve_job_to_company_website(
                id, job_title, company_name, job_url, root_domain)
        else:
            # Job url is resolved to Unknown
            resolve_job_to_unknown_source(
                id, job_title, company_name, job_url, root_domain)


def resolve_job_to_known_job_source(id, job_title, company_name, job_url, job_root_id):
    """Resolves job to job from job boards"""
    jo = JobOpportunity(id=id, job_title=job_title, company_name=company_name,
                        job_url=job_url, job_root_id=job_root_id)
    _add_model_to_db(jo)


def resolve_job_to_company_website(id, job_title, company_name, job_url, root_domain):
    """Resolves job to Company Website"""
    js = JobSource.query.filter_by(name="Company Website").first()
    jr = JobRoot(root_domain=root_domain, job_source_id=js.id)
    _add_model_to_db(jr)
    jo = JobOpportunity(id=id, job_title=job_title,
                        company_name=company_name, job_url=job_url, job_root_id=jr.id)
    _add_model_to_db(jo)


def resolve_job_to_unknown_source(id, job_title, company_name, job_url, root_domain):
    """Resolves job to unknown Source"""
    js = JobSource.query.filter_by(name="Unknown").first()
    jr = JobRoot(root_domain=root_domain, job_source_id=js.id)
    _add_model_to_db(jr)
    jo = JobOpportunity(id=id, job_title=job_title,
                        company_name=company_name, job_url=job_url, job_root_id=jr.id)
    _add_model_to_db(jo)


def _get_root_domain(url):
    """Extracts registered domain name from url"""
    ext = tldextract.extract(url)
    return str(ext.registered_domain)


def _get_domain_name(url):
    """Extracts domain name from url"""
    ext = tldextract.extract(url)
    return str(ext.domain)


def _add_model_to_db(model):
    """Add model to database"""
    db.session.add(model)
    db.session.flush()
