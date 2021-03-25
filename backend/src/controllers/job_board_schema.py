""" Schema for Job board model"""
from config import ma
from marshmallow import fields
from models.JobBoard import JobBoard


class JobBoardSchema(ma.Schema):
    """Loads fields using Marshmallow schema"""
    id = fields.Int(dump_only=True)
    name = fields.String()
    rating = fields.String()
    root_domain = fields.String()
    logo_file = fields.String()
    description = fields.String()

    class Meta:
        model = JobBoard
        ordered = True
