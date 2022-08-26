from xml.sax import default_parser_list
from config.db import db

class tbuserroles(db.Model):
    
    userid = db.Column("userid", db.Integer, primary_key=True)
    roleid = db.Column("roleid", db.Integer, primary_key=True)
    assigneddate = db.Column(db.DateTime)
    assignedby = db.Column(db.Integer)
    details = db.Column(db.String)

    def __init__(self, userid=None, roleid=None, assigneddate=None, assignedby=None, details=None):
        self.userid = userid
        self.roleid =roleid
        self.assigneddate = assigneddate
        self.assignedby =assignedby
        self.details = details
        
        
    @classmethod
    def find_by_useridroleid(cls, userid,roleid) -> "tbuserroles":
        return cls.query.filter_by(userid=userid,roleid=roleid).first()