from ctypes import addressof
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from .disticts import tbdisticts
from config.db import db

class DistictsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbdisticts
        sqla_session = db.session
        load_instance = True

    distictid = auto_field()
    distict = auto_field()
    provinceid = auto_field()
    

