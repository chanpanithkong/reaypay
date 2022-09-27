from flask_jwt_extended import (
    
    JWTManager,
    
)
from flask import jsonify
from flask_restful import Resource, request
from config.db import  app, db
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


class DeleteCitizen(Resource):
    @classmethod
    #@jwt_required()
    def post(cls):
        try:
            
            data = request.get_json()
            userid = data['data']['cid']
            get_statusdata = tbcitizens.find_by_cid(userid)
            db.session.delete(get_statusdata)
            db.session.commit()
            return {"msg":  "delete cid : "+data['data']['cid']}  

        except Exception as err:
            return {"msg":err} 

class UpdateCitizen(Resource):
    @classmethod
    # @jwt_required()
    def post(cls):
        try:
            data = request.get_json()

            citizen_data = tbcitizens.find_by_cid(data['data']['cid'])

            if (citizen_data is not None):

                get_statusdata = tbcitizens()
                # get_statusdata.cid = data['data']['cid']
                get_statusdata.lastname = data['data']['lastname']
                get_statusdata.middlename = data['data']['middlename']
                get_statusdata.firstname = data['data']['firstname']
                get_statusdata.gender = data['data']['gender']
                get_statusdata.dob = data['data']['dob']
                get_statusdata.placeofbirth = data['data']['placeofbirth']
                get_statusdata.address = data['data']['address']
                get_statusdata.electioncenter = data['data']['electioncenter']
                get_statusdata.party = data['data']['party']
                get_statusdata.updatedby = data['data']['updatedby']
                get_statusdata.updateddate = data['data']['updateddate']
                
                db.session.add(get_statusdata)
                db.session.commit()
                result = "update cid : " + data['data']['cid']
                return {"msg": result}
            return {"msg": "there is no cid : " + data['data']['cid']}

        except Exception as err:
            return {"msg":err} 

class InsertCitizen(Resource):
    @classmethod
    # @jwt_required()
    def post(cls):
        try:
            data = request.get_json()

            citizen_data = tbcitizens.find_by_cid(data['data']['cid'])

            if (citizen_data is None):

                get_statusdata = tbcitizens()
                get_statusdata.cid = data['data']['cid']
                get_statusdata.lastname = data['data']['lastname']
                get_statusdata.middlename = data['data']['middlename']
                get_statusdata.firstname = data['data']['firstname']
                get_statusdata.gender = data['data']['gender']
                get_statusdata.dob = data['data']['dob']
                get_statusdata.placeofbirth = data['data']['placeofbirth']
                get_statusdata.address = data['data']['address']
                get_statusdata.electioncenter = data['data']['electioncenter']
                get_statusdata.party = data['data']['party']
                get_statusdata.updatedby = data['data']['updatedby']
                get_statusdata.updateddate = data['data']['updateddate']
                
                db.session.add(get_statusdata)
                db.session.commit()
                result = "insert cid : " + data['data']['cid']
                return {"msg": result}
            return {"msg": "already exists cid : " + data['data']['cid']}
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