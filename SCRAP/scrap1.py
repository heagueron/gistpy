import urllib.request
# urllib.request is a Python module for fetching URLs (Uniform Resource Locators).

from bs4 import BeautifulSoup
# Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree.

import re
# Python's regular expression library


counts = {}


for pageno in range(0,1): 
    search = "https://www.indeed.com/jobs?q=javascript&l=New+York+City&start=" + str(10*pageno) 
    url = urllib.request.urlopen(search)
    soup = BeautifulSoup(url, features="html.parser") 

    for adlink in soup.select('a[onmousedown*="return rclk(this,jobmap["]'):
        subURL  = "https://www.indeed.com" + adlink['href']
        subSOUP = BeautifulSoup(urllib.request.urlopen(subURL), features="html.parser")
        
        for desc in subSOUP.select('div[class*="jobsearch-JobComponent-description"]'): 
            #print(desc.get_text()[:50]) 
            """
            BeautifulSoup.select() returns the HTML / XML tags which match the 
            search parameters that we provide. We can pull attributes from those 
            tags with bracket notation (as in adlink['href']) and we can pull the 
            text contained within opening and closing tags (for instance, between 
            <p> and </p>) with get_text(), as we did above. The subSOUP.select() 
            statement returns a list of <div> tags, with class attributes that 
            contain the substring "jobsearch-JobComponent-description", then we 
            use a for ... in loop to get each <div> in that list (there's only one) 
            and print the text contained within <div> ... </div> with get_text().
            """            
            # words = desc.get_text().lower().split()[:50]
            # for word in words:
            #     print(word)
            words = re.split("[ ,.:/]", desc.get_text().lower())[:50]
            for word in words:
                word = word.strip()
                if word.endswith("'s"):
                    word = word[:-2] 
                if len(word) < 2:
                    continue
                #print(word)
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1

print(counts)
    