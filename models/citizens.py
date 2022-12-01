from config.db import db
from sqlalchemy import or_

class tbcitizens(db.Model):

    cid = db.Column("cid", db.String,primary_key=True)
    firstname = db.Column("firstname", db.String)
    middlename = db.Column("middlename", db.String)
    lastname = db.Column("lastname", db.String) 
    gender = db.Column(db.String)
    dob = db.Column(db.DateTime)
    placeofbirth = db.Column(db.String)
    electioncenter = db.Column(db.String)
    party = db.Column(db.String)
    updatedby = db.Column(db.Integer)
    updateddate = db.Column(db.DateTime)
    joinpartydate = db.Column(db.DateTime)
    position = db.Column(db.String)
    partyposition = db.Column(db.String)
    education = db.Column(db.String)
    nationality = db.Column(db.String)
    partystatus = db.Column(db.String)
    haspartycard = db.Column(db.String)
    provinceid = db.Column(db.String)
    districtid = db.Column(db.String)
    communeid = db.Column(db.String)
    villageid = db.Column(db.String)
    address = db.Column(db.String)
    

    def __init__(self, cid=None, firstname=None, middlename=None, lastname=None, gender = None, dob = None, placeofbirth = None, electioncenter=None, party=None, updatedby=None, updateddate=None, joinpartydate=None, position=None,partyposition=None,education=None,nationality=None,partystatus=None,haspartycard=None, provinceid=None, districtid=None, communeid=None,villageid=None,address=None):
        self.cid = cid
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.gender = gender
        self.dob = dob
        self.placeofbirth = placeofbirth
        self.electioncenter = electioncenter
        self.party = party
        self.updatedby = updatedby
        self.updateddate = updateddate
        self.joinpartydate = joinpartydate
        self.position = position
        self.partyposition = partyposition
        self.education = education
        self.nationality = nationality
        self.partystatus = partystatus
        self.haspartycard = haspartycard
        self.provinceid = provinceid
        self.districtid = districtid
        self.communeid = communeid
        self.villageid = villageid
        self.address = address
        
    @classmethod
    def find_by_cid(cls, cid) -> "tbcitizens":
        return cls.query.filter_by(cid=cid).first()

    @classmethod
    def find_by_fullname(cls, name) -> "tbcitizens":
        return cls.query.filter(or_(db.Column("firstname").contains(name),db.Column("lastname").contains(name)))