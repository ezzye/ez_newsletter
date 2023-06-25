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
def google_search(topics, search_terms):
    for topic in topics:
        for term in search_terms:
            for i in range(1, 6):
                item = (i * 10) - 10
                url = f"https://www.google.com/search?q={topic}+{term}&start={item}&sourceid=chrome&ie=UTF-8"
                response = get_request(url)
                print("--------------------------------START-------------------------------------")
                print(parse_results(response))
                print("---------------------------------END------------------------------------")
                time.sleep(random.uniform(5, 15))  # Sleep to make fewer than 7 requests per minute
                # input file name, topic, search term, page number, and output results into a json file


def parse_results(response):
    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".VwiC3b"

    results = response.html.find(css_identifier_result)

    output = []

    for result in results:
        item = {
            'title': result.find(css_identifier_title, first=True).text,
            'link': result.find(css_identifier_link, first=True).attrs['href'],
            'text': result.find(css_identifier_text, first=True).text
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
            google_search(topics, search_terms)
