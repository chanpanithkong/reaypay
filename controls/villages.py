from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource
from config.db import db, app, api
from models.villages import tbvillages
from models.villagesschema import VillagesSchema

jwt = JWTManager(app)

class Villages(Resource):
    @classmethod
    # @jwt_required()
    def get(cls,villageid=None):
        try:  
            data = tbvillages.find_by_villageid(villageid)
            schema = VillagesSchema(many=False)
            _data = schema.dump(data)
            return {"villages":_data}
        except Exception as err:
            return {"msg":err} 


class VillagesList(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            data = tbvillages.query.all()
            schema = VillagesSchema(many=True)
            _data = schema.dump(data)
            return {"villages":_data}
        except Exception as err:
            return {"msg":err} 