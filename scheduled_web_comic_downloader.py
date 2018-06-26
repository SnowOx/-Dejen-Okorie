#! python3
# scheduled_web_comic_downloader.py

import requests
from bs4 import BeautifulSoup
import os

# 1. Not writing downloaded url to the database text file
# 2. Variables are confusingly named. Suggest changing variables to include 'site_url' and 'image_url' among others


COMIC_BOOK_URLS = ['http://www.lefthandedtoons.com/', 'https://www.safelyendangered.com/']
LOCATION_TO_SAVE_COMICS = 'C:\\Users\\A\\Downloads'


def open_the_record_of_downloaded_comic_images():
    comic_images_database_path = os.path.join(
        LOCATION_TO_SAVE_COMICS,'record_of_previously_downloaded_comic_images.txt')
    try:
        with open(comic_images_database_path, 'r') as infile:
            record_of_downloaded_comic_images = infile.read()
            infile.close()
    except FileNotFoundError:
        record_of_downloaded_comic_images = open(comic_images_database_path, 'w')
        record_of_downloaded_comic_images.close()
    return record_of_downloaded_comic_images


def download_page(url):
    page_download = requests.get(url)
    page_download.raise_for_status()
    return page_download


def get_comic_image_url_from_page(page_download, comic_url):
    page_soup = BeautifulSoup(page_download.text, 'lxml')
    if comic_url == 'http://www.lefthandedtoons.com/':
        for tag in page_soup.find_all('img'):
            attribute_list = tag.get_attribute_list("class")
            if "comicimage" in attribute_list:
                comic_image_url = tag["src"]
    elif comic_url == 'https://www.safelyendangered.com/': #todo: find image url for comic_url with beautiful soup
        pass
    return comic_image_url


def check_if_image_link_has_been_updated(url):
    if str(url) in record_of_previously_downloaded_comic_images:
        print('No updates found for %s' % str(url))
    else:
        print('%s not present in records. Downloading!' % url)
        image_request = get_image_file(url)
        save_image_file(url, image_request)
        write_downloaded_comic_urls_to_record_of_comic_image_urls(url)
        print('Downloaded')


def write_downloaded_comic_urls_to_record_of_comic_image_urls(url):
    with open('record_of_previously_downloaded_comic_images.txt', 'w') as infile:
        record_of_downloaded_comic_images = infile.write(str(url) + '\n')
        infile.close()
        return record_of_downloaded_comic_images


def get_image_file(image_url):
    print('image url = %s' % image_url)
    requests_object = requests.get(image_url)
    print(type(image_url))
    requests_object.raise_for_status()
    downloaded_image_content = requests.get(image_url).content
    print('downloaded_image_content' + str(type(downloaded_image_content)))
    return downloaded_image_content


def save_image_file(image_url, downloaded_image):
    image_filename = str('filename') + '.png'
    print('Saving %s' % image_filename)
    save_filename_path = os.path.join(LOCATION_TO_SAVE_COMICS, image_filename)
    image_file = open(save_filename_path, 'wb')
    image_file.write(downloaded_image)
    image_file.close()


# Engine
record_of_previously_downloaded_comic_images = open_the_record_of_downloaded_comic_images()
for comic_url in COMIC_BOOK_URLS:
    print('comic_url = %s' % comic_url)
    page_download = download_page(comic_url)
    comic_image_url = get_comic_image_url_from_page(page_download, comic_url)
    check_if_image_link_has_been_updated(comic_image_url)
