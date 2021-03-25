from config import app
from config import db
from models.JobOpportunity import JobOpportunity
from models.JobBoard import JobBoard
from controllers.job_opportunity_schema import JobOpportunitySchema
from flask import request, jsonify


@app.route('/jobs', methods=['GET'])
def get_jobs():
    """Returns jobs for a given jobBoard ID"""

    # Get job board data to read job root id
    job_board_id = request.args.get('jobBoardId', default=0, type=int)
    jb = JobBoard.query.filter_by(id=job_board_id).first()

    # Filter job opportunities by job root id
    records = JobOpportunity.query.filter_by(job_root_id=jb.job_root_id).all()
    schema = JobOpportunitySchema()
    schema.many = True
    return jsonify(schema.dump(records)), 200
