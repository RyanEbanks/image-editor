from PIL import Image, ImageEnhance, ImageFilter
# Importing operating system dependency for reading, writing to files, handling directories and retrieving system information
import os

# These describe the path name where we get the images and the path where the images will be sent once edited
path = './pythonImgs'
pathOut = '/editedPyImgs'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert('L')

    clean_name = os.path.splitext(filename)[0]

    edit.save(f".{pathOut}/{clean_name}_edited.jpg")



