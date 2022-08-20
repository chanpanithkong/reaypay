from flask_jwt_extended import (
    jwt_required,
    JWTManager
)
from config.db import db, app, api
from flask_restful import Resource, request

from models.branches import tbbranches
from models.branchschema import BranchSchema

jwt = JWTManager(app)

class Branch(Resource):
    @classmethod
    @jwt_required()
    def get(cls,branchcode):
        try:  
            branchdata = tbbranches.find_by_branchcode(branchcode)
            branch_schema = BranchSchema()
            branch_data = branch_schema.dump(branchdata)
            return {"branches":branch_data}
        except Exception as err:
            return {"msg":err} 


class BranchList(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        try:
            branchdata = tbbranches.query.all()
            user_schema = BranchSchema(many=True)
            branch_data = user_schema.dump(branchdata)
            return {"branches":branch_data}
        except Exception as err:
            return {"msg":err} 