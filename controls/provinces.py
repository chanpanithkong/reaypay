from flask_jwt_extended import (
    jwt_required,
    JWTManager
)
from flask_restful import Resource
from config.db import db, app, api
from models.provinces import  tbprovinces
from models.provincesschema import ProvincesSchema

jwt = JWTManager(app)

class Provinces(Resource):
    @classmethod
    @jwt_required()
    def get(cls,provinceid=None):
        try:  
            data = tbprovinces.find_by_provinceid(provinceid)
            schema = ProvincesSchema(many=False)
            _data = schema.dump(data)
            return {"provinces":_data}
        except Exception as err:
            return {"msg":err} 


class ProvincesList(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        try:
            data = tbprovinces.query.all()
            schema = ProvincesSchema(many=True)
            _data = schema.dump(data)
            return {"provinces":_data}
        except Exception as err:
            return {"msg":err} 