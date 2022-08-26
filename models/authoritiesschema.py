from ctypes import addressof
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from .authorities import tbauthorities
from config.db import db

class AuthoritiesSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbauthorities
        sqla_session = db.session
        load_instance = True

    userid = auto_field()
    username = auto_field()
    userpassword = auto_field()
    gender = auto_field()
    dob = auto_field()
    address = auto_field()
    photo = auto_field()
    

