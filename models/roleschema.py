from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from .roles import tbroles
from config.db import db

class RolesSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbroles
        sqla_session = db.session
        load_instance = True

    roleid = auto_field()
    rolename = auto_field()
    details = auto_field()
    parentid = auto_field()

