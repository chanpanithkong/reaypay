from config.db import db

class tbparties(db.Model):
    
    partyid = db.Column("partyid", db.Integer, primary_key = True)
    party = db.Column("party", db.String)
    photo = db.Column("photo", db.String)
    details = db.Column("details", db.String)
    
    def __init__(self, partyid=None, party=None, photo=None, details=None): 
        self.partyid = partyid
        self.party =party
        self.photo = photo
        self.details = details
        
    @classmethod
    def find_by_partyid(cls, partyid) -> "tbparties":
        return cls.query.filter_by(partyid=partyid).first()