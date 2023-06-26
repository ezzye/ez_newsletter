#!/usr/bin/env python


from bs4 import BeautifulSoup
import requests
import re


def scrape_url_for_terms(url, page_search_terms):
    # Download the webpage
    response = requests.get(url)
    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract all text snippets
    all_text = [text for text in soup.stripped_strings]

    # Join the text snippets together with '|' to make strings of text bigger than 1000 characters,
    # if possible, but less than 2000 characters.
    combined_text = '|'.join(all_text)
    split_index = [m.start() for m in re.finditer('\|', combined_text)]
    split_index = [0] + [idx for idx in split_index if 1000 <= idx <= 2000] + [len(combined_text)]

    chunked_texts = [combined_text[split_index[i - 1]:split_index[i]] for i in range(1, len(split_index))]

    # Filter the resulting strings and only include a string in the results if it contains at least one
    # of the provided page search terms.
    results = [text for text in chunked_texts if any(term in text for term in page_search_terms)]

    return results


page = "https://www.londonremembers.com/memorials/marc-bolan-n16"
page_search = ["marc", "bolan", "t rex", "Mark", "Feld", "newington"]
output = scrape_url_for_terms(page, page_search)
print(output)

# need to also follow read more links
