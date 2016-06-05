from scrapping_methods import get_rss_link, get_rtc_links, get_see_all_link
from regex_ops import get_ncl
from feed_entries import get_feed_entries
from article_text import get_article_text
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client.crowdvoyant
subscription = db.subscription.find()
for subs in subscription:
	rtc_links = get_rtc_links(subs["link"])
	print(rtc_links)
	for link in rtc_links:
		ncl = get_ncl(link)
		if db.stories.find({"ncl": ncl}).count()==0:
			rss_link = get_rss_link(get_see_all_link(link))
			db.stories.insert_one({
				"ncl": ncl,
				"link": rss_link
				})
			print("Added story : "+rss_link)
stories = db.stories.find()

for story in stories:
	entries = get_feed_entries(story["link"])
	for entry in entries:
		if db.articles.find({"link": entry}).count() == 0:
			print("Adding article : "+entry)
			text = get_article_text(entry)
			db.articles.insert_one({
				"link": entry,
				"text": text
				})
			print("Added article")
