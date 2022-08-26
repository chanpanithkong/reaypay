from flask_jwt_extended import (
    jwt_required,
    JWTManager
)
from flask_restful import Resource
from config.db import db, app, api
from models.citizens import tbcitizens
from models.citizenschema import CitizensSchema

jwt = JWTManager(app)

class Citizens(Resource):
    @classmethod
    # @jwt_required()
    def get(cls,cid=None):
        try:  
            data = tbcitizens.find_by_cid(cid)
            schema = CitizensSchema(many=False)
            _data = schema.dump(data)
            return {"citizens":_data}
        except Exception as err:
            return {"msg":err} 


class CitizensList(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            data = tbcitizens.query.all()
            schema = CitizensSchema(many=True)
            _data = schema.dump(data)
            return {"citizens":_data}
        except Exception as err:
            return {"msg":err} 