import os
basedir = os.path.abspath(os.path.dirname(__file__))

# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app2.db')
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/mattw'
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
UPLOAD_FOLDER = "/Users/mattw/Dropbox/Programming/GiphyMe/src/profile_photos"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gifs'])
SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'