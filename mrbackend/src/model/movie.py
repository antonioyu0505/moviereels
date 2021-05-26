class Movie():

  def __init__(self, id, name, overview, posterPath):
    self.__id = id
    self.__name = name
    self.__overview = overview
    self.__posterPath = posterPath

  @property
  def id(self): return self.__id

  @property
  def name(self): return self.__name

  @property
  def overview(self): return self.__overview

  @property
  def posterPath(self): return self.__posterPath