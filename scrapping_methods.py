"""Methods for scrapping certain information from news.google.com"""

import urllib2
from bs4 import BeautifulSoup

def get_rss_link(url):
	"""Method to scrap RSS Link"""
        try:
		html = urllib2.urlopen(url).read()
        	soup = BeautifulSoup(html)
        	rss_link = soup.find('img','feed-icon').parent['href']
        except:
		return ''
	return str(rss_link)

def get_rtc_links(url):
	"""Method to scrap RTC Links"""
	links=[]
	try:
		html = urllib2.urlopen(url).read()
		soup = BeautifulSoup(html)
		rtc_links = soup.find_all('a','esc-fullcoverage-button')
		for link in rtc_links:
			links.append('http://news.google.com'+str(link['href']))
	except:
		pass
	return links

def get_see_all_link(url):
	"""Method to scrap SEE ALL ARTICLES Link"""
        try:
		html = urllib2.urlopen(url).read()
        	soup = BeautifulSoup(html)
        	link = soup.find('a','more-coverage-text')['href']
        except:
		return ''
	return 'http://news.google.com'+str(link)

