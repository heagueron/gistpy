import urllib.request
# urllib.request is a Python module for fetching URLs (Uniform Resource Locators).

from bs4 import BeautifulSoup
# Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree.

import re
# Python's regular expression library


counts = {}
frameworks = ['angular', 'react', 'vue', 'ember', 'meteor', 'mithril', 'node', 'polymer', 'aurelia', 'backbone'] 
max_pages = 100
ads_per_page = 10
max_ads = max_pages * ads_per_page 

for pageno in range(0,max_pages): 
    search = "https://www.indeed.com/jobs?q=javascript&l=New+York+City&start=" + str(10*pageno) 
    url = urllib.request.urlopen(search)
    soup = BeautifulSoup(url, features="html.parser")
    this_page_ad_counter = 0

    for adlink in soup.select('a[onmousedown*="return rclk(this,jobmap["]'):
        href = adlink['href']
        subURL  = "https://www.indeed.com" + href
        subSOUP = BeautifulSoup(urllib.request.urlopen(subURL), features="html.parser")
        ad_index = this_page_ad_counter + pageno*ads_per_page
        print("Scraping (" + str(ad_index + 1) + "/" + str(max_ads) + "): " + href + "...")
        this_page_ad_counter += 1

        for desc in subSOUP.select('div[class*="jobsearch-JobComponent-description"]'): 

            words = re.split("[ ,.:/?()\n\t\r]", desc.get_text().lower()) 
            for word in words:
                word = word.strip()
                if word.endswith("'s"):
                    word = word[:-2] 
                if word.endswith(".js"):
                    word = word[:-3]
                if word.endswith("js"):
                    word = word[:-2]
                if len(word) < 2:
                    continue
                if word not in frameworks:
                    continue
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1

word_freq = []
for key, value in counts.items():
    word_freq.append((value,key))

word_freq.sort(reverse=True)

print(counts)
    