import asyncrequest
import feedparser
import logging

import article
import database

class NewsFeed:
    def __init__(self, name: str, rss_url: str):
        self.name = name
        self.rss_url = rss_url
        self.articles = []

    def process(self):
        """ Do everything required to parse and store all new or updated BBC articles """
        self._read_rss()
        self._read_articles()
        self._store_articles()

    def _read_rss(self):
        """ Fetch and parse the site's RSS page
        
        Returns a list of articles to check
        """
        d = feedparser.parse(self.rss_url)

        data = {
            'title': d.feed.get("title"),
            'published': d.feed.get("published_parsed"),
            'updated': d.feed.get("updated_parsed")
        }

        # Create articles from the RSS feed
        for entry in d.entries:
            article_data = {
                'published_time': entry['published_parsed'],
                'title': entry['title'],
                'summary': entry['summary'],
                'url': entry['link'],
                'host_site': self.name
            }
            a = article.Article(**article_data)
            self.articles.append(a)

    def _read_articles(self):
        """ Read the articles in parallel using async/io - sequential takes way too much time """

        # task collector
        areq = asyncrequest.AsyncRequest()

        # add tasks to run
        for article in self.articles:
            article.read(areq)

        # run all tasks in parallel
        areq.run()

        logging.debug("All tasks done")

    def _store_articles(self):
        """ Save the articles to database for later searching """
        d = database.Database()
        for article in self.articles:
            logging.debug("Saving article %s" % article.title)
            d.save_article(article)
        d.close_connection()
