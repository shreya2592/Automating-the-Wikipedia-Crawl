# download html of last article in article_chain
# find the first link in that html
# add the first link to article_chain
# delay for about two seconds

import requests
from bs4 import BeautifulSoup
import time 

def find_first_link(url):
    reponse= requests.get(url)
    html=reponse.text
    soup= bs4.BeautifulSoup(html, "html.parser")
    return soup.a

while continue_crawl(article_chain, target_url):
    first_link=find_first_link(article_chain[-1])
    article_chain.append(first_link)
    time.sleep(2)




    
