import newsfeed

# bbc = newsfeed.NewsFeed('BBC', 'http://feeds.bbci.co.uk/news/rss.xml')
# bbc.process()


smh = newsfeed.NewsFeed('Sydney Morning Herald', 'https://www.smh.com.au/rss/feed.xml')
smh.process()

