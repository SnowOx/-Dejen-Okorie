#! python3
# resize_and_add_logo_3.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)
for filename in os.listdir('.'):
	filename = filename.lower()
    if not (filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.bmp') or filename.endswith('.gif'):
        continue
    im = Image.open(filename)
    width, height = im.size
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
        print('Resizing %s...' % (filename))
        im = im.resize((width, height))
    width, height = im.size
    if width < 2 * logoWidth:
        print("Image width too narrow to add logo")
        continue
    elif height < 2 * logoHeight:
        print("Image height too short to add logo")
        continue
    else:
        print('Adding logo to %s...' % (filename))
        im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
    im.save(os.path.join('processed_image_', filename))



# Procedural style. Edit to improve style
