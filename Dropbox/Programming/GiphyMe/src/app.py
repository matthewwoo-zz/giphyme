import os

from flask import Flask, request, redirect, url_for, render_template
from flask import flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.utils import secure_filename
from config import Config

import src.config as c
from src.forms import LoginForm, SignupForm

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
import models
migrate = Migrate(app,db)

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

@app.route('/signup')
def signup():
    form = SignupForm()
    return render_template('signup.html', title='Sign Up', form=form)

# @app.route('/query')
# def query_gif():
#     print Gif.query.all()
#     return "Query"



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in c.ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # the reason why it's 'upload_file' and not 'upload' is that url_for builds url based on the function and not the route
            return redirect(url_for('upload_file',
                                    filename=filename))
    return render_template('upload.html')