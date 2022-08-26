from flask_jwt_extended import (
    jwt_required,
    JWTManager
)
from flask_restful import Resource
from config.db import db, app, api
from models.userroles import tbuserroles
from models.userrolesschema import UsersRolesSchema

jwt = JWTManager(app)

class UserRoles(Resource):
    @classmethod
    # @jwt_required()
    def get(cls,userid=None,roleid=None):
        try:  
            data = tbuserroles.find_by_useridroleid(userid,roleid)
            schema = UsersRolesSchema(many=False)
            _data = schema.dump(data)
            return {"userroles":_data}
        except Exception as err:
            return {"msg":err} 


class UserRolesList(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            roledata = tbuserroles.query.all()
            role_schema = UsersRolesSchema(many=True)
            role_data = role_schema.dump(roledata)
            return {"userroles":role_data}
        except Exception as err:
            return {"msg":err} 