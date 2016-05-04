"""Method to get feed entry links"""
import feedparser

def get_feed_entries(url):
        """Method to get feed entry links"""
        doc = feedparser.parse(url)
        links = []
        for feed in doc.entries:
                links.append(str(feed.link))
        return links
