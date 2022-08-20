from turtle import st
from flask import Flask
from ..config.db import db

class tbbranches(db.Model):
    
    branchcode = db.Column('branchcode', db.String, primary_key = True)
    branchname = db.Column(db.String(100))
    branchnamekh = db.Column(db.String(255))
    details = db.Column(db.String(255))
    status = db.Column(db.Integer)
    
    def __init__(self, brnachcode = None , branchname = None , branchnamekh = None , details = None, status = None):
        self.branchcode = brnachcode
        self.branchname = branchname
        self.branchnamekh = branchnamekh
        self.details = details
        self.status = status

    @classmethod
    def find_by_branchcode(cls, branchcode) -> "tbbranches":
        return cls.query.filter_by(branchcode=branchcode).first()