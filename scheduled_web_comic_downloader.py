#! python3
# scheduled_web_comic_downloader.py

import requests
import bs4

COMIC_BOOK_URLS = ['http://www.lefthandedtoons.com/', 'https://www.safelyendangered.com/']

record_of_comic_image_urls = # rather than a list, open a text file with a list of the urls


def download_page():
    page_download = requests.get(url)
    page_download.raise_for_status()
    return page_download


def get_image_link_from_page():
    page_soup = bs4.BeautifulSoup(page_download.text, 'lmxl')
    comic_image_urls = page_soup.select('img class[src]')
    print(comic_image_urls)
    return comic_image_urls

def open_the_record_of_downloaded_comic_images():
    with open('record_of_downloaded_comic_images.txt', 'r') as infile:
        record_of_downloaded_comic_images = infile.read()
        return record_of_downloaded_comic_images


def check_if_image_link_has_been_updated(comic_image_urls):
    for image_url in comic_image_urls:
        if image_url in record_of_comic_image_urls:
            print(image)
            pass
        else:
            # otherwise access





def write_downloaded_comic_urls_to_record_of_comic_image_urls()




# Engine
record_of_downloaded_comic_images = open_the_record_of_downloaded_comic_images()
for comic in COMIC_BOOK_URLS:
    page_download = download_page()
    image_url = get_image_link_from_page()
    check_if_image_link_has_been_updated(comic_image_urls

