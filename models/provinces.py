from config.db import db

class tbprovinces(db.Model):
    
    provinceid = db.Column("provinceid", db.Integer, primary_key = True)
    province = db.Column(db.String)
    details = db.Column(db.Integer)
    
    def __init__(self, provinceid=None, province = None, details=None):
        self.provinceid = provinceid
        self.province =province
        self.details = details
        
    @classmethod
    def find_by_provinceid(cls, provinceid) -> "tbprovinces":
        return cls.query.filter_by(provinceid=provinceid).first()