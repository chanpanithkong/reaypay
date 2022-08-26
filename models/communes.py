from config.db import db

class tbcommunes(db.Model):
    
    communeid = db.Column("communeid", db.Integer, primary_key = True)
    commune = db.Column(db.String)
    distictid = db.Column(db.Integer)
    
    def __init__(self, communeid=None,commune= None, distictid=None):
        self.communeid = communeid
        self.commune =commune
        self.distictid = distictid
        
    @classmethod
    def find_by_communeid(cls, communeid) -> "tbcommunes":
        return cls.query.filter_by(communeid=communeid).first()