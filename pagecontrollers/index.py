from flask_jwt_extended import (
    # jwt_required,
    JWTManager
)
from flask_restful import Resource, request
from config.db import db, app, api
from models.authorities import tbauthorities
from models.authoritiesschema import AuthoritiesSchema
from flask import make_response, render_template, redirect, send_file
from models.citizens import  tbcitizens
from models.parties import tbparties
from fpdf import FPDF, HTMLMixin

import datetime

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

class MyFPDF(FPDF, HTMLMixin):
    pass

class CitizenTableListPrint(Resource):
    @classmethod
    def get(cls):
        headers = {'Content-Type': 'text/html'}
        citizenslist = tbcitizens.query.all()
        part = tbparties
        
        pdf = MyFPDF()
        #First page
        pdf.add_font('KhmerOS','','KhmerOS.ttf')
        pdf.set_font('KhmerOS','',14)
        pdf.add_page()
        pdf.write_html("<p>test</p>")
        pdf.output('mypdf.pdf','F')
        path = "mypdf.pdf"
        return send_file(path, as_attachment=True)

class CitizentDataEntry(Resource):
    @classmethod
    def get(cls):
        headers = {'Content-Type': 'text/html'}
        isupdate = False
        content = ''
        return make_response(render_template('citizendataentry.html',msg=isupdate,content=content), 200, headers)

class CitizentUpdateData(Resource):
    
    @classmethod
    def post(cls):
        headers = {'Content-Type': 'text/html'}
        citizen_data = tbcitizens.find_by_cid(request.form.get('cid'))

        citizen_data.cid = CitizentAddData.convertNonetoNull(request.form.get('cid'))
        citizen_data.lastname = CitizentAddData.convertNonetoNull(request.form.get('lastname'))
        citizen_data.middlename = CitizentAddData.convertNonetoNull(request.form.get('middlename'))
        citizen_data.firstname = CitizentAddData.convertNonetoNull(request.form.get('firstname'))
        citizen_data.gender = CitizentAddData.convertNonetoNull(request.form.get('gender'))
        citizen_data.dob = datetime.datetime.now()
        citizen_data.placeofbirth = CitizentAddData.convertNonetoNull(request.form.get('placeofbirth'))
        
        citizen_data.electioncenter = CitizentAddData.convertNonetoNull(request.form.get('electioncenter'))
        citizen_data.party = CitizentAddData.convertNonetoNull(request.form.get('party'))
        citizen_data.updatedby = '1'
        citizen_data.updateddate = datetime.datetime.now()
        citizen_data.joinpartydate = datetime.datetime.now()
        citizen_data.position = CitizentAddData.convertNonetoNull(request.form.get('position'))
        citizen_data.partyposition = CitizentAddData.convertNonetoNull(request.form.get('partyposition'))
        citizen_data.education = CitizentAddData.convertNonetoNull(request.form.get('education'))
        citizen_data.nationality = CitizentAddData.convertNonetoNull(request.form.get('nationality'))
        citizen_data.partystatus = CitizentAddData.convertNonetoNull(request.form.get('partystatus'))
        citizen_data.haspartycard = CitizentAddData.convertNonetoNull(request.form.get('haspartycard'))
        citizen_data.provinceid = CitizentAddData.convertNonetoNull(request.form.get('provinceid'))
        citizen_data.districtid = CitizentAddData.convertNonetoNull(request.form.get('districtid'))
        citizen_data.communeid = CitizentAddData.convertNonetoNull(request.form.get('communeid'))
        citizen_data.villageid = CitizentAddData.convertNonetoNull(request.form.get('villageid'))
        citizen_data.address = CitizentAddData.convertNonetoNull(request.form.get('address'))

        db.session.commit()
                

        # return make_response(render_template('citizentablelist.html'), 200, headers)
        return redirect("/citizentablelist")

class CitizentAddData(Resource):
    
    def convertNonetoNull(param):
        if param is None:
            param = ''    
        return param

    @classmethod
    def post(cls):
        headers = {'Content-Type': 'text/html'}
        isadd = False
        citizen_data = tbcitizens.find_by_cid(request.form.get('cid'))

        if (citizen_data is None):
                get_statusdata = tbcitizens()
                get_statusdata.cid = CitizentAddData.convertNonetoNull(request.form.get('cid'))
                get_statusdata.lastname = CitizentAddData.convertNonetoNull(request.form.get('lastname'))
                get_statusdata.middlename = CitizentAddData.convertNonetoNull(request.form.get('middlename'))
                get_statusdata.firstname = CitizentAddData.convertNonetoNull(request.form.get('firstname'))
                get_statusdata.gender = CitizentAddData.convertNonetoNull(request.form.get('gender'))
                get_statusdata.dob = datetime.datetime.now()
                get_statusdata.placeofbirth = CitizentAddData.convertNonetoNull(request.form.get('placeofbirth'))
                
                get_statusdata.electioncenter = CitizentAddData.convertNonetoNull(request.form.get('electioncenter'))
                get_statusdata.party = CitizentAddData.convertNonetoNull(request.form.get('party'))
                get_statusdata.updatedby = '1'
                get_statusdata.updateddate = datetime.datetime.now()
                get_statusdata.joinpartydate = datetime.datetime.now()
                get_statusdata.position = CitizentAddData.convertNonetoNull(request.form.get('position'))
                get_statusdata.partyposition = CitizentAddData.convertNonetoNull(request.form.get('partyposition'))
                get_statusdata.education = CitizentAddData.convertNonetoNull(request.form.get('education'))
                get_statusdata.nationality = CitizentAddData.convertNonetoNull(request.form.get('nationality'))
                get_statusdata.partystatus = CitizentAddData.convertNonetoNull(request.form.get('partystatus'))
                get_statusdata.haspartycard = CitizentAddData.convertNonetoNull(request.form.get('haspartycard'))
                get_statusdata.provinceid = CitizentAddData.convertNonetoNull(request.form.get('provinceid'))
                get_statusdata.districtid = CitizentAddData.convertNonetoNull(request.form.get('districtid'))
                get_statusdata.communeid = CitizentAddData.convertNonetoNull(request.form.get('communeid'))
                get_statusdata.villageid = CitizentAddData.convertNonetoNull(request.form.get('villageid'))
                get_statusdata.address = CitizentAddData.convertNonetoNull(request.form.get('address'))

                db.session.add(get_statusdata)
                db.session.commit()

                content = 'Citizen ID ' + request.form.get('cid') + ' is already added.'
                isadd = True
        else:
                content = 'Citizen ID ' + request.form.get('cid') + ' is already exist.'
               

        return make_response(render_template('citizendataentry.html',isadd=isadd,content=content), 200, headers)

class CitizentDataEdit(Resource):
    @classmethod
    def get(cls,cid=None):
        headers = {'Content-Type': 'text/html'}
        citizen = tbcitizens.find_by_cid(cid)
        partylist = tbparties.query.all()
        return make_response(render_template('citizendataedit.html',c=citizen,partylist=partylist), 200, headers)
        