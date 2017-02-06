from study_flask_aql import db


class Accounts(db.Model):
    account_id = db.Column(db.BigInteger, primary_key=True)
    first_name = db.Column(db.String(20))
    account_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    password_hash = db.Column(db.String(64))
    email = db.Column(db.String(100))
