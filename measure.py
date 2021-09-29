# Python program to read
# image using PIL module

# importing PIL
from PIL import Image
import numpy as np
import os
import glob
# Read image

# Extract all the files from the groundtruth folder
dir_name = os.path.dirname(__file__)
file_path = os.path.join(dir_name, 'masks/')
print(file_path)
files = glob.glob(file_path + '*.png')
# Output Images

for file in files[:1]:
    img=Image.open(file)
    # prints format of image
    print("Image format is: "+img.format)
    # prints mode of image
    print(img.width, img.height)
    print(img.mode)
    rgbimg = Image.new("RGB", img.size)
    rgbimg.paste(img)
    print(rgbimg.width, img.height)
    print(rgbimg.mode)
    rgbimg.save('foo.png')