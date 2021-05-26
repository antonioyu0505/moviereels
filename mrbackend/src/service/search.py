from mrbackend.settings import THE_MOVIE_DB_API_KEY
from mrbackend.src.model.movie import Movie
import requests


class Search:
  def tv(query):
    results = []
    url = "https://api.themoviedb.org/3/search/tv"
    payload = payload = {"api_key" : THE_MOVIE_DB_API_KEY, "language" : "en-US", "page" : "1", "query": query,"include_adult" : "false"}
    response = requests.get(url, params=payload)
    if(response.status_code == 200):
      for result in response.json()['results']:
        results.append(Movie(result['id'], result['name'], result['overview'], result['poster_path']))
    return (response.status_code, results)

  def movie(query):
    results = []
    url = "https://api.themoviedb.org/3/search/movie"
    payload = payload = {"api_key" : THE_MOVIE_DB_API_KEY, "language" : "en-US", "page" : "1", "query": query,"include_adult" : "false"}
    response = requests.get(url, params=payload)
    if(response.status_code == 200):
      for result in response.json()['results']:
        results.append(Movie(result['id'], result['original_title'], result['overview'], result['poster_path']))
    return (response.status_code, results)