import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, redirect, url_for, render_template
from flask import flash
from werkzeug.utils import secure_filename

import src.config as c

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = c.UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = c.SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)

