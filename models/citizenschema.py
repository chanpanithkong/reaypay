from ctypes import addressof
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from .citizens import tbcitizens
from config.db import db

class CitizensSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbcitizens
        sqla_session = db.session
        load_instance = True

    cid = auto_field()
    firstname = auto_field()
    middlename = auto_field()
    lastname = auto_field()
    gender = auto_field()
    dob = auto_field()
    placeofbirth = auto_field()
    electioncenter = auto_field()
    party = auto_field()
    updatedby = auto_field()
    updateddate = auto_field()
    joinpartydate = auto_field()
    position = auto_field()
    partyposition = auto_field()
    education = auto_field()
    nationality = auto_field()
    partystatus = auto_field()
    haspartycard = auto_field()
    provinceid = auto_field()
    districtid = auto_field()
    communeid = auto_field()
    villageid = auto_field()
    address = auto_field()
    

