#!/usr/bin/env python3

import os
from flask import Flask, request
from werkzeug.utils import secure_filename
import sqlite3

UPLOAD_FOLDER = './Filesystem/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_files_in_system():
  return str(os.listdir("./Filesystem"))

@app.route('/', methods=['POST'])
def upload_file():
  if request.method == 'POST':
    # check if a file is selected
    if 'file' not in request.files:
      return 'No file selected'
    file = request.files['file']
    if file:
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      return 'file uploaded'
    return '''
    <!doctype html>
    <title>File drop</title>
    <h1>File drop</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

def main():
    print(get_files_in_system())

if __name__ == "__main__":
    main()
