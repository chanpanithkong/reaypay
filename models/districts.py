from config.db import db

class tbdistricts(db.Model):
    
    districtid = db.Column("districtid", db.Integer, primary_key = True)
    district = db.Column(db.String)
    provinceid = db.Column("provinceid", db.Integer)
    
    def __init__(self, districtid=None, district=None,provinceid=None):
        self.districtid = districtid
        self.district =district
        self.provinceid = provinceid
        
    @classmethod
    def find_by_districtid(cls, districtid) -> "tbdristicts":
        return cls.query.filter_by(districtid=districtid).first()