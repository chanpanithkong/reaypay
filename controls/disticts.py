from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource
from config.db import db, app, api
from models.disticts import tbdisticts
from models.distictsschema import DistictsSchema

jwt = JWTManager(app)

class Disticts(Resource):
    @classmethod
    # @jwt_required()
    def get(cls,distictid=None):
        try:  
            data = tbdisticts.find_by_distictid(distictid)
            schema = DistictsSchema(many=False)
            _data = schema.dump(data)
            return {"disticts":_data}
        except Exception as err:
            return {"msg":err} 


class DistictsList(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            data = tbdisticts.query.all()
            schema = DistictsSchema(many=True)
            _data = schema.dump(data)
            return {"disticts":_data}
        except Exception as err:
            return {"msg":err} 