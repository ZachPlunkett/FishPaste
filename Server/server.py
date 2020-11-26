
# imports
from flask import Flask, send_from_directory, request, json, redirect, url_for, abort
from flask_cors import CORS
from werkzeug.utils import secure_filename
from flask import Flask

import os

# import the machine learning model we are using.
# import model

app = Flask(__name__)
# File type configurations
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['IMAGE_EXTENSIONS'] = ['.jpg', '.png', '.jpeg']
app.config['UPLOAD_PATH'] = 'uploaded_images'
app.config['OUTPUT_PATH'] = 'labeled_images'

CORS(app)


# Send main.js or whatever main entry point for the front end framework
@app.route('/main.js', methods=["GET"])
def get_main():
    print("Hello World!")
     #return contents of main.js
    return send_from_directory('', 'main.js', mimetype='text/javascript')

# Send index.html
@app.route('/', methods=["GET"])
@app.route('/index.html', methods=["GET"])
def get_index():
    #return contents of index.html
    return send_from_directory('', 'index.html', mimetype='text/html')

# Send labeled image
@app.route('/labeled/image', methods=["GET"])
def get_labeled(image):
    #return contents of index.html
    return send_from_directory('', 'labeled_images' + image, mimetype='image')

# Upload image of file type .jpg, .jpeg or .png
@app.route('/upload', methods=['POST'])
def upload_image():
    image = request.files['file']

    # Store file with secure filename, to disallow access to paths such as .bashrc, etc.
    filename = secure_filename(image.filename)
    if filename != '':

        # Get file extension
        file_ext = os.path.splitext(filename)[1]

        # File type is not of supported types .jpg, .jpeg or .png
        if file_ext not in app.config['IMAGE_EXTENSIONS']:
            abort(400, 'This file type is unacceptable. Please upload a .jpg, .jpeg, or .png image file type.')

        # File type accepted, save image to path for stored images.
        image.save(os.path.join(app.config['UPLOAD_PATH'], filename))

         # LJW: placeholder to run model
        # labeled_image = model.run(file_path_from_image_dot_save_above), or whatever

        # Saving to output path for testing.
        image.save(os.path.join(app.config['OUTPUT_PATH'], filename))

        # FOR TESTING return url to image saved (for testing)
        return filename

         # return url_for(os.path.join(app.config['OUTPUT_PATH'], filename))
                # return redirect(url_for(os.path.join(app.config['OUTPUT_PATH'], filename)))
                # return redirect(url_for(get_labeled(filename)))

    # LJW: change this to return error error response, since for some reason we didn't reach step 2 in if block
    #return to index.
    abort(400, 'Labeled Image failed to return.')

# Run the server
if __name__ == '__main__':

    # train the model
    # ml.train()

    # start the server
    app.run(port = 8001)