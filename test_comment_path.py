# coding=utf-8
from study_flask_aql import db
from study_flask_aql.models.accounts import Accounts
from study_flask_aql.models.bugs import Bugs
from study_flask_aql.models.comments import Comments
from sqlalchemy.orm import aliased
from sqlalchemy import or_, func
from sqlalchemy import bindparam

# Comments_alias = aliased(Comments)
#


# c = Comments.query.filter(or_(bindparam('path', '1/2/').like(Comments.path+'%'), bindparam('path', '1/2/').like('%'))).all() #搜祖先
# c = Comments.query.filter(bindparam('path', '1/2/').like(Comments.path+'%')).all() #搜祖先
# c = Comments.query.filter(Comments.path.like('1/2/'+'%')).all() #搜儿子

# query = db.session.query(Comments, func.count('*'))
# query = query.filter(
#     Comments.path.like('1/2/' + '%')
# )
# query = query.group_by(Comments.author).group_by(Comments.comment_id)
# c = query.all()
# c = Comments.query.filter(Comments.path.like('1/2/'+'%')).group_by(Comments.author).group_by(Comments.comment_id)
# print c
# c = db.session.query(func.count('*')).filter(Comments.path.like('1/2/'+'%')).group_by(Comments.author)
#
# print type(c)
# print dir(c)
# print '--------------'
# for m in c:
#     print type(m)
#
#
#     # nodealias = aliased(Node)
#     # SQLsession.query(Node).filter(Node.data=='subchild1').\
#     #                 join(nodealias, Node.parent).\
#     #                 filter(nodealias.data=="child2").\
#     #                 all()

# c = Comments()
# c.author = 3
# c.comment = 'fuxk you'
# c.bug_id = 1
# db.session.add(c)
# db.session.commit()
#
# c2 = Comments.query.filter(Comments.comment_id == 5).first()
# c.path = c2.path + str(c.comment_id) + '/'
#
# db.session.commit()

c = Comments.query.filter(Comments.path.like('1/2/%')).filter(
    or_(Comments.author == 1, Comments.author == 5)).order_by(Comments.comment_at).all()

for m in c:
    print m.author, m.comment