#! python3
# image_downloader.py

import requests
import bs4
import os


def get_page_soup(url):
    requests_object = requests.get(url)
    requests_object.raise_for_status()
    print('Downloading %s' % url)
    page_soup = bs4.BeautifulSoup(requests_object.text, "lxml")
    return page_soup


def get_list_of_image_urls(soup_object):
    raw_links = soup_object.select('img[src]')
    image_url_list = [item.get('src') for item in raw_links if
                      '&w=1000' in item.get('src')]  # Purifies list to give search images
    list_of_discrete_image_urls = list(set(image_url_list))
    return list_of_discrete_image_urls


def return_image_from_(url):
    image_object = requests.get(url).content
    return image_object


def save_and_return_image_path(image_object_to_write_to_file, search_term):
    image_filename = str(search_term) + '.jpg'
    with open(image_filename, 'wb') as infile:
        infile.write(image_object_to_write_to_file)
    image_path = os.path.abspath(image_filename)
    print('Wrote image %s' % search_term)
    return image_path


def get_local_image_for(search_term):
    search_url = 'https://unsplash.com/search/photos/' + str(search_term)
    page_soup = get_page_soup(search_url)
    image_url_list = get_list_of_image_urls(page_soup)
    image_object = return_image_from_(image_url_list[0])
    image_path = save_and_return_image_path(image_object, search_term)
    return image_path
