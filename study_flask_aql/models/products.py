from study_flask_aql import db


class Products(db.Model):
    product_id = db.Column(db.BigInteger, primary_key=True)
    product_name = db.Column(db.VARCHAR(50))
