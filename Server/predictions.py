#!/usr/bin/env python
# coding: utf-8

get_ipython().system('git clone https://github.com/ultralytics/yolov5')
get_ipython().system('pip install -qr yolov5/requirements.txt')
get_ipython().run_line_magic('cd', 'yolov5')

import torch
from IPython.display import Image, clear_output  # to display images

clear_output()
print('Setup complete. Using torch %s %s' % (torch.__version__, torch.cuda.get_device_properties(0) if torch.cuda.is_available() else 'CPU'))

# This is where the predictions happen. Images are taken from source (currently ../testImg) and saved to /yolov5/runs/detect/exp<runNum>
# weights file (best.pt) should be located in the current directory. 
get_ipython().system('python detect.py --weights ../best.pt --img 416 --conf 0.4 --source ../testImg --save-conf --save-txt')