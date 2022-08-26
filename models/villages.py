from config.db import db

class tbvillages(db.Model):
    
    villageid = db.Column("villageid", db.Integer, primary_key = True)
    village = db.Column(db.String)
    communeid = db.Column("communeid", db.Integer)
    address = db.Column("address", db.String)

    def __init__(self, villageid=None, village = None, communeid=None, address=None):
        self.villageid = villageid
        self.village =village
        self.communeid = communeid
        self.address = address 
        
    @classmethod
    def find_by_villageid(cls, villageid) -> "tbvillages":
        return cls.query.filter_by(villageid=villageid).first()