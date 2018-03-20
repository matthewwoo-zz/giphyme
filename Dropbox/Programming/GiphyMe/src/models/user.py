from .base import db, Base

class User(Base):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    username = db.Column(db.Strinq, unique=True)
    password_hash = db.Column(db.String)

    def __repr__(self):
        return "Username: {}, Email: {}, ID: {}".format(self.username, self.email, self.id)
