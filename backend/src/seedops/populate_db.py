import json
import tldextract
from pathlib import Path
from config import db
from models.JobBoard import JobBoard
from models.JobOpportunity import JobOpportunity
from models.JobSource import JobSource
from models.JobRoot import JobRoot
import csv

def populate_job_source():
    for source in ["Company Website", "Unknown"]:
        js = JobSource(name=source)
        _add_model_to_db(js)

def populate_job_boards():
    fpath = Path(__file__).parent / "job_boards.json"
    with open(fpath) as f:
        data = json.load(f)
    for jb in data["job_boards"]:
        js = JobSource(name=jb["name"])
        _add_model_to_db(js)
        jr = JobRoot(root_domain=str(jb["root_domain"]), job_source_id=js.id)
        _add_model_to_db(jr)
        jobBoard = JobBoard(name=jb["name"],rating=jb["rating"],job_root_id=jr.id,logo_file=jb["logo_file"], description=jb["description"])
        _add_model_to_db(jobBoard)

def populate_job_oppportunities():
    fpath = Path(__file__).parent / "job_opportunities.csv"
    with open(fpath,'r') as f:
        reader = csv.reader(f)
        normal, cw, unknown  = 0,0,0

        for row in reader:
            id = int(row[0])
            job_title, company_name, job_url = map(str, row[1:])
            root_domain = _get_root_domain(job_url)
            jr = JobRoot.query.filter_by(root_domain=root_domain).first()
            if jr:
                jo = JobOpportunity(id=id, job_title=job_title,company_name=company_name, job_url=job_url, job_root_id=jr.id)
                _add_model_to_db(jo)
                normal+=1
            else:
                domain_name = _get_domain_name(job_url)
                if company_name.startswith(domain_name) or domain_name.startswith(company_name):
                    js = JobSource.query.filter_by(name="Company Website").first()
                    jr = JobRoot(root_domain=root_domain, job_source_id=js.id)
                    _add_model_to_db(jr)
                    jo = JobOpportunity(id=id, job_title=job_title,company_name=company_name, job_url=job_url, job_root_id=jr.id)
                    _add_model_to_db(jo)
                    cw += 1
                else:
                    js = JobSource.query.filter_by(name="Unknown").first()
                    jr = JobRoot(root_domain=root_domain, job_source_id=js.id)
                    _add_model_to_db(jr)
                    jo = JobOpportunity(id=id, job_title=job_title,company_name=company_name, job_url=job_url, job_root_id=jr.id)
                    _add_model_to_db(jo)
                    unknown +=1
        print("normal", str(normal), "unknown", str(unknown), "cw", str(cw))

def _get_root_domain(url):
    ext = tldextract.extract(url)
    return str(ext.registered_domain)

def _get_domain_name(url):
    ext = tldextract.extract(url)
    return str(ext.domain)

def _add_model_to_db(model):
    db.session.add(model)
    db.session.flush()