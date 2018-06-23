#! python3
# image_site_downloader.py

import requests
import bs4
import os

DESIRED_SEARCH_TERM = "foxes"
URL = 'https://unsplash.com/search/photos/' + str(DESIRED_SEARCH_TERM)

# Tidy up the writing below, including the unclear names

def download_page():
    page_download = requests.get(URL)
    page_download.raise_for_status()
    print('Downloading %s' % URL)
    page_soup = bs4.BeautifulSoup(page_download.text, "lxml")
    return page_soup


def get_image_url_list(page_soup):
    raw_links = page_soup.select('img[src]')
    image_url_list = [item.get('src') for item in raw_links if '&w=1000' in item.get('src')] # Purifies list to give search images
    image_url_list = list(set(image_url_list))
    return image_url_list


def write_images(image_url_list):
    counter = 0
    for image_url in image_url_list:
        requests.get(image_url).raise_for_status()
        request_url = requests.get(image_url).content
        save_the_image(request_url,counter)
        counter += 1

        
def save_the_image(request_url, counter):
    os.makedirs('Search for ' + str(DESIRED_SEARCH_TERM) + ' images', exist_ok=True)
    # Todo: modify to write new files into the newly created folder
    image_file = open(str(DESIRED_SEARCH_TERM) + str(counter) + '.jpg', 'wb')
    image_file.write(request_url)
    image_file.close()
    print('Writing %s ' % counter)


# Engine
page_soup = download_page()
image_url_list = get_image_url_list(page_soup)
print(image_url_list)
write_images(image_url_list)

Solved! :)
