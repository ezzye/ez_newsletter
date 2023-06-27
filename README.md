# ez_newsletter

A python script to take a folder of search items about a general topic then generate a file web links of pages 
containing information. Then to use those page links and image links to generate a newsletter. Which is the shared on google drive.


## Scrape test snippets and image links from pages

Write a python function to take a `url` and `page search terms`  and scrape the url page for text snippets.
It should use python library `BeautifulSoup` to parse the page and extract all the text snippets.
It should use code similar to example code below to extract a list of text snippets from the page.
```python
markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'
soup = BeautifulSoup(markup, 'html.parser')
[text for text in soup.stripped_strings]
```
It should then join the text snippets together with a '|' between them to make strings of text bigger than 1000 characters,
if possible, but less than 2000 characters.

It should then filter the resulting strings and only include a string in the results list of strings if it contains at least one
of the list of `page search terms` from the function parameters.

It should return a result list of strings.

Write a python function to take a `url` and `image search terms`  and scrape the url page for image links.
It should use python library `BeautifulSoup` or a similar library to parse the page and extract all the image links.
It should return a result list of image links. Consider image tags also consider alt text and text 50 characters 
before and after the image link when filtering by `image search terms`.

Write a python function to take a `url` and `page search terms`  and scrape the url page for web links.
It should use python library `BeautifulSoup` or a similar library to parse the web links on the page.
It should return two lists, one of same domain links and one of different domain links.




markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'
soup = BeautifulSoup(markup, 'html.parser')

soup.get_text()
'\nI linked to example.com\n'
soup.i.get_text()
'example.com'
You can specify a string to be used to join the bits of text together:

# soup.get_text("|")
'\nI linked to |example.com|\n'
You can tell Beautiful Soup to strip whitespace from the beginning and end of each bit of text:

# soup.get_text("|", strip=True)
'I linked to|example.com'
But at that point you might want to use the .stripped_strings generator instead, and process the text yourself:

[text for text in soup.stripped_strings]
# ['I linked to', 'example.com']








## Print Google Search Results
Write a python script to take a files from folder called `search` that contains json files.

Each json file should contain a list of topics and search terms.
The script should use Google search for each `google search term` `topic` combination and print results page from the
first 5 search results pages.
It should ignore the "image search terms" and "page search terms" in the json file.

GET Request should be like Google Chrome Example
The following is an example of a GET request like Google Chrome:

GET Request of Google Chrome Example
GET /echo HTTP/1.1
Host: reqbin.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36
Upgrade-Insecure-Requests: 1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate

The script should make fewer than 7 request per minute at random intervals of less than one every 3 seconds.

Then it print result pages for each combination of `topics` and `google search terms`.

