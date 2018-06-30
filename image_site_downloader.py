#! python3
# image_site_downloader.py

import requests
import bs4
import os

DESIRED_SEARCH_TERM = str(input('Enter search term'))
SEARCH_URL = 'https://unsplash.com/search/photos/' + str(DESIRED_SEARCH_TERM)


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


def write_images(list_of_image_urls):
    for counter, image_url in enumerate(list_of_image_urls):
        requests.get(image_url).raise_for_status()
        image_object = requests.get(image_url).content
        save_the_image(image_object, counter)


def save_the_image(image_object_to_write_to_file, counter):
    folder_path_to_save_images_into = os.path.join(os.getcwd(), 'Search for ' + str(DESIRED_SEARCH_TERM).title() + ' Images')
    os.makedirs(folder_path_to_save_images_into, exist_ok=True)
    image_file_path = os.path.join(folder_path_to_save_images_into, str(DESIRED_SEARCH_TERM) + str(counter) + '.jpg')
    with open(image_file_path, 'wb') as infile:
        infile.write(image_object_to_write_to_file)
    print('Written image %s\n' % counter)


# Engine
page_soup = get_page_soup(SEARCH_URL)
image_url_list = get_list_of_image_urls(page_soup)
write_images(image_url_list)
print('Done')

# Solved! :)
