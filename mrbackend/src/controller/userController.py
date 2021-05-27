from mrbackend import app
from flask import request, jsonify
from mrbackend.src.schema.userSchema import UserSchema
from mrbackend.src.service.userService import UserService


userSchema = UserSchema()
usersSchema = UserSchema(many=True)
userService = UserService()

@app.route('/user/create', methods=['POST'])
def createUser():
  user = userService.newUserInstance(request.json)
  status = userService.addUser(user)
  return jsonify(), status

@app.route('/user/get', methods=['GET'])
def getUsers():
  results = userService.getAllUsers()
  return usersSchema.jsonify(usersSchema.dump(results))

@app.route('/user', methods=['GET'])
def userExists():
  auth = request.headers.get('Authorization')
  exists = userService.userExists(auth)
  user = None
  status = 200
  if(exists): user = userService.getUserDetails(auth)
  else: status = 401
  return jsonify(userSchema.dump(user)), status