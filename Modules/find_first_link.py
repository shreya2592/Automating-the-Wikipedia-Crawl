"""
    # get the HTML from "url", use the requests library
    # feed the HTML into Beautiful Soup
    # find the first link in the article
    # return the first link as a string, or return None if there is no link
"""

import requests
from bs4 import BeautifulSoup

def find_first_link(url):
    response=requests.get(url)
    html=response.text
    soup= BeautifulSoup(html,"html.parser")
    content_div= soup.find(id='mw-content-text').find(class_="mw-parser-output")
    for element in content_div.find_all("p", recurcive=False):
	if element.find("a",recurcive=False):
	    first_relative_link=element.find("a", recursive=False).get('href')
	    break

