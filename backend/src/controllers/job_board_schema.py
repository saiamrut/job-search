from config import ma
from marshmallow import fields
from models.JobBoard import JobBoard

class JobBoardSchema(ma.Schema):
    # job_opportunities = fields.Nested('JobOpportunitySchema', default=None, many=True)
    id = fields.Int(dump_only=True)
    name = fields.String()
    rating = fields.String()
    root_domain = fields.String()
    logo_file = fields.String()
    description = fields.String()

    class Meta:
        model = JobBoard
        ordered = True