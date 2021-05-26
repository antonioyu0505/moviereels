from mrbackend import app
from mrbackend.src.service.search import Search
from mrbackend.src.schema.movieSchema import MovieSchema
from flask import request, jsonify

moviesSchema = MovieSchema(many=True)

@app.route('/search/tv', methods=['GET'])
def searchTV():
  q = Search.tv(request.args.get('query'))[1]
  return moviesSchema.jsonify(moviesSchema.dump(q))

@app.route('/search/movie', methods=['GET'])
def searchMovie():
  q = Search.movie(request.args.get('query'))[1]
  return moviesSchema.jsonify(moviesSchema.dump(q))