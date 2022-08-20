from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from ..models.branches import tbbranches
from ..config.db import db

class BranchSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbbranches
        sqla_session = db.session
        load_instance = True

    branchcode = auto_field()
    branchname = auto_field()
    branchnamekh = auto_field()
    details = auto_field()
    status = auto_field()

