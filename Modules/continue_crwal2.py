"""
 Implementing the program - Part II

1. Change the max number 25 from hard coded value to a variable that can be changed in future. So replaced it with variable max_steps
2. Thus we add a new argument to the continue crwal function, i.e, max_steps and assign it some default value 
3. 

"""

def continue_crawl(search_history, target_url, max_steps=25):
    if search_history[-1] == target_url:
        print("We have found the target article!")
        return False
    elif len(search_history)>max_steps:
        print("The search has gone suspiciously long. Aborting Search.")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("We have arrived at an article we've already seen. Aborting search!!")
        return False
    else:
        return True

