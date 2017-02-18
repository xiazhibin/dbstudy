from study_flask_aql import db
from datetime import datetime


class Bugs(db.Model):
    bug_id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    summary = db.Column(db.String(80))
    description = db.Column(db.String(1000))
    resolution = db.Column(db.String(1000))
    reported_by = db.Column(db.BigInteger)
    assigned_to = db.Column(db.BigInteger)
    verified_by = db.Column(db.BigInteger)
    status = db.Column(db.String(20), db.ForeignKey('bug_status.status', onupdate='CASCADE'), default='NEW')
    priority = db.Column(db.String(20))
    hours = db.Column(db.Numeric(9, 2))
