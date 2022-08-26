from ctypes import addressof
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from .parties import tbparties
from config.db import db

class PartiesSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbparties
        sqla_session = db.session
        load_instance = True

    partyid = auto_field()
    party = auto_field()
    photo = auto_field()
    details = auto_field()
    

