#!/usr/bin/env python3
import os
from flask import Flask, request
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './Filesystem/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_files_in_system():
  return str(os.listdir("./Filesystem"))

@app.route('/', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'GET':
    return get_files_in_system()
  
  if request.method == 'POST':
    # check if a file is selected
    if 'file' not in request.files:
      return 'No file selected'
    file = request.files['file']
    if file:
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      return 'file uploaded'

@app.route('/<name>', methods=['GET'])
def file_get(name):
  return 'Requested file is ' + name

def main():
    print('File drop app')

if __name__ == "__main__":
    main()
