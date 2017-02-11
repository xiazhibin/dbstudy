# coding=utf-8

from study_flask_aql import db
from datetime import datetime


class Comments(db.Model):
    comment_id = db.Column(db.BigInteger, primary_key=True)
    bug_id = db.Column(db.BigInteger, db.ForeignKey('bugs.bug_id'))
    author = db.Column(db.BigInteger, db.ForeignKey('accounts.account_id'))
    comment_at = db.Column(db.DateTime, default=datetime.now)
    comment = db.Column(db.Text)
    path = db.Column(db.VARCHAR(1000))


'''
想构建评论树(每个评论可以有自己的爸爸)，
一种做法是添加一个parent_id 来记录 自己的爸爸，这相当于邻接表。坏处是无法查询一个节点的所有后代。删除也是很麻烦，删自己前要看自己有没有爸爸 => 总是依赖父节点

另一种做法是路径枚举,添加一个path(string)，来记录所有的轨迹 例如1/2/5/7，好处是简单，查找也是很快速，问题是维护path比较麻烦，而且也有长度限制

另另外一种做法是闭包表 使用一张 TreePath来记录所有的所有的关系


'''