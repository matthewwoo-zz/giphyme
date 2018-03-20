import os

from flask import Flask, request, redirect, url_for, render_template
from flask import flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

import src.config as c
from src.forms import LoginForm, SignupForm

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = c.UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = c.SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = c.SECRET_KEY
# db = SQLAlchemy(app)

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

@app.route('/query')
def query_gif():
    print Gif.query.all()
    return "Query"



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