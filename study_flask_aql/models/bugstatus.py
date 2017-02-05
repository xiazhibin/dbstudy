from study_flask_aql import db


class BugStatus(db.model):
    status = db.Column(db.String(20), primary_key=True)
