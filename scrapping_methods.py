"""Methods for scrapping certain information from news.google.com"""

import urllib2
from bs4 import BeautifulSoup

def get_rss_link(url):
	"""Method to scrap RSS Link"""
        html = urllib2.urlopen(url).read()
        soup = BeautifulSoup(html)
        rss_link = soup.find('img','feed-icon').parent['href']
        return str(rss_link)

def get_rtc_links(url):
	"""Method to scrap RTC Links"""
	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html)
	links=[]
	rtc_links = soup.find_all('a','esc-fullcoverage-button')
	for link in rtc_links:
		links.append('http://news.google.com'+str(link['href']))
	return links

def get_see_all_link(url):
	"""Method to scrap SEE ALL ARTICLES Link"""
        html = urllib2.urlopen(url).read()
        soup = BeautifulSoup(html)
        link = soup.find('a','more-coverage-text')['href']
        return 'http://news.google.com'+str(link)

