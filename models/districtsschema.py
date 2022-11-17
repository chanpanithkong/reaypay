from ctypes import addressof
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from .districts import tbdistricts
from config.db import db

class DistrictsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbdistricts
        sqla_session = db.session
        load_instance = True

    districtid = auto_field()
    district = auto_field()
    provinceid = auto_field()
    

