from study_flask_aql import db
from datetime import datetime


class Comments(db.Model):
    comment_id = db.Column(db.BigInteger, primary_key=True)
    bug_id = db.Column(db.BigInteger, db.ForeignKey('bugs.bug_id'))
    author = db.Column(db.BigInteger, db.ForeignKey('accounts.account_id'))
    comment_at = db.Column(db.DateTime, default=datetime.now)
    comment = db.Column(db.Text)
