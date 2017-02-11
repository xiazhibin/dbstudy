# coding=utf-8
from study_flask_aql import db
from study_flask_aql.models.accounts import Accounts
from study_flask_aql.models.bugs import Bugs
from study_flask_aql.models.comments import Comments
from study_flask_aql.models.treepaths import TreePaths
from sqlalchemy.orm import aliased
from sqlalchemy import or_, func
from sqlalchemy import bindparam
from sqlalchemy.orm import load_only
# Comments_alias = aliased(Comments)
#


# c = Comments.query.filter(or_(bindparam('path', '1/2/').like(Comments.path+'%'), bindparam('path', '1/2/').like('%'))).all() #搜祖先
# c = Comments.query.filter(bindparam('path', '1/2/').like(Comments.path+'%')).all() #搜祖先
# c = Comments.query.join(TreePaths, Comments.comment_id == TreePaths.descendant).filter(TreePaths.ancestor == 2).all() #搜2的后代

# c = Comments.query.join(TreePaths, Comments.comment_id == TreePaths.ancestor).filter(TreePaths.descendant == 9).all() #搜2的祖先
#
# for m in c:
#     print m.comment_id, m.comment

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

# 插入一个评论

from sqlalchemy import select, insert

c = Comments()
c.author = 5
c.comment = u'不客气不客气'
c.bug_id = 1
db.session.add(c)
db.session.flush()

# m = TreePaths.query.options(load_only(['ancestor', c.comment_id])).filter(TreePaths.descendant==5)
#
'''
insert into TreePaths(ancestor, descendant)
  select t.ancestor,c.comment_id
  from TreePaths as t
  where t.descendant=2
union all
  select c.comment_id,c.comment_id
'''
q = db.session.query(TreePaths.ancestor, bindparam('path', c.comment_id)).filter(TreePaths.descendant == 2)
x = q.union_all(select((c.comment_id, c.comment_id)))
ins = insert(TreePaths).from_select([TreePaths.ancestor, TreePaths.descendant], x)

rv = db.session.execute(ins)
print rv.rowcount

# q = TreePaths.query.filter(TreePaths.descendant == 5)
# x = q.union_all(
#     select((c.comment_id, c.comment_id)))
# # m = select([TreePaths.ancestor, c.comment_id]).where(TreePaths.descendant==5).union_all(select((8,8))).as_scalar()
# for m in x.all():
#     print m.descendant

# TreePaths.insert().from_select(['a', 'b'], Comments.select().where(t2.c.y == 5)))
# c2 = Comments.query.filter(Comments.comment_id == 5).first()
# c.path = c2.path + str(c.comment_id) + '/'
#
# db.session.commit()
