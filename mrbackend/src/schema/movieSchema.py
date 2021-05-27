from mrbackend.src.extensions import ma
from marshmallow import post_dump
from unicodedata import normalize

class MovieSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'overview', 'posterPath', 'genres')

  @post_dump
  def normalizeCharacters(self, data, **kwargs):
    for field in data:
      if isinstance(data[field], str): data[field] = normalize('NFKD', data[field])
    return data