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
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('profile', username=form.username.data))
        # next_page = request.args.get('next')
        # if not next_page or url_parse(next_page).netloc != '':
        #     next_page = url_for('profile', username=form.username.data)
        # return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@login_required
@app.route('/profile/<username>')
def profile(username):
    print current_user
    u = User.query.filter_by(username=current_user.username).first()
    s = Selfie.query.filter_by(user_id=u.id).order_by('-id').first()
    g = Gif.query.filter_by(user_id=u.id).order_by('-id').first()
    selfie_filename = 'http://0.0.0.0:8000/uploads/' + s.filename
    gif_filename = 'http://0.0.0.0:8000/uploads/' + g.filename
    return render_template('profile.html',
                           username=username,
                           selfie_filename=selfie_filename,
                           gif_filename=gif_filename)

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

@login_required
@app.route('/upload_selfie', methods=['GET','POST'])
def upload_selfie():
    u = User.query.filter_by(username=current_user.username).first()
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
            file_path = os.path.join(Config.UPLOAD_FOLDER,filename)
            s = Selfie(emotion="Happy", url=file_path, user=u, filename=filename)
            db.session.add(s)
            db.session.commit()
            flash('Congratulations you have uploaded your selfie')
            # the reason why it's 'upload_file' and not 'upload' is that url_for builds url based on the function and not the route
            # return redirect(url_for('uploaded_file',
            #                         filename=filename))
            return render_template('profile.html',username=u.username)
    return render_template('profile.html', username=u.username)

@login_required
@app.route('/upload_gif', methods=['GET','POST'])
def upload_gif():
    u = User.query.filter_by(username=current_user.username).first()
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
            file_path = os.path.join(Config.UPLOAD_FOLDER,filename)
            s = Gif(emotion="Happy", url=file_path, user=u, filename=filename)
            db.session.add(s)
            db.session.commit()
            print "commited"
            flash('Congratulations you have uploaded your gif')
            # the reason why it's 'upload_file' and not 'upload' is that url_for builds url based on the function and not the route
            # return redirect(url_for('uploaded_file',
            #                         filename=filename))
            return render_template('profile.html',username=u.username)
    return render_template('profile.html', username=u.username)

@app.route('/show/<filename>')
def uploaded_file(filename):
    filename='http://0.0.0.0:8000/uploads/'+filename
    return render_template('show.html',filename=filename)


@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(Config.UPLOAD_FOLDER, filename)



import models
User = models.User
Selfie = models.Selfie
Gif = models.Gif

from src.forms import LoginForm, SignupForm



