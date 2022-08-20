from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from ..models.wsusers import tbwsusers
from ..config.db import db

class WsUserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbwsusers
        sqla_session = db.session
        load_instance = True

    wsuserid = auto_field()
    email= auto_field()
    password = auto_field()

