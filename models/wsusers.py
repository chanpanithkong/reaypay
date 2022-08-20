from ..config.db import db

class tbwsusers(db.Model):
    
    wsuserid= db.Column('wsuserid', db.Integer, primary_key = True)
    email = db.Column(db.String(255))
    password = db.Column(db.String(100))
    
    def __init__(self, wsuserid = None, email = None, password = None):
        self.wsuserid = wsuserid
        self.email = email
        self.password = password

    @classmethod
    def find_by_email(cls, email: str) -> "tbwsusers":
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, wsuserid: int) -> "tbwsusers":
        return cls.query.filter_by(wsuserid=wsuserid).first()
        