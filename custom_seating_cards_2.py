#! python3
# custom_seating_cards.py

from PIL import Image, ImageDraw
import image_site_downloader


#FILE_CONTAINING_GUESTS = #

card_width, card_height = 288, 360

# def get_guest_name():


def create_white_seating_card():
   base_image = Image.new('RGB', (card_width, card_height))
   return base_image


def get_image_based_on_guests_name(guest):
    guest_image = image_site_downloader.get_image_for_the_name_of_(guest)
    print(type(image))
    return guest_image


def add_an_image_to_another_image(base_image, added_image, x_value, y_value):
    collated_image = base_image.paste(added_image, (x_value, y_value), added_image)
    return collated_image


def draw_rectangle_on_image(image, corner_1_position, corner_2_position, corner_3_position,
                            corner_4_position, color):
    with ImageDraw.Draw(image) as draw:
        draw.rectangle((corner_1_position, corner_2_position, corner_3_position, corner_4_position), fill=color)


## def save_image


def engine():
    guest_name = get_guest_name()
    base_image = create_white_seating_card()
    guest_image = get_image_based_on_guests_name(guest_name)
    collated_image = add_an_image_to_another_image(base_image, guest_image, x_value, y_value) # Todo: Add image coordinates based on the width nad height of the seating card
    draw_rectangle_on_image(image, corner_1_position, corner_2_position, corner_3_position,
                            corner_4_position, color)
