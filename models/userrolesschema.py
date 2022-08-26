from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from .userroles import tbuserroles
from config.db import db

class UsersRolesSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbuserroles
        sqla_session = db.session
        load_instance = True

    userid = auto_field()
    roleid = auto_field()
    assigneddate = auto_field()
    assignedby = auto_field()
    details = auto_field()

