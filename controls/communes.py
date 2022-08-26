from flask_jwt_extended import (
    jwt_required,
    JWTManager
)
from flask_restful import Resource
from config.db import db, app, api
from models.communes import tbcommunes
from models.communesschema import CommunesSchema

jwt = JWTManager(app)

class Communes(Resource):
    @classmethod
    # @jwt_required()
    def get(cls,communeid=None):
        try:  
            data = tbcommunes.find_by_communeid(communeid)
            schema = CommunesSchema(many=False)
            _data = schema.dump(data)
            return {"communes":_data}
        except Exception as err:
            return {"msg":err} 


class CommunesList(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            data = tbcommunes.query.all()
            schema = CommunesSchema(many=True)
            _data = schema.dump(data)
            return {"communes":_data}
        except Exception as err:
            return {"msg":err} 