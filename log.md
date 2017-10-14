### Day 1, 6th October'17

+ Worked on the basic structure for the crawler.
+ Designed the logic for the crawler.
+ Divided the project into 2 smaller modules. 

### Breaking the Problem into Steps

+ Open an article
+ Find the first link in the article
+ Follow the link
+ Record the link in the article_chain data structure.
+ Repeat this process until we reach the Philosophy article, or get stuck in an article cycle.

+ article_chain will be our program's output. 

### The program should end the while loop when:

+ we reach Philosophy,
+ we reach a page we've already visited, hence find ourselves in a cycle of articles (like the case of Chair,
+ we go on for too long (we think that 25 steps is plenty, but you can adjust this if you like), or
+ we find a page that has no links on it - we simply can't keep going in this case.

+ article_chain variable tracking which articles we've already visited. 

### Day 2: 7th October'2017

### Implementation- part I

+ search_history is a list of strings which are the urls of Wikipedia articles. The last item in the list most recently found url.
+ target_url is a string, the url of the article that the search should stop at if it is found.

+ continue_crawlshould return True or False following these rules:
+ if the most recent article in the search_history is the target article the search should stop and the function should return  False
+ If the list is more than 25 urls long, the function should return False
+ If the list has a cycle in it, the function should return False
+ otherwise the search should continue and the function should return True.


**Link to Work:** https://github.com/shreya2592/Automating-the-Wikipedia-Crawl/blob/master/Modules/continue_crawl.py

###  Implementing the program - Part II

+ Change the max number 25 from hard coded value to a variable that can be changed in future. So replaced it with variable max_steps
+ Thus we add a new argument to the continue crwal function, i.e, max_steps and assign it some default value 


**Link to Work:** https://github.com/shreya2592/Automating-the-Wikipedia-Crawl/blob/master/Modules/continue_crawl2.py


###  Implementing the program - Part III

+ Download html of last article in article_chain
+ Find the first link in that html
+ Add the first link to article_chain
+ Delay for about two seconds


**Link to Work:** https://github.com/shreya2592/Automating-the-Wikipedia-Crawl/blob/master/Modules/while_loop.py



###  Implementing the program - Part IV

 + get the HTML from "url", use the requests library
 + feed the HTML into Beautiful Soup
 + find the first link in the article
 + return the first link as a string, or return None if there is no link
 

**Link to Work:** https://github.com/shreya2592/Automating-the-Wikipedia-Crawl/blob/master/Modules/find_first_link.py




###  Final Program- putting it all together. 

+ Combine all the modules.
+ Check for errors. 
+ Run the code 

**Link to Work:** https://github.com/shreya2592/Automating-the-Wikipedia-Crawl/blob/master/Web_Crawler.py





