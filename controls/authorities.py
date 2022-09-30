from flask_jwt_extended import (
    jwt_required,
    JWTManager
)
from flask_restful import Resource
from config.db import db, app, api
from models.authorities import tbauthorities
from models.authoritiesschema import AuthoritiesSchema

jwt = JWTManager(app)

class Authorities(Resource):
    @classmethod
    @jwt_required()
    def get(cls,userid=None):
        try:  
            data = tbauthorities.find_by_userid(userid)
            schema = AuthoritiesSchema(many=False)
            _data = schema.dump(data)
            return {"authorities":_data}
        except Exception as err:
            return {"msg":err} 


class AuthoritiesList(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        try:
            data = tbauthorities.query.all()
            schema = AuthoritiesSchema(many=True)
            _data = schema.dump(data)
            return {"authorities":_data}
        except Exception as err:
            return {"msg":err} 

class IndexPage(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        return "<h1>hello world</h1>" 

# class UserLogin(Resource):
#     @classmethod
#     @jwt_required()
#     def get(cls):
#         try:  
#             data = request.get_json()
#             userid = data['data']['userid']
#             password = data['data']['password']
            
#             get_usersdata = tbusers.find_by_userid(userid)
#             user_schema = UserSchema()
#             user_data = user_schema.dump(get_usersdata)

#             if user_data.password == password:
#                 return {"login":True}
#             return {"login":False}
            
#         except Exception as err:
#             return {"msg":err} 