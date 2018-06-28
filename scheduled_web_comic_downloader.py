#! python3
# scheduled_web_comic_downloader.py

import requests
from bs4 import BeautifulSoup
import os
import time

COMIC_BOOK_URLS = ['http://www.lefthandedtoons.com/', 'https://www.safelyendangered.com/']
LOCATION_TO_SAVE_COMICS = 'C:\\Users\\A\\Downloads'


def open_the_record_of_downloaded_comic_images():
    comic_images_database_path = os.path.join(LOCATION_TO_SAVE_COMICS,
                                              'record_of_previously_downloaded_comic_images.txt')
    try:
        with open(comic_images_database_path, 'r') as infile:
            record_of_downloaded_comic_images = infile.read()
    except FileNotFoundError:
        print('Creating new record of downloaded comic images')
        record_of_downloaded_comic_images = open(comic_images_database_path, 'w')
        record_of_downloaded_comic_images.close()
    return (record_of_downloaded_comic_images, comic_images_database_path)


def download_page(url):
    requests_page_object = requests.get(url)
    requests_page_object.raise_for_status()
    return requests_page_object


def get_comic_image_url_from_page(page_object, url):
    page_soup = BeautifulSoup(page_object.text, 'lxml')
    if url == 'http://www.lefthandedtoons.com/':
        comic_image_url = get_comic_image_url_for_left_handed_toons(page_soup)
    elif url == 'https://www.safelyendangered.com/':
        for tag in page_soup.find_all('img'):
            print(str(tag))     # Update the BS4 mechanism here so that the url is not hardcoded. Add a function also
            comic_image_url = "https://www.safelyendangered.com/wp-content/uploads/2018/05/birthday-new2.png"
    return comic_image_url


def get_comic_image_url_for_left_handed_toons(page_soup):
    for tag in page_soup.find_all('img'):
        attribute_list = tag.get_attribute_list("class")
        if "comicimage" in attribute_list:
            comic_image_url = tag["src"]
            return comic_image_url


def check_if_image_url_is_in_record_of_downloaded_urls(url, path_to_downloaded_image_urls_stored_in_text_file):
    with open(path_to_downloaded_image_urls_stored_in_text_file, 'r') as opened_record_of_downloaded_image_urls:
        record_of_downloaded_image_urls_from_text_file = opened_record_of_downloaded_image_urls.readlines()
        cleaned_record_of_downloaded_image_urls_from_text_file = str(record_of_downloaded_image_urls_from_text_file)
        if url in cleaned_record_of_downloaded_image_urls_from_text_file:   # Is this working correctly?
            return True
        elif url not in cleaned_record_of_downloaded_image_urls_from_text_file:
            return False


def write_downloaded_comic_urls_to_record_of_comic_image_urls(url, location_to_write_text_file_to):
    with open(location_to_write_text_file_to, 'a') as infile:
        infile.write('\nDownloaded comic ' + str(time.strftime("%d%m%Y%s")) + ': ' +'\n' + str(url) + '\n')


def read_downloaded_comic_urls_record(location_from_which_to_read_text_file):
    with open(location_from_which_to_read_text_file, 'r') as infile:
        record_of_downloaded_comic_images = infile.readlines()
    print('record_of_downloaded_comic_images = %s' % str(record_of_downloaded_comic_images))


def get_image_file(image_url):
    requests_object = requests.get(image_url)
    requests_object.raise_for_status()
    downloaded_image_content = requests.get(image_url).content
    return downloaded_image_content


def save_image_file(url, downloaded_image):
    image_filename = time.strftime("%d%m%Y%s") + '.png' # Alter so that every image has a unique name
    print('Saving %s' % image_filename)
    save_filename_path = os.path.join(LOCATION_TO_SAVE_COMICS, image_filename)
    with open(save_filename_path, 'wb') as infile:
        infile.write(downloaded_image)


def get_comic_image_url_from_requests_and_beautiful_soup(comic_url):
    requests_page_object = download_page(comic_url)
    comic_image_url = get_comic_image_url_from_page(requests_page_object, comic_url)
    return comic_image_url


# Engine
record_of_downloaded_comic_images, comic_url_text_file_database_path = open_the_record_of_downloaded_comic_images()
for comic_url in COMIC_BOOK_URLS:
    print('Checking %s' % comic_url)
    comic_image_url = get_comic_image_url_from_requests_and_beautiful_soup(comic_url)
    if check_if_image_url_is_in_record_of_downloaded_urls(comic_image_url, comic_url_text_file_database_path) == True:
        print('Image url %s found in records. Accordingly, this image url will not be downloaded' % str(comic_image_url))
        read_downloaded_comic_urls_record(comic_url_text_file_database_path)
    elif check_if_image_url_is_in_record_of_downloaded_urls(comic_image_url, comic_url_text_file_database_path) == False:
        print('Image url not found in records. Downloading %s!' % str(comic_image_url))
        image_file = get_image_file(comic_image_url)
        save_image_file(comic_image_url, image_file)
        write_downloaded_comic_urls_to_record_of_comic_image_urls(comic_image_url, comic_url_text_file_database_path)
print('Completed')