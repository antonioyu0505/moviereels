from mrbackend import app
from mrbackend.src.service.searchService import SearchService
from mrbackend.src.schema.movieSchema import MovieSchema
from flask import request

moviesSchema = MovieSchema(many=True)
searchService = SearchService()

@app.route('/search/tv', methods=['GET'])
def searchTV():
  q = searchService.tv(request.args.get('query'))[1]
  return moviesSchema.jsonify(moviesSchema.dump(q))

@app.route('/search/movie', methods=['GET'])
def searchMovie():
  q = searchService.movie(request.args.get('query'))[1]
  return moviesSchema.jsonify(moviesSchema.dump(q))