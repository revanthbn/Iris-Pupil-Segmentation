import numpy as np
import cv2
from PIL import Image, ImageDraw
import pandas as pd
import os
import glob

# Extract all the files from the groundtruth folder in the training set
dir_name = os.path.dirname(__file__)
file_path = os.path.join(dir_name, 'training_set/groundtruth/')
print(file_path)
files = glob.glob(file_path + '*.csv')

# Creating the mask image for each file in the training set
for file in files:
    # parse the csv groundtruth file
    df = pd.read_csv(file)

    # extracting the name of the output file
    basename = os.path.basename(file)
    # parsing the output file path
    out_name = basename[:-4]+".png"
    out_path = os.path.join(dir_name, 'training_set/masks/'+out_name)

    # processing the info from the csv file
    # pupil measurements
    pupil_x = df['coord_p_true_x'][0]
    pupil_y = df['coord_p_true_y'][0]
    pupil_radX = df['radiusX_p_true'][0]
    pupil_radY = df['radiusY_p_true'][0]
    pupil_theta = df['theta_p_true'][0]

    # iris_measurements
    iris_x = df['coord_i_true_x'][0]
    iris_y = df['coord_i_true_y'][0]
    iris_radX = df['radiusX_i_true'][0]
    iris_radY = df['radiusY_i_true'][0]
    iris_theta = df['theta_i_true'][0]

    # Bounding boxes for drawing the iris
    iris_left = (iris_x - iris_radX, iris_y - iris_radY)
    iris_right = (iris_x + iris_radX, iris_y + iris_radY)
    iris_bounds = [iris_left, iris_right]

    # Bounding boxes for drawing the pupil
    pupil_left = (pupil_x - pupil_radX, pupil_y - pupil_radY)
    pupil_right = (pupil_x + pupil_radX, pupil_y + pupil_radY)
    pupil_bounds = [pupil_left, pupil_right]

    # Creating the mask in the specific file
    img = Image.open(out_path)

    # create ellipse image
    iris = ImageDraw.Draw(img)
    iris.ellipse(iris_bounds, fill="#ffffff")
    pupil = ImageDraw.Draw(img)
    pupil.ellipse(pupil_bounds, fill="#808080")
    img.save(out_path)
