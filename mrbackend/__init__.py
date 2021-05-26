from flask import Flask
from mrbackend.src.extensions import db, ma, Base

def create_app(config_file="settings.py"):

  app = Flask(__name__)

  app.config.from_pyfile(config_file)

  db.init_app(app)
  ma.init_app(app)

  return app

app = create_app()

with app.app_context(): Base.prepare(db.engine, reflect = True)

from mrbackend.src.controller import userController, searchController