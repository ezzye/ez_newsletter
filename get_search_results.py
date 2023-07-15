#!/usr/bin/env python


import os
import json
import requests
import time
import random
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse
from urllib.parse import urljoin

visited_urls = []
level = 0
total_results_texts, total_results_image_links = [], []


# Function to make GET request like Google Chrome
def get_request(url):
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'Upgrade-Insecure-Requests': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
    }
    web_response = None  # Initialize web_response to None
    try:
        session = HTMLSession()
        web_response = session.get(url, headers=headers)
        session.close()
        # response = requests.get(url, headers=headers)

    except requests.exceptions.RequestException as e:
        print(e)
    return web_response


def scrape_url_for_terms(url, page_search_terms, image_search_terms,
                         total_results_texts, total_results_image_links, level=0, domain=None):
    # add url to list of visited urls
    if url in visited_urls:
        return [], []
    else:
        visited_urls.append(url)

    if url.split('.')[-1] in ['pdf', 'doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx']:
        return [], []

    for bad_site in ['mailto', 'facebook', 'twitter', 'instagram', 'youtube', 'linkedin', 'pinterest', 'reddit', 'tumblr',
                     'flickr', 'vimeo', 'soundcloud', 'myspace', 'deviantart']:
        if bad_site in url:
            return [], []

    in_results_texts, in_results_image_links = [], []
    ex_results_texts, ex_results_image_links = [], []

    if level == 0:
        domain = urlparse(url).netloc

    # Download the webpage
    response = get_request(url)
    if response is None:
        return [], []
    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    results_texts = get_text_from_url(page_search_terms, soup)

    results_image_links = scrape_url_for_images(soup, image_search_terms)

    in_results_links, ex_results_links = scrape_url_for_links(soup, page_search_terms, domain)

    if level < 1:
        for link in in_results_links:
            in_results_texts, in_results_image_links = scrape_url_for_terms(link, page_search_terms, image_search_terms,
                                                                            total_results_texts,
                                                                            total_results_image_links, level=level + 1,
                                                                            domain=domain)
    if level < 1:
        for link in ex_results_links:
            ex_results_texts, ex_results_image_links = scrape_url_for_terms(link, page_search_terms, image_search_terms,
                                                                            total_results_texts,
                                                                            total_results_image_links, level=level + 1,
                                                                            domain=domain)

    total_results_texts.extend(results_texts)
    total_results_texts.extend(in_results_texts)
    total_results_texts.extend(ex_results_texts)
    total_results_image_links.extend(results_image_links)
    total_results_image_links.extend(ex_results_image_links)
    total_results_image_links.extend(ex_results_image_links)

    return total_results_texts, total_results_image_links


def get_text_from_url(page_search_terms, soup):
    # Extract all text snippets
    all_text = [text for text in soup.stripped_strings]
    # Join the text snippets together with '|' to make strings of text bigger than 1000 characters,
    # if possible, but less than 2000 characters.
    combined_text = '|'.join(all_text)
    split_index = [m.start() for m in re.finditer('\|', combined_text)]
    split_index = [0] + [idx for idx in split_index if 2000 <= idx <= 4000] + [len(combined_text)]
    chunked_texts = [combined_text[split_index[i - 1]:split_index[i]] for i in range(1, len(split_index))]
    # Filter the resulting strings and only include a string in the results if it contains at least one
    # of the provided page search terms.
    results = [text for text in chunked_texts if any(term in text for term in page_search_terms)]
    return results


def scrape_url_for_images(soup, image_search_terms):
    # Extract all image elements
    img_elements = soup.find_all('img')

    image_links = []

    for img in img_elements:
        if 'src' in img.attrs:
            src = img['src']
            alt = img.get('alt', '')

            # Extract the parent element's text
            parent_text = img.parent.get_text() if img.parent else ''

            # Find the position of the img tag within the parent's text
            surrounding_text = ''
            for match in re.finditer(re.escape(str(img)), parent_text):
                start, end = match.span()
                surrounding_text = parent_text[max(0, start - 250):min(len(parent_text), end + 250)]

            # If any of the search terms are in the src, alt, or surrounding text, add the src to the results
            if any(term in content for term in image_search_terms for content in [src, alt, surrounding_text]):
                image_links.append(src)

    return image_links


def scrape_url_for_links(soup, page_search_terms, original_domain):
    # Extract all link elements
    a_elements = soup.find_all('a')

    # Extract the 'href' attribute of each link element as the web link
    # Filter the resulting web links and only include a link in the results if it contains at least one
    # of the provided page search terms.
    web_links = [a['href'] for a in a_elements if
                 'href' in a.attrs and any(term in a['href'] for term in page_search_terms)]

    same_domain_links = []
    different_domain_links = []

    for link in web_links:
        link_domain = urlparse(link).netloc
        # Compare the domain of the link to the domain of the original url
        if link_domain == original_domain or link_domain == '':
            same_domain_links.append(urljoin(f'https://{original_domain}/', link))
        else:
            different_domain_links.append(link)

    return same_domain_links, different_domain_links


def remove_duplicates(links, text_snippets):
    unique_links = list(set(links))  # Remove duplicate links

    # Separate snippets by '|' character and remove duplicates
    # all_snippets = [snippet for text in text_snippets for snippet in text.split('|')]

    return unique_links, text_snippets


