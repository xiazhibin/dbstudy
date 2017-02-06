from study_flask_aql import db


class Tags(db.Model):
    bug_id = db.Column(db.BigInteger, db.ForeignKey('bugs.bug_id'), primary_key=True)
    tag = db.Column(db.VARCHAR(20), primary_key=True)
