import os
import subprocess
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, Response
from werkzeug.utils import secure_filename
from pcap import gen_imgs

app = Flask(__name__)

@app.route('/')
def upload_file():
    return render_template('index.html')

@app.route('/generate', methods = ['GET', 'POST'])
def save_file():
    if request.method == 'POST':
        f = request.files['file']
        if f.filename == "":
            return render_template('index.html')
            
        filename = secure_filename(f.filename)
        app.logger.info(str(filename))
        f.save(filename)
        zipfile = gen_imgs(filename)
        
        return send_from_directory(directory=os.path.curdir, path=zipfile)
        

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5555, )