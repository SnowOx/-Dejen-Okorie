#! python3
# resize_and_add_logo_3.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import Image

SQUARE_FIT_SIZE = 4000
LOGO_PATH = '#'
FOLDER_OF_IMAGES_TO_BE_PROCESSED_PATH = ' '


def save_image_to_file(image, filename):
    image_new_save_path = os.path.join('processed_image_', filename)
    image.save(image_new_save_path)
    print('Saved image to path >> %s' % image_new_save_path)


# open_image(path) use this as a generic function
logo_image = Image.open(LOGO_PATH)
logoWidth, logoHeight = logo_image.size
print(logoWidth, logoHeight)
# make_new_directory(path)
os.makedirs('processed_images', exist_ok=True)
for filename in os.listdir(FOLDER_OF_IMAGES_TO_BE_PROCESSED_PATH):  # add path
    print(filename)
    # check_that_filename_is_an_image_filename
    filename = filename.lower()
    filename_path = os.path.join(FOLDER_OF_IMAGES_TO_BE_PROCESSED_PATH, filename)
    if not filename.endswith('.png') and not filename.endswith('.jpg') and not filename.endswith('.bmp') and not filename.endswith('.gif'):
        continue
    # open_image_file()
    print('filename_path = %s' % filename_path)
    image_file = Image.open(filename_path)
    width, height = image_file.size
    # resize_image_if_dimensions_are_greater_than_square_fit_size
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
        print('Resizing %s...' % filename_path)
        image_file = image_file.resize((width, height))
    # add_logo_if_image_is_big_enough()
    print(width, height)
    if width < 2 * logoWidth:
        print("Image width too narrow to add logo")
        save_image_to_file(image_file, filename_path)
        continue
    elif height < 2 * logoHeight:
        print("Image height too short to add logo")
        save_image_to_file(image_file, filename_path)
        continue
    else:
        print('Adding logo to %s...' % filename_path)
        image_file.paste(logo_image, (width - logoWidth, height - logoHeight), logo_image)
        save_image_to_file(image_file, filename_path)
    print()
print('Done')

#Solved. Wish to refactor.
