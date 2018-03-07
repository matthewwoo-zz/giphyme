from src.app import db

class Giphyme(db.Model):
    __tablename__ = "giphyme"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    url = db.Column(db.String)

    def __init__(self, title=None, url=None):
        self.title = title
        self.url = url

    def __repr__(self):
        return "Title: {}, URL: {}, ID: {}".format(self.title, self.url, self.id)
