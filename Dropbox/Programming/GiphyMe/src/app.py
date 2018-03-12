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
#
class Gif(db.Model):
    __tablename__ = "gifs"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    url = db.Column(db.String)

    def __init__(self, title=None, url=None):
        self.title = title
        self.url = url

    def __repr__(self):
        return "Title: {}, URL: {}, ID: {}".format(self.title, self.url, self.id)

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


#
# from src.models.gifs.gif import Gif
# from src.models.giphymes.giphyme import Giphyme
# from src.models.selfie.selfie import Selfie



# @app.before_first_request()
# def create_tables():
#     db.create_all()

@app.route('/')
def hello():
    # db.create_all()
    gif_1 = Gif(title="Test Gif", url="www.test.com")
    db.session.add(gif_1)
    db.session.commit()
    print db.get_tables_for_bind()
    return render_template('home.html')

@app.route('/query')
def test_db():
    print Gif.query.all()
    return "hello"


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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)