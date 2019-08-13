import unittest

import article

"""
Run tests with
nose2 -s .
"""

class TestBBC(unittest.TestCase):
    def test_parse_bbc_article(self):
        with open('testdata/bbc_article.txt', 'r') as f:
            html = f.read()

        a = article.Article(None, None, 'BBC')
        a.parse(html)

        # Make sure that some text was found
        self.assertGreater(len(a.text), 500)

        # Make sure the ads / JS functions are removed
        self.assertNotIn('/**/', a.text)
