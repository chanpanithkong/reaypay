from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from marshmallow import ValidationError
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST

from config.db import db, app, api


from controls.wsusers import WsTokenRefresh, WsUserLogin, WsUserLogout
from controls.authorities import Authorities,AuthoritiesList, IndexPage
from controls.citizens import Citizens,CitizensList,InsertCitizen,DeleteCitizen,UpdateCitizen
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
# Hello word

api.add_resource(IndexPage, "/")
bf2ef13ab2147945
#Authorities
api.add_resource(AuthoritiesList, "/authoritieslist")
api.add_resource(Authorities, "/authorities/<aid>")
#Citizens
api.add_resource(CitizensList, "/citizenslist")
api.add_resource(Citizens, "/citizens/<cid>")
api.add_resource(DeleteCitizen, "/deletecitizen")
api.add_resource(InsertCitizen, "/insertcitizen")
api.add_resource(UpdateCitizen, "/updatecitizen")

#Roles
api.add_resource(RoleList, "/rolelist")
api.add_resource(Role, "/role/<cid>")
#Villages
api.add_resource(VillagesList, "/villageslist")
api.add_resource(Villages, "/villages/<cid>")
#Communes
api.add_resource(CommunesList, "/communeslist")
api.add_resource(Communes, "/communes/<cid>")
#Disticts
api.add_resource(DistictsList, "/distictslist")
api.add_resource(Disticts, "/disticts/<did>")
#Parties
api.add_resource(PartiesList, "/partieslist")
api.add_resource(Parties, "/parties/<pid>")
#Provinces
api.add_resource(ProvincesList, "/provinceslist")
api.add_resource(Provinces, "/provinces/<pid>")
#UserRoles
api.add_resource(UserRolesList, "/userroleslist")
api.add_resource(UserRoles, "/userRoles/<urid>")



if __name__ == "__main__":
    db.init_app(app)
    app.run(host='0.0.0.0',port=5000, debug=True)
