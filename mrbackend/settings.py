from decouple import config

THE_MOVIE_DB_API_KEY = config('THE_MOVIE_DB_API_KEY')
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG')
SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = config('SQLALCHEMY_TRACK_MODIFICATIONS')