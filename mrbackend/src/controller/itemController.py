from mrbackend.src.schema.movieSchema import MovieSchema
from mrbackend.src.service.searchService import SearchService
from mrbackend import app

searchService = SearchService()
movieSchema = MovieSchema()

@app.route('/movie/<int:movieId>')
def getMovie(movieId):
  q = searchService.movieDetails(movieId)
  return movieSchema.jsonify(movieSchema.dump(q))

@app.route('/tv/<int:tvId>')
def getTV(tvId):
  q = searchService.tvDetails(tvId)
  return movieSchema.jsonify(movieSchema.dump(q))