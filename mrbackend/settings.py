import os

THE_MOVIE_DB_API_KEY = os.environ.get("THE_MOVIE_DB_API_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = True
SQL_DATABASE_URI = "mysql+pymsql://moviereels:moviereels@localhost/moviereelsdb"
SQLALCHEMY_TRACK_MODIFICATIONS = False