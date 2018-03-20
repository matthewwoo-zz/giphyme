from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import src.config as c

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = c.UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = c.SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)

