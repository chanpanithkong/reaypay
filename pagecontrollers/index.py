from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource, request
from config.db import db, app, api
from models.authorities import tbauthorities
from models.authoritiesschema import AuthoritiesSchema
from flask import make_response, render_template
from models.citizens import  tbcitizens
from models.parties import tbparties

class IndexPage(Resource):
    @classmethod
    def get(cls):
        headers = {'Content-Type': 'text/html'}
        partylist = tbparties.query.all()
        return make_response(render_template('index.html',partylist=partylist), 200, headers)

class LoginPage(Resource):
    @classmethod
    def get(cls):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('login.html'), 200, headers)

class CitizenTableList(Resource):
    @classmethod
    def get(cls):
        headers = {'Content-Type': 'text/html'}
        citizenslist = tbcitizens.query.all()
        part = tbparties
        # print(part.find_by_partyid(1).party)
        return make_response(render_template('citizentablelist.html',title='Home',citizenslist = citizenslist, part=part), 200, headers)

class CitizentDataEntry(Resource):
    @classmethod
    def get(cls):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('citizendataentry.html'), 200, headers)

class CitizentDataEdit(Resource):
    @classmethod
    def get(cls,cid=None):
        headers = {'Content-Type': 'text/html'}
        citizen = tbcitizens.find_by_cid(cid)
        partylist = tbparties.query.all()
        return make_response(render_template('citizendataedit.html',c=citizen,partylist=partylist), 200, headers)
        