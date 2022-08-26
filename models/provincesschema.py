from ctypes import addressof
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from .provinces import tbprovinces
from config.db import db

class ProvincesSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbprovinces
        sqla_session = db.session
        load_instance = True

    provinceid = auto_field()
    province = auto_field()
    details = auto_field()
    

