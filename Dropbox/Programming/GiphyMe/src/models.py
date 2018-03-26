from datetime import datetime

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    username = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    selfie_id = db.relationship('Selfie', backref='user', lazy='dynamic')
    gif_id = db.relationship('Gif', backref='user', lazy='dynamic')
    giphyme_id = db.relationship('Giphyme', backref='user', lazy='dynamic')

    def __repr__(self):
        return "Username: {}, Email: {}, ID: {}".format(self.username, self.email, self.id)


class Selfie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emotion = db.Column(db.String)
    url = db.Column(db.String)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    giphyme_id = db.relationship('Giphyme', backref='selfie', lazy='dynamic')

    def __repr__(self):
        return "Emotion: {}, URL: {}, ID: {}".format(self.title, self.url, self.id)

class Gif(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    emotion = db.Column(db.String)
    url = db.Column(db.String)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    giphyme_id = db.relationship('Giphyme', backref='gif', lazy='dynamic')


    def __init__(self, title=None, url=None):
        self.title = title
        self.url = url

    def __repr__(self):
        return "Title: {}, URL: {}, ID: {}".format(self.title, self.url, self.id)


class Giphyme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    emotion = db.Column(db.String)
    url = db.Column(db.String)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    selfe_id = db.Column(db.Integer, db.ForeignKey('selfie.id'))
    gif_id = db.Column(db.Integer, db.ForeignKey('gif.id'))

    def __repr__(self):
        return "Title: {}, URL: {}, ID: {}".format(self.title, self.url, self.id)









