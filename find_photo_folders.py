#! python3
# find_photo_folders.py

import os
from PIL import Image

START_POSITION = '/Users/A/Downloads'

photo_files = 0
non_photo_files = 0


def search_files_for_photos():
    for dirpath, dirnames, filenames in os.walk(START_POSITION):
        reset_photo_and_non_photo_files_counter()
        for filename in filenames:
            if check_if_filename_is_an_image_filename(filename) == False:
                continue
            elif check_if_filename_is_an_image_filename(filename) == True:
                filename_path = get_filename_path(dirpath, filename)
                check_image_dimensions(filename_path)
        print_directory_if_it_contains_a_majority_of_image_files(dirpath)


def reset_photo_and_non_photo_files_counter():
    global photo_files
    photo_files = 0
    global non_photo_files
    non_photo_files = 0


def check_if_filename_is_an_image_filename(filename):
    if filename.endswith('.png') or filename.endswith('.jpeg') or filename.endswith('.jpg'):
        return True
    else:
        global non_photo_files
        non_photo_files += 1
        return False


def get_filename_path(dirpath, filename):
    filename_path = os.path.join(dirpath, filename)
    return filename_path


def check_image_dimensions(filename_path):
    with Image.open(filename_path) as image_file:
        width, height = image_file.size
    if width >= 500 and height >= 500:
        global photo_files
        photo_files += 1
    else:
        global non_photo_files
        non_photo_files += 1


def print_directory_if_it_contains_a_majority_of_image_files(dirpath):
    if photo_files > non_photo_files:
        print('%s contains %s photos files and %s non_photo_files\n' % (dirpath, photo_files, non_photo_files))
        print('{} is a photo folder'.format(os.path.basename(dirpath)))
    else:
        print('%s is not a photo folder\n' % dirpath)


search_files_for_photos()