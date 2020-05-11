####
# this file takes my output .json from 2_scrape_individual_pages and converts it to xml so it can be used in a library catalog.
####

import json
import xml.etree.ElementTree as etree

with open("item_details.json") as json_file:
    item_details = json.load(json_file)

# set a root element for all items
root_element = etree.Element("item")

for each_item in item_details:
    # define first subelement
    etree.SubElement(root_element,"name").text = each_item["name"]

    # define second sublement, which has a list, so it needs to loooooooop
    for each_characteristic in each_item["characteristics"]:
        etree.SubElement(characteristics,"characteristic").text = each_characteristic

    # define a bunch of bland-ass subelements
    etree.SubElement(root_element,"historic variety").text = each_item["historic variety"]
    etree.SubElement(root_element,"description").text = each_item["description"]
    etree.SubElement(root_element,"instructions").text = each_item["instructions"]

    # this section needs if statements in case the items aren't present
    if "seed_distance" in each_item:
        etree.SubElement(root_element,"seed distance").text = each_item["seed_distance"]

    if "seed_depth" in each_item:
        etree.SubElement(root_element,"seed depth").text = (each_item["seed_depth"])

    if "germination" in each_item:
        etree.SubElement(root_element,"germination").text = (each_item["germination"])

    if "thin" in each_item:
        etree.SubElement(root_element,"thin").text = (each_item["thin"])

    if "start_indoors" in each_item:
        etree.SubElement(root_element,"start indoors").text = (each_item["start_indoors"])

    if "plant_outdoors" in each_item:
        etree.SubElement(root_element,"plant outdoors").text = (each_item["plant_outdoors"])

    if "light" in each_item:
        etree.SubElement(root_element,"light").text = (each_item["light"])

    etree.SubElement(root_element,"url").text = (each_item["url"])

# don't forget to ignore the ones with value 0, bc xml won't be able to deal with those

#write it out

a = etree.ElementTree(root_element)


#a.write("item_details_xml.xml")