# Function to get the first 5 Google search results pages for each topic and search term combination
def google_search(input_file_name, topics, search_terms):
    # The main dictionary to hold the file name, topic, search term, and corresponding results
    main_dict = {}
    for topic in topics:
        for term in search_terms:
            for i in range(1, 6):
                item = (i * 10) - 10
                url = f"https://www.google.com/search?q={topic}+{term}&start={item}&sourceid=chrome&ie=UTF-8"
                response = get_request(url)
                results = parse_results(response)
                append_search_results(input_file_name, topic, term, results, main_dict)
                time.sleep(random.uniform(5, 15))  # Sleep to make fewer than 7 requests per minute
                # input file name, topic, search term, page number, and output results into a json file
    # print("--------------------------------START-------------------------------------")
    # print(main_dict)
    # print("---------------------------------END------------------------------------")
    dir_path = './links_search'
    with open(f'{dir_path}/{input_file_name}', 'w') as f:
        json.dump(main_dict, f, indent=2)


def append_search_results(input_file_name, topic, search_term, results_dict, main_dict):
    # If the input file name already exists in the main dictionary, just update the relevant fields
    # print(f"main_dict:   {main_dict}")
    if input_file_name in main_dict:
        # If the topic already exists under the input file name, just update the relevant fields
        if topic in main_dict[input_file_name]:
            # If the search term already exists under the topic, append the results to the existing list
            if search_term in main_dict[input_file_name][topic]:
                # print("Search term already exists")
                # print(f"results_dict: {results_dict}")
                # print(f"existing result: {main_dict[input_file_name][topic][search_term]}")
                main_dict[input_file_name][topic][search_term].extend(results_dict)
            else:
                # If the search term does not exist under the topic, create a new list with the results
                # print("Search term does not exist")
                # print(f"results_dict: {results_dict}")
                # print(f"existing result: {main_dict[input_file_name][topic]}")
                main_dict[input_file_name][topic][search_term] = results_dict
        else:
            # If the topic does not exist under the input file name, create a new dictionary for the topic and search term
            # print("Topic does not exist")
            # print(f"results_dict: {results_dict}")
            # print(f"existing result: {main_dict[input_file_name]}")
            main_dict[input_file_name][topic] = {search_term: results_dict}
    else:
        # If the input file name does not exist in the main dictionary, create a new dictionary for the file name, topic, and search term
        # print("Input file name does not exist")
        # print(f"results_dict: {results_dict}")
        # print(f"existing result: main_dict")
        main_dict[input_file_name] = {topic: {search_term: results_dict}}

    return main_dict


def parse_results(response: object) -> object:
    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".VwiC3b"

    results = response.html.find(css_identifier_result)

    output = []

    for result in results:
        title = result.find(css_identifier_title, first=True)
        link = result.find(css_identifier_link, first=True)
        test = result.find(css_identifier_text, first=True)
        if title is None or link is None or test is None:
            continue
        item = {
            'title': title.text,
            'link': link.attrs['href'],
            'text': test.text
        }

        output.append(item)

    return output


def get_search_content():
    for fname in os.listdir(search_folder):
        if fname.endswith('.json'):
            with open(os.path.join(links_search_folder, fname), 'r') as links_file:
                links_data = json.load(links_file)
                with open(os.path.join(search_folder, fname), 'r') as file:
                    search_data = json.load(file)
                    for topic in search_data["topics"]:
                        for google_search_terms in search_data["google search terms"]:
                            image_search_terms = search_data["image search terms"]
                            page_search_terms = search_data["page search terms"]
                            for link_item in links_data[fname][topic][google_search_terms]:
                                url = link_item['link']
                                results_texts, results_image_links = [], []
                                f_results_texts, f_results_image_links = scrape_url_for_terms(url, page_search_terms,
                                                                                              image_search_terms,
                                                                                              results_texts,
                                                                                              results_image_links)
                                text_search_terms = dict()
                                text_search_terms[topic] = dict()
                                text_search_terms[topic][google_search_terms] = dict()
                                text_search_terms[topic][google_search_terms][url] = dict([
                                    ("title", link_item["title"]),
                                    ("text", link_item["text"]),
                                    ("google search terms", search_data["google search terms"]),
                                    ("image search terms", search_data["image search terms"]),
                                    ("page search terms", search_data["page search terms"]),
                                    ("page_text_snippets", f_results_texts),
                                    ("image_links", f_results_image_links)])
                                url = url.replace("/", "_").replace(":", "_").replace(".", "_")
                                print(text_search_terms)
                                with open(
                                        os.path.join(text_snippets_folder, f"{fname}_{google_search_terms}_{url}.json"),
                                        'w') as f:
                                    json.dump(text_search_terms, f, indent=2)


# Is it necessary to close session?

# Main script
if __name__ == '__main__':
    search_folder = 'search'
    links_search_folder = 'links_search'
    text_snippets_folder = 'text_snippets'
    for filename in os.listdir(search_folder):
        if filename.endswith('.json'):
            with open(os.path.join(search_folder, filename), 'r') as file:
                data = json.load(file)
                topics = data.get('topics', [])
                search_terms = data.get('google search terms', [])
                google_search(filename, topics, search_terms)
                get_search_content()
