from study_flask_aql import db


class Accounts(db.model):
    account_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    account_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    password_hasn = db.Column(db.String(64))
    email = db.Column(db.String(100))
