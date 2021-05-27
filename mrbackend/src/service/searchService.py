from mrbackend.settings import THE_MOVIE_DB_API_KEY
from mrbackend.src.model.movie import Movie
import requests

class SearchService:
  def tv(self, query):
    results = []
    url = "https://api.themoviedb.org/3/search/tv"
    payload = {"api_key" : THE_MOVIE_DB_API_KEY, "language" : "en-US", "page" : "1", "query": query,"include_adult" : "false"}
    response = requests.get(url, params=payload)
    if(response.status_code == 200):
      for result in response.json()['results']:
        results.append(Movie(result['id'], result['name'], result['overview'], result['poster_path']))
    return (response.status_code, results)

  def movie(self, query):
    results = []
    url = "https://api.themoviedb.org/3/search/movie"
    payload = {"api_key" : THE_MOVIE_DB_API_KEY, "language" : "en-US", "page" : "1", "query": query,"include_adult" : "false"}
    response = requests.get(url, params=payload)
    if(response.status_code == 200):
      for result in response.json()['results']:
        results.append(Movie(result['id'], result['original_title'], result['overview'], result['poster_path']))
    return (response.status_code, results)

  def movieDetails(self, movieId):
    url = "https://api.themoviedb.org/3/movie/{}".format(movieId)
    payload = {"api_key" : THE_MOVIE_DB_API_KEY, "language" : "en-US"}
    response = requests.get(url, params=payload)
    movie = None
    if(response.status_code == 200):
      r = response.json()
      movie = Movie(r['id'], r['original_title'], r['overview'], r['poster_path'])
      for g in r['genres']: movie.genres.append(g['name'])
    return movie

  def tvDetails(self, tvId):
    url = "https://api.themoviedb.org/3/tv/{}".format(tvId)
    payload = {"api_key" : THE_MOVIE_DB_API_KEY, "language" : "en-US"}
    response = requests.get(url, params=payload)
    if(response.status_code == 200):
      r = response.json()
      movie = Movie(r['id'], r['name'], r['overview'], r['poster_path'])
      for g in r['genres']: movie.genres.append(g['name'])
    return movie