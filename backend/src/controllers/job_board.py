"""API endpoints for job boards"""
from config import app
from config import db
from models.JobBoard import JobBoard
from controllers.job_board_schema import JobBoardSchema
import flask


@app.route('/jobboards', methods=['GET'])
def get_job_boards():
    """ Returns all job boards"""
    records = JobBoard.query.all()
    schema = JobBoardSchema()
    schema.many = True
    return flask.jsonify(schema.dump(records)), 200
