#! python3
# custom_seating_cards.py

from PIL import Image, ImageDraw
import image_downloader
import datetime
import logging


FILE_CONTAINING_GUESTS = r'#.txt'
CARD_WIDTH, CARD_HEIGHT = 400, 300
CARD_IMAGE_WIDTH, CARD_IMAGE_HEIGHT = 270, 170
DECORATION_IMAGE_PATH = r'#.jpg'
DECORATION_IMAGE_WIDTH, DECORATION_IMAGE_HEIGHT = 125, 35

# Todo: Express all hard coded figures as ratios of CARD_WIDTH and CARD_HEIGHT
# Todo: Stop image_downloader module from saving all of the guest_images as separate files


def get_current_date():
    now = datetime.datetime.now()
    date = now.strftime("%A %d %B, of the year %Y")
    return date


def get_guest_names():
    with open(FILE_CONTAINING_GUESTS, 'r') as infile:
        guests = infile.read().splitlines()
    return guests


def shorten_name_if_name_is_long(name):
    if len(name) > 24:
        shorter_name = name[0:25]
        print(f'Shortened name to {name}')
        return shorter_name
    else:
        return name


def create_white_canvas():
    base_image = Image.new('RGBA', (CARD_WIDTH, CARD_HEIGHT), 'white')
    return base_image


def download_image_based_on_guest_name(guest):
    downloaded_image_path = image_downloader.get_local_image_for(guest)
    return downloaded_image_path


def resize_guest_image(guest_image_path):
    with Image.open(guest_image_path).convert('RGBA') as guest_image:
        guest_image = guest_image.resize((CARD_IMAGE_WIDTH, CARD_IMAGE_HEIGHT))
        return guest_image


def add_an_image_to_another_image(base_image, added_image, x, y):
    base_image.paste(added_image, (x, y), added_image)
    logging.info(f'{added_image} added to {base_image}')
    return base_image


def add_guest_image(image, name_of_guest):
    try:
        downloaded_image_path = download_image_based_on_guest_name(name_of_guest)
    except IndexError:
        print(f'No image found for {name_of_guest}. Downloading default image')
        downloaded_image_path = download_image_based_on_guest_name('animal')
    guest_image = resize_guest_image(downloaded_image_path)
    combined_image = add_an_image_to_another_image(image, guest_image, 85, 71)
    return combined_image


def add_decoration_to(image):
    decoration = get_resized_decoration_image()  # Todo: Add call fucntion from a list of tuples
    image = add_an_image_to_another_image(image, decoration, 42, 13)
    image = add_an_image_to_another_image(image, decoration, 167, 13)
    image = add_an_image_to_another_image(image, decoration, 282, 13)
    image = add_an_image_to_another_image(image, decoration, 42, 265)
    image = add_an_image_to_another_image(image, decoration, 167, 265)
    image = add_an_image_to_another_image(image, decoration, 282, 265)
    return image


def get_resized_decoration_image():
    image = Image.open(DECORATION_IMAGE_PATH).convert('RGBA')
    image = image.resize((DECORATION_IMAGE_WIDTH, DECORATION_IMAGE_HEIGHT))
    return image


def draw_rectangle_on_image(image, left, top, right, bottom, color):
    drawer = ImageDraw.Draw(image)
    image_with_rectangle = drawer.rectangle((left, top, right, bottom), fill=color)
    return image_with_rectangle


def save_image(image, name):
    filename = 'seating_card_for_' + str(name) + '.png'
    image.save(filename)
    print(f'Saved {filename}')


def add_text_to_image(image, x, y, text, fill_color):
    drawer = ImageDraw.Draw(image)
    image_with_text = drawer.text((x, y), text, fill=fill_color)
    return image_with_text


def add_text_to_top_and_bottom_of_image(image, guest_name):
    text_top = f'The hosts welcome the honorable {guest_name}'
    text_bottom = f'On the evening of {get_current_date()}'
    add_text_to_image(image, 52, 54, text_top, 'black')
    add_text_to_image(image, 68, 247, text_bottom, 'black')


def engine():
    guest_names = get_guest_names()
    for name_of_guest in guest_names:
        name_of_guest = shorten_name_if_name_is_long(name_of_guest)
        image = create_white_canvas()
        image = add_guest_image(image, name_of_guest)
        add_decoration_to(image)
        draw_rectangle_on_image(image, 0, 0, 40, 12, 'black')
        add_text_to_top_and_bottom_of_image(image, name_of_guest)
        save_image(image, name_of_guest)


engine()
