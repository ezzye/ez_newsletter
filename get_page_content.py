#!/usr/bin/env python


from bs4 import BeautifulSoup
# import requests
import re
from urllib.parse import urlparse
from urllib.parse import urljoin
from get_search_results import get_request

visited_urls = []
level = 0
total_results_texts, total_results_image_links = [], []


def scrape_url_for_terms(url, page_search_terms, image_search_terms,
                         total_results_texts, total_results_image_links, level=0, domain=None):
    # add url to list of visited urls
    if url in visited_urls:
        return [], []
    else:
        visited_urls.append(url)

    in_results_texts, in_results_image_links = [], []
    ex_results_texts, ex_results_image_links = [], []

    if level == 0:
        domain = urlparse(url).netloc

    # Download the webpage
    response = get_request(url)
    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    results_texts = get_text_from_url(page_search_terms, soup)

    results_image_links = scrape_url_for_images(soup, image_search_terms)

    in_results_links, ex_results_links = scrape_url_for_links(soup, page_search_terms, domain)

    if level < 2:
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


page_url = "https://www.londonremembers.com/memorials/marc-bolan-n16"
page_search = ["marc", "bolan", "t rex", "Mark", "Feld"]
image_search = ["marc", "bolan", "t rex", "Mark", "Feld", "Rolan", "Bolan", "Newington", "dyslexia", "Glam Rock",
                "Jewish", "songwriter"]
output_text, output_image = scrape_url_for_terms(page_url, page_search, image_search, total_results_texts,
                                                 total_results_image_links)

output_text_snippets, output_images_deduped = remove_duplicates(output_image, output_text)

print(output_text_snippets)
print(output_images_deduped)
print(visited_urls)
