"""Method to get article text"""
from newspaper import Article

def get_article_text(link):
    """Method to extract article text"""
    try:
        article = Article(link)
        article.download()
        article.parse()
    except:
        return None
    return article.text.encode("utf8")
