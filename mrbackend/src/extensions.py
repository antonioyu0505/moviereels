from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.ext.automap import automap_base

db = SQLAlchemy()
ma = Marshmallow()
Base = automap_base()