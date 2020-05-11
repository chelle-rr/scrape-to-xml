import requests
from bs4 import BeautifulSoup
import json
import time
import re
import csv


####
# this opens the json with all urls and scrapes each one
####

#DONT FORGET TO CHANGE THIS TEST JSON!!!
with open("all_urls.json","r") as all_urls:
	items = json.load(all_urls)

item_details = []


for each_item in items:

	url = each_item

	page_request_results = requests.get(url)

	page_html = page_request_results.text

	soup = BeautifulSoup(page_html, "html.parser")

	####
	# this section is to set up a variable for each thing i want to pull out ...
	####

	# get the item name
	#name_element = soup.find_all("h1", attrs = {'class':'item-details-content-header-title'})
	# this gives me something that looks like this:
	#[<h1 class="item-details-content-header-title" itemprop="name">Peking Ta Ching Kou Pai Tsai Asian Green</h1>]
	# this is a beautifulsoup object, so i can do beautifulsoup stuff with it
	# ^^turns out all of that is not necessary because the name happens to be the only h1 on the page!
	name = soup.h1.string

	# and the characterstics (multiple, so need to loop)
	characteristics_element = soup.find_all("div", attrs = {'class': 'item-characteristics'})
	for each_characteristic in characteristics_element:
		all_li_el_in_div = each_characteristic.find_all('li')
		# not sure what this does so commmenting it out for now. stops short of the last item? i think i need it for mine?
		#creator_stmts_li = all_li_el_in_div[0:-1]
		characteristics = []
		for li_el in all_li_el_in_div:
			characteristics.append(li_el.text)
		# now each characteristics list has several characteristics, ie ['thing', 'thing']
		# these characteristics are currently not distinguished by type bc they vary a bit from item to items

	# whether or not it's a historic variety
	historic_element = soup.find_all("p", attrs = {'class': 'pdp-historic-distinction'})
	for historic_info in historic_element:
		historic_variety = historic_info.text

	# the description
	description_element = soup.find_all("div", attrs = {'class': 'store-detailed-description'})
	for description_info in description_element:
		description = description_info.text

	# planting info
	#for literally_everything in soup:
	seed_distance = "N/A"
	seed_distance_bs = soup.find("p", text=re.compile("Direct Seed:"))
	if seed_distance_bs:
		for thing in seed_distance_bs:
			seed_distance = (seed_distance_bs.text).replace("Direct Seed: ","")

	seed_depth = "N/A"
	seed_depth_bs = soup.find("p", text=re.compile("Seed Depth:"))
	if seed_depth_bs:
		for thing in seed_depth_bs:
			seed_depth = (seed_depth_bs.text).replace("Seed Depth: ","")

	germination = "N/A"
	germination_bs = soup.find("p", text=re.compile("Germination:"))
	if germination_bs:
		for thing in germination_bs:
			germination = (germination_bs.text).replace("Germination: ","")

	thin = "N/A"
	thin_bs = soup.find("p", text=re.compile("Thin:"))
	if thin_bs:
		for thing in thin_bs:
			thin = (thin_bs.text).replace("Thin: ","")

	start_indoors = "N/A"
	start_indoors_bs = soup.find("p", text=re.compile("Start Indoors:"))
	if start_indoors_bs:
		for thing in start_indoors_bs:
			start_indoors = (start_indoors_bs.text).replace("Start Indoors: ","")

	plant_outdoors = "N/A"
	plant_outdoors_bs = soup.find("p", text=re.compile("Plant Outdoors:"))
	if plant_outdoors_bs:
		for thing in plant_outdoors_bs:
			plant_outdoors = (plant_outdoors_bs.text).replace("Plant Outdoors: ","")

	light = "N/A"
	light_bs = soup.find("p", text=re.compile("Light:"))
	if light_bs:
		for thing in light_bs:
			light = (light_bs.text).replace("Light: ","")

	# additional planting instructions
	instructions_element = soup.find_all("div", attrs = {'class': 'learn-to-grow-extra-details'})
	for instructions_info in instructions_element:
		instructions = instructions_info.text

	# setting up a blank dictionary to store info about each item. need to set up each variable too
	item_dict = {
		"name": name,
		"characteristics": characteristics,
		"historic variety": historic_variety,
		"description": description,
		"instructions": instructions,
		"seed distance": seed_distance,
		"seed depth": seed_depth,
		"germination": germination,
		"thin": thin,
		"start indoors": start_indoors,
		"plant outdoors": plant_outdoors,
		"light": light,
		"url": url
	}

	item_details.append(item_dict)
#

	json.dump(item_details, open('item_details.json','w'), indent=2)
