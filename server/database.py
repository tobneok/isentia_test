"""
Database middleware
"""

from pymongo import MongoClient
import re
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

    def search(self, query):
        """ Returns all data that contains the query """
        if not self.db:
            self.open_connection()

        search_expr = re.compile(f".*{query}.*", re.IGNORECASE)

        search_request = {
            '$or': [
                    {'title': {'$regex': search_expr}},
                    {'text': {'$regex': search_expr}}
            ]
        }

        collection = self.db.articles
        cursor = collection.find(search_request)

        results = []
        for result in cursor:
            results.append(result)
        
        return results
