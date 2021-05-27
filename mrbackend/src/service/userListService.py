from mrbackend.src.model.itemList import ItemList
from mrbackend.src.extensions import db, Base

UserList = Base.classes.UserList
Movie = Base.classes.Movie

class UserListService:
  def __init__(self):
    self.ulist = UserList
    self.list = Movie

  def newUListInstance(self, listId, tag, userId):
    newUList = self.ulist(userId=userId, movieId=listId, tag=tag)
    return newUList

  def addUListItem(self, newUList):
    status = -1
    try:
      db.session.add(newUList)
      db.session.commit()
      status = 200
    except Exception as e:
      status = 400
      if 1062 in e.orig.args: status = 409 # 1062 is the code for duplicate value
      print(e)
      db.session.rollback()
    return status

  def uListExists(self, listId, userId):
    q = db.session.query(self.list).filter_by(userId=userId, movieId=listId)
    return db.session.query(q.exists()).scalar()

  def modifyUListItem(self, listId, userId, tag):
    q = db.session.query(self.ulist).filter_by(userId=userId, movieId=listId).first()
    q.tag = tag
    db.session.commit()
    return q

  def getUserList(self, auth):
    q = (db.session.query(self.ulist, self.list).join(self.ulist, self.ulist.movieId==self.list.id)\
      .filter(self.ulist.userId==auth)).all()
    itemList = ItemList(auth)
    for u, l in q:
      itemList.items.append({"tag":u.tag, "type":l.type, "typeId":l.typeId})
    return itemList
    