# coding=utf-8

from study_flask_aql import db


class TreePaths(db.Model):
    ancestor = db.Column(db.BigInteger, db.ForeignKey('comments.comment_id'), primary_key=True)
    descendant = db.Column(db.BigInteger, db.ForeignKey('comments.comment_id'), primary_key=True)
