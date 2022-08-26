from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from marshmallow import ValidationError
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST

from config.db import db, app, api


from controls.wsusers import WsTokenRefresh, WsUserLogin, WsUserLogout
from controls.authorities import Authorities,AuthoritiesList
from controls.citizens import Citizens,CitizensList
from controls.communes import Communes,CommunesList
from controls.disticts import Disticts,DistictsList
from controls.parties import Parties,PartiesList
from controls.provinces import Provinces,ProvincesList
from controls.roles import Role,RoleList
from controls.userroles import UserRoles,UserRolesList
from controls.villages import Villages,VillagesList


@app.route("/")
def index():
    return "Hello World"


# @app.errorhandler(ValidationError)
# def handle_marshmallow_validation(err):
#     return {"msg":err.messages}, 400

# jwt = JWTManager(app)


# @jwt.token_in_blocklist_loader
# def check_if_token_in_blacklist(jwt_header, jwt_payload: dict):
#     jti = jwt_payload["jti"]
#     return jti in BLACKLIST


# # jwt token
# api.add_resource(WsUserLogin, "/wslogin")
# api.add_resource(WsTokenRefresh, "/wsrefresh")
# api.add_resource(WsUserLogout, "/wslogout")


# # users
# api.add_resource(UserList, "/userlist")
# api.add_resource(Users, "/userbyid/<userid>")
# api.add_resource(UserDelete, "/userdelete")
# api.add_resource(UserUpdate, "/userUpdate")
# api.add_resource(UserInsert, "/userUpdate")
# api.add_resource(UserLogin, "/userlogin")

#Authorities
api.add_resource(AuthoritiesList, "/authoritiesList")
api.add_resource(Authorities, "/authorities/<aid>")
#Citizens
api.add_resource(CitizensList, "/citizensList")
api.add_resource(Citizens, "/citizens/<cid>")
#Communes
api.add_resource(CommunesList, "/communesList")
api.add_resource(Communes, "/communes/<cid>")
#Disticts
api.add_resource(DistictsList, "/distictsList")
api.add_resource(Disticts, "/disticts/<did>")
#Parties
api.add_resource(PartiesList, "/partiesList")
api.add_resource(Parties, "/parties/<pid>")
#Provinces
api.add_resource(ProvincesList, "/provincesList")
api.add_resource(Provinces, "/provinces/<pid>")
#UserRoles
api.add_resource(UserRolesList, "/userRolesList")
api.add_resource(UserRoles, "/userRoles/<urid>")



if __name__ == "__main__":
    db.init_app(app)
    app.run(host='0.0.0.0',port=5000, debug=True)