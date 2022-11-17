from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource
from config.db import db, app, api
from models.districts import tbdistricts
from models.districtsschema import DistrictsSchema

jwt = JWTManager(app)

class Districts(Resource):
    @classmethod
    # @jwt_required()
    def get(cls,districtid=None):
        try:  
            data = tbdistricts.find_by_distictid(districtid)
            schema = DistrictsSchema(many=False)
            _data = schema.dump(data)
            return {"districts":_data}
        except Exception as err:
            return {"msg":err} 


class DistrictsList(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            data = tbdistricts.query.all()
            schema = DistrictsSchema(many=True)
            _data = schema.dump(data)
            return {"districts":_data}
        except Exception as err:
            return {"msg":err} 