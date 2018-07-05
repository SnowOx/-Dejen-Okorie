#! python3
# resize_and_add_logo_3.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'


def save_image_to_file(image, filename):
    image_new_save_path = os.path.join('processed_image_', filename)
    image.save(image_new_save_path)
    print('Saved image to path >> %s' % image_new_save_path) 

    
# open_image(path) use this as a generic function
logo_image = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logo_image.size  
# make_new_directory(path)
os.makedirs('processed_images', exist_ok=True)
for filename in os.listdir('.'): # add path
    # check_that_filename_is_an_image_filename
    filename = filename.lower()
    if not (filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.bmp') or filename.endswith('.gif'):
        continue
    # open_image_file()
    image_file = Image.open(filename)
    width, height = image_file.size
    # resize_image_if_dimensions_are_greater_than_square_fit_size
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
        print('Resizing %s...' % (filename))
        im = im.resize((width, height))
    # add_logo_if_image_is_big_enough()
    width, height = im.size
    if width < 2 * logoWidth:
        print("Image width too narrow to add logo")
        save_image_to_file(im, filename)
        continue
    elif height < 2 * logoHeight:
        print("Image height too short to add logo")
        save_image_to_file(im, filename)
        continue
    else:
        print('Adding logo to %s...' % (filename))
        im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
        save_image_to_file(im, filename)
print('Done')


