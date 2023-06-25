#!/usr/bin/env python


import os
import json
import requests
import time
import random
from bs4 import BeautifulSoup
from requests_html import HTML
from requests_html import HTMLSession


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
    try:
        session = HTMLSession()
        web_response = session.get(url, headers=headers)
        # response = requests.get(url, headers=headers)

    except requests.exceptions.RequestException as e:
        print(e)
    return web_response


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


# Main script
folder = 'search'
for filename in os.listdir(folder):
    if filename.endswith('.json'):
        with open(os.path.join(folder, filename), 'r') as file:
            data = json.load(file)
            topics = data.get('topics', [])
            search_terms = data.get('google search terms', [])
            google_search(filename, topics, search_terms)
