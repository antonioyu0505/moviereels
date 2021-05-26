from mrbackend import app
from flask import request, jsonify
from mrbackend.src.extensions import db, Base
from mrbackend.src.schema.userSchema import UserSchema
from datetime import datetime

User = Base.classes.User
userSchema = UserSchema()
usersSchema = UserSchema(many=True)

@app.route('/user/create', methods=['POST'])
def createUser():
  username = request.json['username']
  password = request.json['password']
  countryCode = request.json['countryCode']
  status = -1
  user = User(username=username, password=password, countryCode=countryCode, lastLogin=datetime.now())
  try:
    db.session.add(user)
    db.session.commit()
    status = 200
  except Exception as e:
    if 1062 in e.orig.args: status = 409 # 1062 is the code for duplicate value
  return jsonify(), status

@app.route('/user/get', methods=['GET'])
def getUsers():
  results = db.session.query(User).all()
  return usersSchema.jsonify(usersSchema.dump(results))