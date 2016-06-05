""" Methods for Regex Operations """
import re

def get_ncl(link):
	"""Method to extract ncl value of a story"""
	ncl_string = re.findall("ncl=.*?&",link)
	if ncl_string:
		return ncl_string[0][4:-1]
	else:
		return ''
