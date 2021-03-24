from config import ma
from marshmallow import fields
from models.JobOpportunity import JobOpportunity

class JobOpportunitySchema(ma.Schema):
    # job_opportunities = fields.Nested('JobOpportunitySchema', default=None, many=True)
    id = fields.Int(dump_only=True)
    job_title = fields.String()
    company_name = fields.String()
    root_domain = fields.String()
    job_url = fields.String()
    job_root_id = fields.Int()

    class Meta:
        model = JobOpportunity
        ordered = True