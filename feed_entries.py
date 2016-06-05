"""Method to get feed entry links"""
import feedparser

def get_feed_entries(url):
    """Method to get feed entry links"""
    links = []
    try:
        doc = feedparser.parse(url)
        for feed in doc.entries:
            links.append(str(feed.link))
    except:
        pass
    return links
