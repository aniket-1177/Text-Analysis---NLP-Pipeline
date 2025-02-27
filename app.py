from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from src.pipeline import run_pipeline
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
if not os.path.exists('uploads'):
    os.makedirs('uploads')

ALLOWED_EXTENSIONS = {'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            results = run_pipeline(file_path)
            os.remove(file_path) #remove the uploaded file after processing.
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)