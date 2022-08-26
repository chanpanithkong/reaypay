from config.db import db

class tbauthorities(db.Model):
    
    userid = db.Column("userid", db.Integer, primary_key = True)
    username = db.Column(db.String)
    userpassword = db.Column(db.String)
    gender = db.Column(db.String)
    dob = db
    address = db.Column(db.String)
    photo = db.Column(db.String)
    
    def __init__(self, userid, username, userpassword, gender, dob, address, photo):
        self.userid = userid
        self.username = username
        self.userpassword = userpassword
        self.gender = gender
        self.dob = dob
        self.address = address
        self.photo = photo
        
        
    @classmethod
    def find_by_userid(cls, userid) -> "tbauthorities":
        return cls.query.filter_by(userid=userid).first()