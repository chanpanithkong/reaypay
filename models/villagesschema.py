from ctypes import addressof
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from .villages import tbvillages
from config.db import db

class VillagesSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbvillages
        sqla_session = db.session
        load_instance = True

    villageid = auto_field()
    village = auto_field()
    communeid = auto_field()
    address = auto_field()
    

