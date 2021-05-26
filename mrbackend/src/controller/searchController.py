from mrbackend import app
from mrbackend.src.service.search import Search
from mrbackend.src.util.jsonEncoder import JsonEncoder
from flask import request
from json import dumps

@app.route('/search/tv', methods=['GET'])
def searchTV():
  results = []
  for result in Search.tv(request.args.get('query'))[1]: results.append(dumps(result, cls=JsonEncoder))
  response = app.response_class(
    response=results,
    status=200,
    mimetype='application/json'
  )
  return response

@app.route('/search/movie', methods=['GET'])
def searchMovie():
  results = []
  for result in Search.movie(request.args.get('query'))[1]: results.append(dumps(result, cls=JsonEncoder))
  response = app.response_class(
    response=results,
    status=200,
    mimetype='application/json'
  )
  return response