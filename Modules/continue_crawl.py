# Implement the continue_crawl function described below: 

"""
search_history is a list of strings which are the urls of Wikipedia articles. The last item in the list most recently found url.

target_url is a string, the url of the article that the search should stop at if it is found.

continue_crawlshould return True or False following these rules:

if the most recent article in the search_history is the target article the search should stop and the function should return False

If the list is more than 25 urls long, the function should return False

If the list has a cycle in it, the function should return False

otherwise the search should continue and the function should return True.

"""


def continue_crawl(search_history, target_url):
    if search_history[-1] == target_url:
        return False
    elif len(search_history)>25:
        return False
    elif search_history[-1] in search_history[:-1]:
        return False
    else: 
        return True




