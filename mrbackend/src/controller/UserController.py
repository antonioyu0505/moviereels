from mrbackend import app
from flask import request

@app.route('/user/create', methods=['POST'])
def createUser():
  print(request.json)
  return "received"