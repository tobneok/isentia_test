import unittest

import article
import database

"""
Run tests with
nose2 -s .
"""

class TestDatabase(unittest.TestCase):
    def test_insert(self):
        a = article.Article('testurl', 'name', 'BBC')
        a.text = 'Some text'

        d = database.Database()
        d.save_article(a)
