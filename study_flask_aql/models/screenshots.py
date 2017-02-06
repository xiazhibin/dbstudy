from study_flask_aql import db
from datetime import datetime


class Screenshots(db.Model):
    image_id = db.Column(db.BigInteger, primary_key=True)
    bug_id = db.Column(db.BigInteger, db.ForeignKey('bugs.bug_id'), primary_key=True)
    screenshot_image = db.Column(db.LargeBinary)
    caption = db.Column(db.VARCHAR(100))
