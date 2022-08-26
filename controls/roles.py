from flask_jwt_extended import (
    jwt_required,
    JWTManager
)
from flask_restful import Resource
from config.db import db, app, api
from models.roles import tbroles
from models.roleschema import RoleSchema

jwt = JWTManager(app)

class Role(Resource):
    @classmethod
    # @jwt_required()
    def get(cls,roleid=None):
        try:  
            roledata = tbroles.find_by_roleid(roleid)
            role_schema = RoleSchema(many=False)
            role_data = role_schema.dump(roledata)
            return {"branches":role_data}
        except Exception as err:
            return {"msg":err} 


class RoleList(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            roledata = tbroles.query.all()
            role_schema = RoleSchema(many=True)
            role_data = role_schema.dump(roledata)
            return {"branches":role_data}
        except Exception as err:
            return {"msg":err} 