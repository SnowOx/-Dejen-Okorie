#! python3
# url_link_checker.py

import requests
import bs4
import pprint

WEBPAGE_TO_CHECK_LINK_OF = 'https://www.google.com/'


def get_beautiful_soup_object():
    requests_object = requests.get(WEBPAGE_TO_CHECK_LINK_OF)
    requests_object.raise_for_status()
    bs4_object = bs4.BeautifulSoup(requests_object.text)
    return bs4_object


def get_array_of_urls_from(bs4_object):
    raw_link_data = bs4_object.select('a[href]')
    url_array = []
    for element in raw_link_data:
        url = element.get('href')
        if url.startswith('http') or url.startswith('www'):
            url_array.append(url)
        if url.startswith('//'):
            corrected_url = 'https:' + 'url'
    return (url_array)


def check_and_categorise_each_url_in(url_array):
    successfully_checked_urls = []
    potentially_problematic_urls = []
    for url in url_array:
        print('Checking %s' % url)
        try:
            res = requests.get(url)
            res.raise_for_status()
            successfully_checked_urls.append(url)
        except Exception as inst:
            print('%s appears to have a problem' % inst)
            potentially_problematic_urls.append((url, inst))
    print('Checking done\n')
    return (successfully_checked_urls, potentially_problematic_urls)


def print_url_check_results(successfully_checked_urls, potentially_problematic_urls):
    pprint.pprint('Successfully checked urls: ' + str(successfully_checked_urls))
    pprint.pprint('Potentially problematic urls: ' + str(potentially_problematic_urls))


# Engine
bs4_object = get_beautiful_soup_object()
url_array = get_array_of_urls_from(bs4_object)
successfully_checked_urls, potentially_problematic_urls = check_and_categorise_each_url_in(url_array)
print_url_check_results(successfully_checked_urls, potentially_problematic_urls)

# Solved
