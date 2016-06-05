""" Methods for Regex Operations """
import re

def get_ncl(link):
	"""Method to extract ncl value of a story"""
	ncl_string = re.findall("ncl=.*?&",link)
	if ncl_string:
		return ncl_string[0][4:-1]
	else:
		return ''

def get_article_link(link):
	"""Method to extract article link from google news feed entry url"""
	article_link = re.findall("url=.*",link)
	if article_link:
		return article_link[0][4:]
	else:
		return ''
