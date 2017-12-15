# from src.app import db
#
# class Gif (db.Model):
#     __tablename__= 'gifs'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String)
#     url = db.Column(db.String)
#     path = db.Column(db.String)
#
#     def __init__(self, title=None, url=None, path=None):
#         self.title = title
#         self.url = url
#         self.path = path
#
#
#     def __repr__(self):
#         return "Title: {}, URL: {}, ID: {}".format(self.title, self.url, self._id)
#
#
# class User (db.Model):
#     __tablename__= "users"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#
# class Selfie(db.Model):
#     __tablename__ = "selfie"
#
