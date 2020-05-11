import requests
from bs4 import BeautifulSoup
import json
import time
import re

####
# this is to gather all the URLs for the individual item pages
# and dump them in a json
####

all_urls = []
# this advances the page # in the for loop below
item_counter = 1

# 498 products, defaults to 24 per page, so will need to loop through 21 pages
total_pages = range(0,21)

# this is a regex to help me identify just the link portion of the a tags
# ok i think i don't actually need this but i'm scared to remove it bc it worked
url_pattern = re.compile(r'/([a-z]*-){1,5}[a-z]*')

# for every page in the total of 21 pages ...
for page_number in total_pages:

	url = 'https://www.seedsavers.org/department/vegetable-seeds?page='

	# add 1 page on every loop
	url = url + str(item_counter)

	#print("Working on... ",url)

	page_request_results = requests.get(url)

	page_html = page_request_results.text

	soup = BeautifulSoup(page_html, "html.parser")

	# is this the right place to add 1 to the item_counter to advance the page #? is there a better spot?
	item_counter = item_counter+1

	# each url is in an a tag with a specific class. thank you for doing it like this, site
	all_as = soup.find_all("a", attrs = {'class':'facets-item-cell-grid-title'})


	# loop through each item in the dictionary? all_as, turn it into text instead of a beautifulsoup object.
	for a_link in all_as:
		make_it_text = a_link.text
		just_url = url_pattern.findall(make_it_text)

		# accessing the link by attribute href
		url = a_link['href']
		url = "https://www.seedsavers.org" + url
		all_urls.append(url)

		json.dump(all_urls, open('all_urls.json','w'), indent=2)

#this section is taking the all_urls list and scraping each! one! of! them! boys!
#for each_link in all_urls:
#	url = url + str(item_counter)

#	print("Working on... ",url)

#	page_request_results = requests.get(url)

#	page_html = page_request_results.text

#	soup = BeautifulSoup(page_html, "html.parser")

#	name = soup.find_all("a", attrs = {'class':'facets-item-cell-grid-title'})

#	print(name)

	# setting up a blank dictionary to store info about each item. need to set up each variable too
	#item = {
	#	"name": name,
	#	"characteristics": characteristics,
	#	"description" : description,
	#	"url" : link
#	}
