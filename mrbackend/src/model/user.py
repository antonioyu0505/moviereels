from mrbackend.src.extensions import db
from datetime import datetime

class User(db.Model):
  id = db.Column(db.Integer, primarykey = True)
  username = db.Column(db.String(50), unique = True)
  password = db.Column(db.Text)
  countryCode = db.Column(db.String(2))
  lastLogin = db.Column(db.DateTime)

  def __init__(self, username, password, countryCode):
    self.username = username
    self.password = password
    self.countryCode = countryCode
    self.lastLogin = datetime.now()

  def getUsername(self): print(self.username)
  def getPassword(self): print(self.password)
  def getCountryCode(self): print(self.countryCode)
  def getlastLogin(self): print(self.lastLogin)
