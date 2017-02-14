from study_flask_aql.models.accounts import Accounts
from study_flask_aql import db

ac = Accounts.query.filter(Accounts.account_id == 1).first()

ac.hourly_rate = 78.908
db.session.commit()

print ac.hourly_rate  # 78.91
