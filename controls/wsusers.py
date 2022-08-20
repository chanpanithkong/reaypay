from flask_restful import Resource
from flask import jsonify, request
from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    jwt_required,
    JWTManager,
    get_jwt_identity,
    set_access_cookies,
    unset_jwt_cookies
)
from flask_jwt_extended import JWTManager
from src.config.db import db, app, api

from ..models.wsusers import tbwsusers
from ..models.wsuserschema import WsUserSchema
from blacklist import BLACKLIST
from ..libs.strings import gettext



jwt = JWTManager(app)
wsuser_schema = WsUserSchema()



class WsUserLogin(Resource):
    @classmethod
    def post(cls):
        user_json = request.get_json()
        user_data = wsuser_schema.load(user_json)
        user = tbwsusers.find_by_email(user_data.email)
        
        if user and user.password == user_data.password:
            response = jsonify({"msg": "login successful"})
            access_token = create_access_token(identity=user.email)

            set_access_cookies(response, access_token)
            
            return {'msg': 'login',"access_token":access_token}, 200
        return {"msg": gettext("user_invalid_credentials")}, 401


class WsUserLogout(Resource):
    @classmethod
    @jwt_required()
    def post(cls):
        jti = get_jwt()['jti']
        BLACKLIST.add(jti)
        
        resp = jsonify({'logout': True})
        
        unset_jwt_cookies(resp)
        print(jti)
        return {'msg': "logout"}, 200


class WsTokenRefresh(Resource):
    @classmethod
    @jwt_required()
    def post(cls):
        current_user = get_jwt_identity()
        print(current_user)
        new_token = create_access_token(identity=current_user, fresh=False)
        return {"msg": "refresh_token","access_token":new_token}, 200
