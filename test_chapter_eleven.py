from study_flask_aql.models.bugs import Bugs
from study_flask_aql.models.bugstatus import BugStatus
from study_flask_aql import db

# b = Bugs()
# b.assigned_to = 1
# b.description = 'dashabi2'
# b.reported_by = 5
# db.session.add(b)
# db.session.commit()


# b = Bugs.query.filter_by(bug_id=2).first()
# b.status = 'FIXED'
# db.session.commit()

'''
  when bugstatus change, bug.status change too
'''
# bs = BugStatus.query.filter_by(status='NEW').first()
# bs.status = 'NEW2'
# db.session.commit()
