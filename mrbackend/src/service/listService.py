from mrbackend.src.extensions import db, Base

List = Base.classes.Movie

class ListService:
  def __init__(self):
    self.list = List

  def newListInstance(self, newItem):
    newItem = self.list(type=newItem['type'], typeId=newItem['typeId'])
    return newItem

  def itemExists(self, item):
    q = db.session.query(self.list).filter_by(type=item['type'], typeId=item['typeId']).first()
    return q

  def addListItem(self, newItem):
    itemId = -1
    try:
      db.session.add(newItem)
      db.session.commit()
      itemId = newItem.id
    except Exception as e:
      print(e)
      db.session.rollback()
    return itemId