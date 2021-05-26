from mrbackend.src.extensions import db
from datetime import datetime

class User(db.Model):
  _id = db.Column(db.Integer, primary_key = True)
  _username = db.Column(db.String(50), unique = True)
  _password = db.Column(db.Text)
  _countryCode = db.Column(db.String(2))
  _lastLogin = db.Column(db.DateTime)

  def __init__(self, username, password, countryCode):
    self._username = username
    self._password = password
    self._countryCode = countryCode
    self._lastLogin = datetime.now()

  def getUsername(self): print(self._username)
  def getPassword(self): print(self._password)
  def getCountryCode(self): print(self._countryCode)
  def getlastLogin(self): print(self._lastLogin)
