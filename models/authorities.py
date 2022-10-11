from config.db import db

class tbauthorities(db.Model):
    
    userid = db.Column("userid", db.Integer, primary_key = True)
    username = db.Column("username",db.String)
    userpassword = db.Column(db.String)
    gender = db.Column(db.String)
    dob = db.Column(db.DateTime)
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

    @classmethod
    def find_by_username(cls, username) -> "tbauthorities":
        return cls.query.filter_by(username=username).first()