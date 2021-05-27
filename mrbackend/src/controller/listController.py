from mrbackend.src.schema.movieSchema import MovieSchema
from mrbackend.src.service.searchService import SearchService
from mrbackend.src.service.userListService import UserListService
from mrbackend.src.service.listService import ListService
from mrbackend.src.service.userService import UserService
from mrbackend import app
from flask import request, jsonify

userService = UserService()
listService = ListService()
uListService = UserListService()
searchService = SearchService()
movieSchema = MovieSchema()

@app.route('/list/add', methods=['POST'])
def addList():  
  auth = request.headers.get('Authorization')
  exists = userService.userExists(auth)
  status = 200
  itemId = -1
  if(exists):
    itemExists = listService.itemExists(request.json)
    if(itemExists == None):
      newItem = listService.newListInstance(request.json)
      itemId = listService.addListItem(newItem)
    else:
      itemId = itemExists.id
      uList = uListService.newUListInstance(itemId, request.json['tag'], auth)
      status = uListService.addUListItem(uList)
  else: status = 401
  return jsonify(), status

@app.route('/list/update', methods=['PUT'])
def updateList():
  auth = request.headers.get('Authorization')
  exists = userService.userExists(auth)
  status = 200
  if(exists):
    if not(request.json['type'] == "movie" or request.json['type'] == "tv"): status = 400
    else:
      itemId = listService.itemExists(request.json).id
      uListService.modifyUListItem(itemId, auth, request.json['tag'])
  else: status = 401
  return jsonify(), status


@app.route('/list', methods=['GET'])
def getList():
  auth = request.headers.get('Authorization')
  exists = userService.userExists(auth)
  status = -1
  resp = {}
  if(exists):
    itemList = uListService.getUserList(auth)
    resp = itemList.__dict__
    status = 200
  else: status = 401
  return jsonify(resp), status