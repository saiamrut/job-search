from config import db


class JobRoot(db.Model):
    __tablename__ = "job_roots"

    id = db.Column(db.Integer, primary_key=True)
    root_domain = db.Column(db.String(200), nullable=False, server_default="")
    job_source_id = db.Column(db.Integer, db.ForeignKey('job_sources.id'), index=True)

    def __repr__(self):
        return f"JobRoot('{self.id}','{self.root_domain}','{self.job_source_id}')"