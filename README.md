# FishPaste
Spongebob character detector

First the code should be cloned or downloaded from the Github repository: https://github.com/ZachPlunkett/FishPaste . 
Either an existing weights file should be downloaded: https://drive.google.com/file/d/1bojdAnNtfdQ4LAD3mmF0bQLL1ssPUkWK/view?usp=sharing (example that was trained for this project), 
or the training can be performed by running “YOLOV5Train.ipynb” (from the repository) in Google Colab which will output a weights file with the extension “.pt”. 

The weights file should be saved in the Server directory of the repository with the name “best.pt”. The entire data set can be found within the repository, however the
weights file is far too large to include in the repository which is why it must be downloaded or trained separately. As mentioned in Section 2, the dataset can be 
downloaded from Google Drive by clicking this link: https://drive.google.com/file/d/1xNuINEDmn-5vROKtrwJnhL3_04siJNBF/view?usp=sharing

Next, the dependencies need to be installed. This is done by running “ipython dependenciesInstall.py” within the Server directory. Note that it is important that your 
current working directory is the Server directory before this command is run so that the YOLOv5 dependency is cloned to the correct location.

Next, the backend server needs to be started. This is done by running “ipython server.py” in the Server directory. This will start the Flask web server that takes POST 
requests, runs the YOLOV5 detection algorithm using the “best.pt” weights file, and returns the path to the labeled image back to the frontend.

Next, the frontend server needs to be started. In the fish-paste-frontend directory, type "npm install". Note that this requires both Node.js and the Angular CLI to be installed. 
The Angular CLI can be installed globally with the command "npm install -g @angular/cli". Then, start the frontend by running “npm start” in the fish-paste-frontend directory. 
Note also that the first time the command is run, it must download all of the dependencies to run the frontend which may take several minutes, but is not required on subsequent runs.

Once the front end server is running, it will indicate that the server is running at http://localhost:4200. Finally, navigate to this location in your web browser. 
You should be greeted with a set of instructions which indicate to click the “Choose File” button to choose an image on your local storage (if you don’t have one, 
here is a good sample: http://fairfieldmirror.com/wp-content/uploads/2016/10/SpongeBob-SquarePants-and-friends-750x400.jpg ). Next, click “Detect!” This will send the 
request to the backend. The server will run predictions on the image, store the image in the Server directory, and the frontend will display this labeled image.