from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from marshmallow import ValidationError
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST


from config.db import db, app, api


from control.wsusers import WsTokenRefresh, WsUserLogin, WsUserLogout


app = Flask(__name__, template_folder='templates')

api = Api(app)




@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return {"msg":err.messages}, 400

jwt = JWTManager(app)


@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload: dict):
    jti = jwt_payload["jti"]
    return jti in BLACKLIST


# jwt token
api.add_resource(WsUserLogin, "/wslogin")
api.add_resource(WsTokenRefresh, "/wsrefresh")
api.add_resource(WsUserLogout, "/wslogout")

# users
api.add_resource(UserList, "/userlist")
api.add_resource(Users, "/userbyid/<userid>")
api.add_resource(UserDelete, "/userdelete")
api.add_resource(UserUpdate, "/userUpdate")
api.add_resource(UserInsert, "/userUpdate")
api.add_resource(UserLogin, "/userlogin")

#brnaches
api.add_resource(BranchList, "/branchlist")
api.add_resource(Branch, "/branchbycode/<branchcode>")
#departments
api.add_resource(DepartmentList, "/departmentlist")
api.add_resource(Department, "/departmentbyid/<deptid>")
#formcategories
api.add_resource(FormCategoryList, "/formcategorylist")
api.add_resource(FormCategory, "/formcategorybyid/<formcategoryid>")
#forms
api.add_resource(FormList, "/formlist")
api.add_resource(Form, "/formbyid/<formid>")
#positsions
api.add_resource(PositionList, "/positionlist")
api.add_resource(Position, "/positionbyid/<positionid>")
#rolecategories
api.add_resource(RoleCategoryList, "/rolecategorylist")
api.add_resource(RoleCategory, "/rolecategorybyid/<rolecategoryid>")
#roles
api.add_resource(RoleList, "/rolelist")
api.add_resource(Role, "/rolebyid/<roleid>")
#serialnumbers
api.add_resource(SerialNumbersList, "/serialnumberlist")
api.add_resource(SerialNumbers, "/serialnumberbyid/<serialnumber>")
#status
api.add_resource(StatusList, "/statuslist")
api.add_resource(Status, "/statusbyid/<statusid>")
#systems
api.add_resource(SystemList, "/systemlist")
api.add_resource(System, "/systembyid/<systemid>")
#systemserialnumbers
api.add_resource(SystemSertialNumberList, "/systemserialnumberlist")
api.add_resource(SystemSertialNumber, "/systemserialnumberbyid/<systemid>")
#userlog
api.add_resource(UserLogList, "/userloglist")
api.add_resource(UserLog, "/userlogbyid/<userlogid>")
#userrequestforms
api.add_resource(UserRequestFormList, "/userrequestformlist")
api.add_resource(UserRequestForm, "/userrequestformbyid/<aid>")
#userroles
api.add_resource(UserRoleList, "/userrolelist")
api.add_resource(UserRole, "/userrolebyid/<userid>")



if __name__ == "__main__":
    db.init_app(app)
    app.run(host='0.0.0.0',port=5000, debug=True)