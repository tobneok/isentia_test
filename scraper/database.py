"""
Database middleware
"""

from pymongo import MongoClient
import yaml

class Database:
    def __init__(self):
        self.client = None
        self.db = None
        self.open_connection()

    def open_connection(self):
        cfg = yaml.safe_load(open('config.yaml'))
        mongo = cfg['mongo']
        s = 'mongodb+srv://{user}:{pass}@{cluster}/test?retryWrites=true&w=majority'.format(**mongo)
        self.client = MongoClient(s)
        self.db = self.client.test

    def close_connection(self): # in case we want to close the connection before the Database object dies
        self.client.close()

    def save_article(self, article):
        """ Saves an Article object """
        if not self.db:
            self.open_connection()

        collection = self.db.articles
        article_data = article.as_dict()
        collection.insert(article_data)