Example of an input json file (`marc_bolan.json`) with ``` in `search` folder:
```json
{
    "topics": ["topic1", "topic2"],
    "google search terms": ["search term1", "search term2"],
    "image search terms": ["image search term1", "image search term2"],
    "page search terms": ["page search term1", "page search term2"]
}
```
## Extract web links from Google Search Results
Write a python function to take web page source code as a parameter and extract the web links and corresponding text from the page.
It should return the results as a dictionary with the following format.

```python
[
    {
        "link": "https://www.example.com",
        "text": "Example related text"
    },
    {
        "link": "https://www.example2.com",
        "text": "Example2 related text"
    }
]
```

## Output Search Results as a JSON file for  each `search_json_file_name` file in `search` folder
Write a python function to take a parameters an input file name(without extension), topic, search term, page number, results dictionary
for a search term and append results to a dictionary.
The dictionary returned should have the following format:
```python
{
  "file name": {
    "topic1": {
      "search term1": [
        {
          "link": "https://www.example.com",
          "text": "Example related text"
        },
        {
          "link": "https://www.example2.com",
          "text": "Example2 related text"
        }
      ],
      "search term2": [
        {
          "link": "https://www.example.com",
          "text": "Example related text"
        },
        {
          "link": "https://www.example2.com",
          "text": "Example2 related text"
        }
      ]
    }
  },
  "topic2": {
    "search term1": [
      {
        "link": "https://www.example.com",
        "text": "Example related text"
      },
      {
        "link": "https://www.example2.com",
        "text": "Example2 related text"
      }
    ],
    "search term2": [
      {
        "link": "https://www.example.com",
        "text": "Example related text"
      },
      {
        "link": "https://www.example2.com",
        "text": "Example2 related text"
      }
    ]
  }
}
```
The input results dictionary dict has the following format:
```python
[
    {
        "link": "https://www.example.com",
        "text": "Example related text"
    },
    {
        "link": "https://www.example2.com",
        "text": "Example2 related text"
    }
]
```







and output a json to `google_results` folder.
In the output file the `image links` and `text snippets` should be empty lists.
in to `google_results` folder for each `search_json_file_name` file in `search` folder.  The file should have the same
file name as the original file in the `search` folder.
Ignore `Sponsored` links and `People also ask` links.
Example of a result file `marc_boylan.json` in the `google_results` folder a sample few example `topic` and `google search term` combinations:
```json
{
  "marc_bolan.json": {
    "topic1": {
      "search term1": {
        "page search term1": {
          "page link1": {
            "image links": [
            ],
            "text snippets": [
            ]
          },
          "page link2": {
            "image links": [
            ],
            "text snippets": [
            ]
          }
        },
        "page search term2": {
          "page link1": {
            "image links": [
            ],
            "text snippets": [
            ]
          },
          "page link2": {
            "image links": [
            ],
            "text snippets": [
            ]
          }
        }
      },
      "search term2": {
        "page search term1": {
          "page link1": {
            "image links": [
            ],
            "text snippets": [
            ]
          },
          "page link2": {
            "image links": [
            ],
            "text snippets": [
            ]
          }
        },
        "page search term2": {
          "page link1": {
            "image links": [
            ],
            "text snippets": [
            ]
          },
          "page link2": {
            "image links": [
            ],
            "text snippets": [
            ]
          }
        }
      }
    }
  },
  "topic2": {
    "search term1": {
      "page search term1": {
        "page link1": {
          "image links": [
          ],
          "text snippets": [
          ]
        },
        "page link2": {
          "image links": [
          ],
          "text snippets": [
          ]
        }
      },
      "page search term2": {
        "page link1": {
          "image links": [
          ],
          "text snippets": [
          ]
        }
      }
    }
  }
}
```




## Get Topic Content
Write a python script to take a folder of lists of search items about a topic, searches google for each. 
Then it outputs to a file listing web links and image links relating of `pages of interest`.

To decide if a page is of interest the script needs to scrape the text and image content from the page in google search result
and see if it contains half of the `page search terms` for deciding page is of interest 
and any `image search terms` for images of interest.

The input to the script should be the contents a folder called `search`. The folder should contain json files.
Each json file should contain, a list of `topics`, a list of `google search terms`, `image search terms` 
and a list of `page search terms`.

Example of a json file in `search` folder:
```json
{
    "topics": ["topic1", "topic2"],
    "google search terms": ["search term1", "search term2"],
    "image search terms": ["image search term1", "image search term2"],
    "page search terms": ["page search term1", "page search term2"]
}
```

The output of the script should be a file called `links.json` in the `search` folder.
Each page link should have a list of image links and a list of text snippets from web page.

Example of `links.json`:
```json
{
  "search_json_file_name": {
    "topic1": {
      "search term1": {
        "page search term1": {
          "page link1": {
            "image links": [
              "image link1",
              "image link2"
            ],
            "text snippets": [
              "text snippet1",
              "text snippet2"
            ]
          },
          "page link2": {
            "image links": [
              "image link1",
              "image link2"
            ],
            "text snippets": [
              "text snippet1",
              "text snippet2"
            ]
          }
        },
        "page search term2": {
          "page link1": {
            "image links": [
              "image link1",
              "image link2"
            ],
            "text snippets": [
              "text snippet1",
              "text snippet2"
            ]
          },
          "page link2": {
            "image links": [
              "image link1",
              "image link2"
            ],
            "text snippets": [
              "text snippet1",
              "text snippet2"
            ]
          }
        }
      },
      "search term2": {
        "page search term1": {
          "page link1": {
            "image links": [
              "image link1",
              "image link2"
            ],
            "text snippets": [
              "text snippet1",
              "text snippet2"
            ]
          },
          "page link2": {
            "image links": [
              "image link1",
              "image link2"
            ],
            "text snippets": [
              "text snippet1",
              "text snippet2"
            ]
          }
        },
        "page search term2": {
          "page link1": {
            "image links": [
              "image link1",
              "image link2"
            ],
            "text snippets": [
              "text snippet1",
              "text snippet2"
            ]
          },
          "page link2": {
            "image links": [
              "image link1",
              "image link2"
            ],
            "text snippets": [
              "text snippet1",
              "text snippet2"
            ]
          }
        }
      }
    }
  },
  "topic2": {
    "search term1": {
      "page search term1": {
        "page link1": {
          "image links": [
            "image link1",
            "image link2"
          ],
          "text snippets": [
            "text snippet1",
            "text snippet2"
          ]
        },
        "page link2": {
          "image links": [
            "image link1",
            "image link2"
          ],
          "text snippets": [
            "text snippet1",
            "text snippet2"
          ]
        }
      },
      "page search term2": {
        "page link1": {
          "image links": [
            "image link1",
            "image link2"
          ],
          "text snippets": [
            "text snippet1",
            "text snippet2"
          ]
        }
      }
    }
  }
}
```

