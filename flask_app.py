from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
import pandas as pd
from io import StringIO
from main import extract_text_from_pdf, extract_multiple_details

app = Flask(__name__)

# Define the folder for storing uploaded files
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

# Allowed file extensions check
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Extract text from the uploaded PDF
        extracted_text = extract_text_from_pdf(file_path)
        if extracted_text:
            # Extract details from the text
            df = extract_multiple_details(extracted_text)
            # Convert the DataFrame to HTML
            data_html = df.to_html(classes='table table-bordered', index=False)
            return render_template('index.html', table=data_html)
    
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
