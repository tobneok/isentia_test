import logging
from pyquery import PyQuery as pq
import re

class Article:
    def __init__(self, url, title, host_site, summary="", published_time=None):
        self.url = url
        self.title = title
        self.summary = summary
        self.published_time = published_time
        self.host_site = host_site
        self.fetched_time = None
        self.text = None

    def as_dict(self):
        return {
            'url': self.url,
            'title': self.title,
            'summary': self.summary,
            'published_time': self.published_time,
            'host_site': self.host_site,
            'fetched_time': self.fetched_time,
            'text': self.text
        }

    def read(self, async_requester):
        """ Adds the article URL to the queue to read """
        async_requester.get_page(self.url, cb=self.parse)

    def parse(self, html):
        """ Parses the fetched page """
        logging.debug(f"Finished reading article {self.title}")
        if self.host_site == 'BBC':
            self.parse_bbc(html)
        elif self.host_site == 'Sydney Morning Herald':
            self.parse_smh(html)
        else:
            logging.error("Unknown host site: %s" % self.host_site)

    def parse_bbc(self, html):
        # Extract the article from the page
        page = pq(html)
        content = page(".story-body")
        text = pq(content).text()

        # Cut out advertisements. They are in a block like /**/ BLA /**/
        regex = re.compile(r"\/\*\*\/.*?\/\*\*\/", re.IGNORECASE | re.DOTALL)
        text = regex.sub('', text)

        self.text = text

    def parse_smh(self, html):
        pass
