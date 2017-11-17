import os
from flask import Flask, request, redirect, url_for, render_template
from flask import flash
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "/Users/mattw/Dropbox/Programming/GiphyMe/src/profile_photos"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def hello():
    return render_template('home.html')

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