from ctypes import addressof
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from .communes import tbcommunes
from config.db import db

class CommunesSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbcommunes
        sqla_session = db.session
        load_instance = True

    communeid = auto_field()
    commune = auto_field()
    distictid = auto_field()
    

