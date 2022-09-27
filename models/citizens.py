from sqlite3 import paramstyle
from config.db import db

class tbcitizens(db.Model):

    cid = db.Column("cid", db.String,primary_key=True)
    firstname = db.Column("firstname", db.String)
    middlename = db.Column("middlename", db.String)
    lastname = db.Column("lastname", db.String) 
    gender = db.Column(db.String)
    dob = db.Column(db.DateTime)
    placeofbirth = db.Column(db.String)
    address = db.Column(db.String)
    electioncenter = db.Column(db.String)
    party = db.Column(db.String)
    updatedby = db.Column(db.Integer)
    updateddate = db.Column(db.DateTime)


    def __init__(self, cid=None, firstname=None, middlename=None, lastname=None, gender = None, dob = None, placeofbirth = None, address=None, electioncenter=None, party=None, updatedby=None, updateddate=None):
        self.cid = cid
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.gender = gender
        self.dob = dob
        self.placeofbirth = placeofbirth
        self.address = address
        self.electioncenter = electioncenter
        self.party = party
        self.updatedby = updatedby
        self.updateddate = updateddate

    @classmethod
    def find_by_cid(cls, cid) -> "tbcitizens":
        return cls.query.filter_by(cid=cid).first()