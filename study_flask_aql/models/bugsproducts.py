from study_flask_aql import db
from datetime import datetime


class BugsProducts(db.Model):
    product_id = db.Column(db.BigInteger, primary_key=True)
    bug_id = db.Column(db.BigInteger, db.ForeignKey('bugs.bug_id'), primary_key=True)
