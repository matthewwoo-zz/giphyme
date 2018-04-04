import os

from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from flask import flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager,current_user, login_user,logout_user,login_required
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename
from config import Config

import src.config as c


app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)
login.login_view = 'login'
db = SQLAlchemy(app)
migrate = Migrate(app,db)


@login.user_loader
def load_user(id):
    print "user loaded"
    return User.query.get(int(id))


@app.route('/')
def hello():
    return render_template('homepage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('home'))
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@login_required
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/signup', methods=['GET','POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations %s you have signed up with Giiphy me ' % form.username.data)
        return redirect(url_for('login'))
    return render_template('signup.html', title='Sign Up', form=form)

# @app.route('/query')
# def query_gif():
#     print Gif.query.all()
#     return "Query"



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

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
            file.save(os.path.join(Config.UPLOAD_FOLDER, filename))
            print os.path.join(Config.UPLOAD_FOLDER,filename)
            # the reason why it's 'upload_file' and not 'upload' is that url_for builds url based on the function and not the route
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template('upload.html')

@app.route('/show/<filename>')
def uploaded_file(filename):
    filename='http://0.0.0.0:8000/uploads/'+filename
    return render_template('show.html',filename=filename)


@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(Config.UPLOAD_FOLDER, filename)



import models
User = models.User

from src.forms import LoginForm, SignupForm



