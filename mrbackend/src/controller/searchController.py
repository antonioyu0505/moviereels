from mrbackend import app
from mrbackend.src.service.search import Search
from flask import request, jsonify

@app.route('/search/tv', methods=['GET'])
def searchTV():
  results = []
  for result in Search.tv(request.args.get('query'))[1]: results.append(result.__dict__)
  return jsonify(results)

@app.route('/search/movie', methods=['GET'])
def searchMovie():
  results = []
  for result in Search.movie(request.args.get('query'))[1]: results.append(result.__dict__)
  return jsonify(results)