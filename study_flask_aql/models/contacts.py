# coding=utf-8
from study_flask_aql import db


class Contacts(db.Model):
    product_id = db.Column(db.BigInteger, db.ForeignKey('products.product_id'), primary_key=True)
    account_id = db.Column(db.BigInteger, db.ForeignKey('accounts.account_id'), primary_key=True)


'''
    当一个product需要对应多个account的时候，可以在product加个字段，叫做account_ids(string)，以逗号分隔
    坏处，索引用不上，查询性能差，聚合函数用不上，长度（id数量）限制,验证账户id的输入合法性，更新也不方便

    还是老老实实建一个交叉表吧
'''