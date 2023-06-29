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

## Remove Duplicate Links and text snippets

Write a python scrip to take a list of links and text snippets and remove duplicate links and text snippets.
Example list of links:
```python
['https://d2kdkfqxnvpuu9.cloudfront.net/images/giant/57441.jpg?1367511669',
 'https://d2kdkfqxnvpuu9.cloudfront.net/images/giant/56881.jpg?1367137806',
 'https://d2kdkfqxnvpuu9.cloudfront.net/images/giant/57021.jpg',
 'https://d2kdkfqxnvpuu9.cloudfront.net/images/thumb/57061.jpg',
 'https://d2kdkfqxnvpuu9.cloudfront.net/images/thumb/57051.jpg',
 'https://d2kdkfqxnvpuu9.cloudfront.net/images/thumb/57081.jpg',
 'https://d2kdkfqxnvpuu9.cloudfront.net/images/thumb/57061.jpg',
 'https://d2kdkfqxnvpuu9.cloudfront.net/images/thumb/57051.jpg']
```
The text snippets are the text are in a list of strings consisting of snippets joined by `|` character.
Example list of strings made up of text snippets joined with `|` characters:
```python
[
    "Marc Bolan : London Remembers, Aiming to capture all memorials in London|London Remembers|Memorials|Subjects|Map|This Day|MENU|Memorials|Subjects|Map|Lost Memorials|Puzzle Corner|Memorial Types|Subject Types|About|Advanced search|Contact|Home|/|Subjects|/|People|/|Marc Bolan|Search|London|Remembers…|Person||\xa0Male\xa0\n  \t\t\t\tBorn\n  \t\t\t\t30/9/1947\xa0\n  \t\t\t\n  \t\t\t\tDied\n  \t\t\t\t16/9/1977|Marc Bolan|Categories:|Music / songs|Picture source: fendersixstring.blogspot.co.uk|Singer and guitarist in his band|T.Rex|. Born as Mark Feld at Hackney General Hospital on 30th September 1947 and grew up at 25 Stoke Newington Common. As a young teenager worked on the counter at the|2I’s coffee bar|. Died in a car-crash on Barnes Common. After a night out his girlfriend, Gloria Jones, driving a purple mini home to 142 Upper Richmond Road West, crashed into a tree. Bolan died in the crash; Jones was injured but survived.|Londonist|have photos and a map showing Bolan's life in London.|View from the Mirror|has a tribute with photos and videos.|This section lists the memorials where the subject on this page is commemorated:|Marc Bolan|Commemorated at|i|Marc Bolan - N16|He was here for his first 15 years.|Read More|Marc Bolan shrine - bust|Unveiled by Rolan Bolan, Marc's son,\xa0to commemorate the\xa025th anniversary of B...|Read More|Marc Bolan shrine - noticeboard|Other|Read More|Marc Bolan shrine - plaque - TAG|These steps were laid on January 9th &amp; 10th 2000 by TAG (T-Rex Action Gro...|Read More|Marc Bolan shrine - PRS|In Respectful memory of\xa0Marc Bolan, 30th September 1947 - 16th September 1977...|Read More|Show all 6|See other memorials in this area|Other Subjects|Mrs Jemima Luke|Writer of hymns and religious studies. Born Jemima Thompson in Islington. She planned to do missionary work in India, but illness prevented her from doing so. She married the Reverend Samuel Luke, ...|Person|,|Literature|,|Music / songs|,|Religion|1 memorial|Rev. John Newton|A slave-trader turned preacher and abolitionist. \xa0Born Wapping. \xa0Began his ecclesiastical career at\xa0Olney in Buckinghamshire where he wrote the words to 'Amazing Grace' and published the hymn in a ...",
    "Marc Bolan shrine - bust : London Remembers, Aiming to capture all memorials in London|London Remembers|Memorials|Subjects|Map|This Day|MENU|Memorials|Subjects|Map|Lost Memorials|Puzzle Corner|Memorial Types|Subject Types|About|Advanced search|Contact|Home|/|Memorials|/|Busts|/|Marc Bolan shrine - bust|Search|London|Remembers…|Bust|Marc Bolan shrine - bust|Erection date: 13/9/2002|Inscription|{On the front of the plinth:}|Marc Bolan, 25th anniversary 16th September 2002.|Sad to see them mourning you when you are here within the flowers and the trees.|Donated to TAG by Fee Warner.|Unveiled by Rolan Bolan, Marc's son,\xa0to commemorate the\xa025th anniversary of Bolan's death.  Paid for personally by Fee Warner.|Site: Marc Bolan shrine (10 memorials)|SW13, Queen's Ride|This site\xa0has evolved over the years from flowers place around the tree to become the shrine that it is today. \xa0The steps were probably introduced to give visitors somewhere safe to stand, off the busy road. \xa0Opposite the tree a sturdy notice board has been erected on which fans can attach their drawings, personal messages, etc. \xa0The bust, in 2013, has been wrapped in a black feather boa with some purple tinsel, and decorated with a few white swans at the front.|The risers of the steps provide space for small brass plaques - memorials for people related to Bolan, such as members of T Rex. \xa0Plaques for\xa0Took, Currie, June Bolan, Finn and TAG are all on the top riser.\xa0 Dines occupies the first plaque space on the next riser down.|More photos and information at|Flickering Lamps|.|This section lists the subjects commemorated on the memorial on this page:|Marc Bolan shrine - bust|Subjects commemorated|i|Marc Bolan|Singer and guitarist in his band T.Rex. Born as Mark Feld at Hackney General ...|Read More|This section lists the subjects who helped to create/erect the memorial on this page:|Marc Bolan shrine - bust|Created by|i|TAG (T-Rex Action Group)|TAG is the legal leaseholder of the site of the Marc Bolan Shrine. \xa0They arra...",
    "Marc Bolan shrine - noticeboard : London Remembers, Aiming to capture all memorials in London|London Remembers|Memorials|Subjects|Map|This Day|MENU|Memorials|Subjects|Map|Lost Memorials|Puzzle Corner|Memorial Types|Subject Types|About|Advanced search|Contact|Home|/|Memorials|/|Others|/|Marc Bolan shrine - noticeboard|Search|London|Remembers…|Other|Marc Bolan shrine - noticeboard|Site: Marc Bolan shrine (10 memorials)|SW13, Queen's Ride|This site\xa0has evolved over the years from flowers place around the tree to become the shrine that it is today. \xa0The steps were probably introduced to give visitors somewhere safe to stand, off the busy road. \xa0Opposite the tree a sturdy notice board has been erected on which fans can attach their drawings, personal messages, etc. \xa0The bust, in 2013, has been wrapped in a black feather boa with some purple tinsel, and decorated with a few white swans at the front.|The risers of the steps provide space for small brass plaques - memorials for people related to Bolan, such as members of T Rex. \xa0Plaques for\xa0Took, Currie, June Bolan, Finn and TAG are all on the top riser.\xa0 Dines occupies the first plaque space on the next riser down.|More photos and information at|Flickering Lamps|.|This section lists the subjects commemorated on the memorial on this page:|Marc Bolan shrine - noticeboard|Subjects commemorated|i|Marc Bolan|Singer and guitarist in his band T.Rex. Born as Mark Feld at Hackney General ...|Read More|This section lists the other memorials at the same location as the memorial on this page:|Marc Bolan shrine - noticeboard|Also at this site|i|Marc Bolan shrine - bust|Unveiled by Rolan Bolan, Marc's son,\xa0to commemorate the\xa025th anniversary of B...|Read More|Marc Bolan shrine - plaque - Currie|Steve Currie, 20th May 1947 - 28th April 1981.  Original bassist with T-Rex. ...|Read More|Marc Bolan shrine - plaque - Dines|Peter (Dino) Dines, Dec. 17th 1944 - 28th Jan. 2004.  Keyboards.  A member of...|Read More|Marc Bolan shrine - plaque - Finn",
]
```
The python script should output list of snippets.







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

