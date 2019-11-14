# Scraps repos from github. Features: argparse, urllib, BeautifulSoup, PrettyTable, try/except block
# Usage: python scrap3.py username

import argparse
import urllib.request
from bs4 import BeautifulSoup

from prettytable import PrettyTable
    

parser = argparse.ArgumentParser()
parser.add_argument("username", help="A github username. Example: 'heagueron'")
args = parser.parse_args()
username = args.username

x = PrettyTable()
x.field_names = ["Repo Name", "Description"]

# print(username)
repo_names = []
repo_descriptions = []
repos = {}

def get_repos(url):
    soup = BeautifulSoup(url, features="html.parser")
    # print(soup)
    
    for repo in soup.select('li[itemprop="owns"]'):
        repo_name = repo.div.div.h3.a.get_text().lower().strip()
        repo_names.append(repo_name)

    for desc in soup.select('p[itemprop="description"]'):
        desc_name = desc.get_text().lower().strip()
        repo_descriptions.append(desc_name)

    # print(repo_names, repo_descriptions)
    print(f"\n\tGithub repositories for: {username}\n")
    # print(f"\n\tNAME\t\t\t\tDESCRIPTION\n")
    # print(f"\n\t----\t\t\t\t-----------\n")
   
    for (name,desc) in zip(repo_names, repo_descriptions):
        repos[name] = desc
    #     print(f"\n\tNAME\t\t\t\tDESCRIPTION")
    #     print(f"\t{repos[name]}\t\t\t{repos[desc]}")
    
    # print(type(repos))
    # for key, value in repos.items():
    #     print(f"\t{repos[name]}\t\t\t{repos[desc]}")

    for name in repos:
        desc = repos.get(name)
        if desc:
            x.add_row([name, desc])
            #print(f"\t{name}\t\t\t{desc}")
        else:
            pass
            # print(f"{repo} is unknown.")
    print(x)

search = "https://github.com/" + username + "?tab=repositories"

try:
    url = urllib.request.urlopen(search)
    get_repos(url)    
except urllib.error.HTTPError as error:
    print(error)
    print( "User Not FOUND")
else:
    print("Executing the else clause.")

print("***** Thanks for using scrap3.py ***** ")





