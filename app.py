from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from marshmallow import ValidationError
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST

# from config.db import db, app, api


from controls.wsusers import WsTokenRefresh, WsUserLogin, WsUserLogout
from controls.authorities import Authorities,AuthoritiesList,  AuthoritiesLogin
from controls.citizens import Citizens,CitizensList,InsertCitizen,DeleteCitizen,UpdateCitizen,UpdateCitizenParty
from controls.communes import Communes,CommunesList
from controls.districts import Districts,DistrictsList
from controls.parties import Parties,PartiesList
from controls.provinces import Provinces,ProvincesList
from controls.roles import Role,RoleList
from controls.userroles import UserRoles,UserRolesList
from controls.villages import Villages,VillagesList

from pagecontrollers.index import IndexPage, LoginPage, CitizenTableList, CitizentDataEntry


# config file
app = Flask(__name__,template_folder='pages')
api = Api(app)

#cambodia
app.config['SECRET_KEY'] = 'eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJpc3MiOiJodHRwczovL2p3dC1pZHAuZXhhbXBsZS5jb20iLCJzdWIiOiJtYWlsdG86bWlrZUBleGFtcGxlLmNvbSIsIm5iZiI6MTY1NzI3NTA4MiwiZXhwIjoxNjU3Mjc4NjgyLCJpYXQiOjE2NTcyNzUwODIsImp0aSI6ImlkMTIzNDU2IiwidHlwIjoiaHR0cHM6Ly9leGFtcGxlLmNvbS9yZWdpc3RlciJ9.'
#disable message error in internal system
app.config['PROPAGATE_EXCEPTIONS'] = True
# mysql db connect
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:$Cambodia__089$@localhost:3306/dbpartychecklist'
#cleardb
#app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql://b26aadaf3595c9:ec5703a5@us-cdbr-east-06.cleardb.net/heroku_fe380b29b8d54aa'
#bongsithdb
# url = quote('13.230.198.156')
# port =  quote('3306')
# username = quote('phanith')
# password =  quote('@Phan1tH@')
# mysqldb = quote('phanith')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + username + ':' + password + '@' + url + ':' + port + '/' + mysqldb

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("CLEARDB_DATABASE_URL")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DEBUG = True
db = SQLAlchemy(app)


# api = Api(app)

# @app.route("/")
# def index():
#     return "Hello World"


# @app.errorhandler(ValidationError)
# def handle_marshmallow_validation(err):
#     return {"msg":err.messages}, 400

# jwt = JWTManager(app)


# @jwt.token_in_blocklist_loader
# def check_if_token_in_blacklist(jwt_header, jwt_payload: dict):
#     jti = jwt_payload["jti"]
#     return jti in BLACKLIST


# jwt token
# api.add_resource(WsUserLogin, "/wslogin")
# api.add_resource(WsTokenRefresh, "/wsrefresh")
# api.add_resource(WsUserLogout, "/wslogout")

api.add_resource(IndexPage, "/")
api.add_resource(LoginPage, "/login")
api.add_resource(CitizenTableList, "/citizentablelist")
api.add_resource(CitizentDataEntry, "/citizendataentry")
#Authorities
api.add_resource(AuthoritiesList, "/authoritieslist")
api.add_resource(Authorities, "/authorities/<userid>")
api.add_resource(AuthoritiesLogin, "/authoritieslogin")
#Citizens
api.add_resource(CitizensList, "/citizenslist")
api.add_resource(Citizens, "/citizens/<cid>")
api.add_resource(DeleteCitizen, "/deletecitizen")
api.add_resource(InsertCitizen, "/insertcitizen")
api.add_resource(UpdateCitizenParty, "/updatecitizenparty")
api.add_resource(UpdateCitizen, "/updatecitizen")

#Roles
api.add_resource(RoleList, "/roleslist")
api.add_resource(Role, "/roles/<roleid>")
#Villages
api.add_resource(VillagesList, "/villageslist")
api.add_resource(Villages, "/villages/<villageid>")
#Communes
api.add_resource(CommunesList, "/communeslist")
api.add_resource(Communes, "/communes/<communeid>")
#Disticts
api.add_resource(DistrictsList, "/distictslist")
api.add_resource(Districts, "/disticts/<distictid>")
#Parties
api.add_resource(PartiesList, "/partieslist")
api.add_resource(Parties, "/parties/<partyid>")
#Provinces
api.add_resource(ProvincesList, "/provinceslist")
api.add_resource(Provinces, "/provinces/<provinceid>")
#UserRoles
api.add_resource(UserRolesList, "/userroleslist")
api.add_resource(UserRoles, "/userrole/<userid>/<roleid>")

#hellow world
# @app.route("/")
# def index():
#     return render_template('index.html')

if __name__ == "__main__":
    db.init_app(app)
    app.run(host='0.0.0.0',port=5000, debug=True)
