from config.db import db

class tbdisticts(db.Model):
    
    distictid = db.Column("distictid", db.Integer, primary_key = True)
    distict = db.Column(db.String)
    provinceid = db.Column("provinceid", db.Integer)
    
    def __init__(self, distictid=None, distict=None,provinceid=None):
        self.distictid = distictid
        self.distict =distict
        self.provinceid = provinceid
        
    @classmethod
    def find_by_communeid(cls, communeid) -> "tbdisticts":
        return cls.query.filter_by(communeid=communeid).first()