from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource
from config.db import db, app, api
from models.parties import tbparties
from models.partiesschema import PartiesSchema

jwt = JWTManager(app)

class Parties(Resource):
    @classmethod
    # @jwt_required()
    def get(cls,partyid=None):
        try:  
            data = tbparties.find_by_partyid(partyid)
            schema = PartiesSchema(many=False)
            _data = schema.dump(data)
            return {"parties":_data}
        except Exception as err:
            return {"msg":err} 


class PartiesList(Resource):
    @classmethod
    # @jwt_required()
    def get(cls):
        try:
            data = tbparties.query.all()
            schema = PartiesSchema(many=True)
            _data = schema.dump(data)
            return {"parties":_data}
        except Exception as err:
            return {"msg":err} 