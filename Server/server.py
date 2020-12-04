
# imports
from flask import Flask, send_from_directory, request, json, redirect, url_for, abort
from flask_cors import CORS
from werkzeug.utils import secure_filename
from flask import Flask
import torch
from IPython.display import Image, clear_output  # to display images
from IPython import get_ipython
import os, re, os.path

app = Flask(__name__)
#uncomment for debug mode
#app.debug = True


# File type configurations
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['IMAGE_EXTENSIONS'] = ['.jpg', '.png', '.jpeg']
app.config['UPLOAD_PATH'] = 'uploaded_images'
app.config['OUTPUT_PATH'] = 'labeled_images'

CORS(app)

# Custom static data
@app.route('/' + app.config['OUTPUT_PATH'] + '/<path:filename>')
def custom_static(filename):
    return send_from_directory(app.config['OUTPUT_PATH'], filename)

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
#
#         # Remove files currently stored in uploaded_images
#         for root, dirs, files in os.walk('UPLOAD_PATH'):
#             var = 1
#             if len(UPLOAD_PATH) != 0:
#                 print("Not empty directory")
#             if len(UPLOAD_PATH) == 0:
#                 print("Not empty directory")
# #             for file in files:
# #                 if not fnmatch.fnmatch(file, secureFilename):
# #                     os.remove(os.path.join(root, file)
#
#         # Remove files currently stored in uploaded_images
#         for root, dirs, files in os.walk('OUTPUT_PATH'):
#             var = 1
# #             for file in files:
# #                 if not fnmatch.fnmatch(file, secureFilename):
# #                     os.remove(os.path.join(root, file)


        # Get file extension
        file_ext = os.path.splitext(filename)[1]

        # File type is not of supported types .jpg, .jpeg or .png
        if file_ext not in app.config['IMAGE_EXTENSIONS']:
            abort(400, 'This file type is unacceptable. Please upload a .jpg, .jpeg, or .png image file type.')

        # File type accepted, save image to path for stored images.
        image.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        print("image " + filename + " saved to: " + 'UPLOAD_PATH')

        # Run ML:
        # This is where the predictions happen. Images are taken from source 'Server/uploaded_images' and saved to 'Server/labeled_images'.
        # weights file (best.pt) should be located in the current directory.
        get_ipython().run_line_magic('cd', 'yolov5')
        clear_output()
        print('Setup complete. Using torch %s %s' % (torch.__version__, torch.cuda.get_device_properties(0) if torch.cuda.is_available() else 'CPU'))

        # This is where the predictions happen. Images are taken from source (currently ../testImg) and saved to /yolov5/runs/detect/exp<runNum>
        # weights file (best.pt) should be located in the current directory.
        get_ipython().system('python detect.py --weights ../best.pt --img 416 --conf 0.4 --source ../uploaded_images/ --exist-ok --project ../../Server --name labeled_images')

        # The settings to write the confidence model confidence is disabled right now, but can be re-enabled by adding the lines: --save-conf --save-txt to the above argument list.

        # labeled_image = model.run(file_path_from_image_dot_save_above), or whatever
        outFilePath = os.path.join(app.config['OUTPUT_PATH'], filename)
        #image.save(outFilePath)

        return outFilePath

    #Error if we aren't able to return file output path (required by frontend for image display)
    abort(400, 'Labeled Image failed to return.')

# Run the server
if __name__ == '__main__':

    # start the server
    app.run(port = 8001)