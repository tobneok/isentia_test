
Isentia coding challenge

https://github.com/Isentia/Coding-Challenge/blob/master/Data-Engineer-Coding-Challenge.md

# Description

## Scraper

The folder 'scraper' contains the scraper and scraper unittests. It scrapes two sites: BBC and SMH.

The architecture is:
* The RSS feed of a site is read in module newsfeed.py
* From the feed, Article objects are created using module article.py
* The articles are all fetches in parallel (asynchronously)
* The articles' HTML pages are parsed and cleaned up
* The article metadata and text are stored in a hosted MongoDB running on an Atlas cluster, using the module database.py

Libraries used are:
* aiohttp for async requests
* feedparser for reading RSS feeds
* pymongo for querying a mongo database
* pyquery for parsing html
* re for cleaning html
* yaml for config file reading

## Server

The folder 'server' contains a very basic Flask server. The empty endpoint presents a form to enter a search keyword. This makes a POST to /search, which returns a list of JSON data with articles that have the requested keyword somewhere in the title or the text body.

For ease of use, you can also access /search directly via GET with a ?search parameter, e.g.

'''
GET /search?search=prince
'''

Libraries used are:
* flask
* gunicorn + gevent
* pymongo
* yaml


# Installation

The Python version used is 3.7.

Do not use Python lower than 3.5, as the asyncio / aiohttp libraries are relatively recent.

## Scraper

Run the following commands

```
cd scraper
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python scrape.py
```

For the articles to be saved to the database, a config.yaml file must be created with the database connection settings. Refer to config_example.yaml for the structure.

## Flask Server

Run the following commands

```
cd server
virtualenv env
source env/bin/activate
pip install -r requirements.txt
./run_gunicorn.sh
```

# Testing

Tests for the page parsing and database access (saving an article) are included.

To run the tests, do

```
cd server
virtualenv env
source env/bin/activate
nose2 -s .
```
