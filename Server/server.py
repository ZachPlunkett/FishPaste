
# imports
from flask import Flask, send_from_directory, request, json, redirect, url_for, abort
from flask_cors import CORS
from werkzeug.utils import secure_filename

import os

# import the machine learning model we are using.
# import model

app = Flask(__name__)
# File type configurations
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['IMAGE_EXTENSIONS'] = ['.jpg', '.png', '.jpeg']
app.config['UPLOAD_PATH'] = 'uploaded_images'

CORS(app)

# Send index.html
@app.route('/', methods=["GET"])
@app.route('/index.html', methods=["GET"])
def get_index():
    #return contents of index.html
    return send_from_directory('', 'index.html', mimetype='text/html')

# Send main.js or whatever main entry point for the front end framework
@app.route('/main.js', methods=["GET"])
def get_main():
     #return contents of main.js
    return send_from_directory('', 'main.js', mimetype='text/javascript')

# Send the result from machine learning
# Endpoint is "result", where the result is the predicted character in the uploaded image.
@app.route('/result', methods=["GET"])
def characterResult():

    # call the prediction function in model.py
    # characterInImage = model.prediction()

    # convert dictionary to JSON string
    resultString = json.dumps(characterInImage)

    return resultString

# Upload image of file type .jpg, .jpeg or .png
@app.route('/', methods=['POST'])
def upload_image():
    image = request.files['file']

    # store file with secure filename, to disallow access to paths such as .bashrc, etc.
    filename = secure_filename(image.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]

        # file type is not of supported types .jpg, .jpeg or .png
        if file_ext not in app.config['IMAGE_EXTENSIONS']:
            abort(400, 'This file type is unacceptable. Please upload a .jpg, .jpeg, or .png image file type.')

        #file type accepted, save image to path for stored images.
        image.save(os.path.join(app.config['UPLOAD_PATH'], filename))

    #return to index.
    return redirect(url_for('get_index'))





# Run the server
if __name__ == '__main__':

    # train the model
    # ml.train()

    # start the server
    app.run(port = 8001)