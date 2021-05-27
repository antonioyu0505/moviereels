from mrbackend.src.extensions import db, Base
from sqlalchemy.sql import exists
from datetime import datetime

User = Base.classes.User

class UserService:
  def __init__(self):
    self.user = User

  def newUserInstance(self, newUser):
    newUser = self.user(username=newUser['username'], password=newUser['password'], countryCode=newUser['countryCode'], 
    lastLogin=datetime.utcnow())
    return newUser

  def addUser(self, newUser):
    status = -1
    try:
      db.session.add(newUser)
      db.session.commit()
      status = 200
    except Exception as e:
      status = 400
      if 1062 in e.orig.args: status = 409 # 1062 is the code for duplicate value
      print(e)
      db.session.rollback()
    return status
  
  # This function will be revamped into the future, once the session tokens comes into play.
  # 401 if Unauthorized
  def userExists(self, auth):
    return db.session.query(exists().where(self.user.id == auth)).scalar()

  def getUserDetails(self, auth):
    query = db.session.query(self.user).filter_by(id = auth).first()
    return query

  def getAllUsers(self):
    return db.session.query(self.user).all()