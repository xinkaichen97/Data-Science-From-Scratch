from collections import Counter

import requests
from bs4 import BeautifulSoup
import json
from dateutil.parser import parse
from twython import Twython

"""
html = requests.get("https://www.google.com").text
soup = BeautifulSoup(html, 'html5lib')

first_paragraph = soup.find('p')
first_paragraph_text = soup.p.text
first_paragraph_words = soup.p.text.split()
# print(first_paragraph_text)
# first_paragraph_id = soup.p['id']  # raises KeyError if no 'id'
# first_paragraph_id2 = soup.p.get('id')  # returns None if no 'id'

all_paragraphs = soup.find_all('p')  # or just soup('p')
print(all_paragraphs)

important_paragraphs = soup('p', {'class' : 'important'})
print(important_paragraphs)
"""

url = "http://shop.oreilly.com/category/browse-subjects/data.do?sortby=publicationDate&page=1"
soup = BeautifulSoup(requests.get(url).text, 'html5lib')
tds = soup('span', 'orm-Icon-title')
print(len(tds))

serialized = """{ "title" : "Data Science Book",
"author" : "Joel Grus",
"publicationYear" : 2014,
"topics" : [ "data", "science", "data science"] }"""
# parse the JSON to create a Python dict
deserialized = json.loads(serialized)
if 'data science' in deserialized['topics']:
    print(deserialized['topics'])

endpoint = "https://api.github.com/users/joelgrus/repos"
repos = json.loads(requests.get(endpoint).text)
print(repos)

dates = [parse(repo["created_at"]) for repo in repos]
month_counts = Counter(date.month for date in dates)
weekday_counts = Counter(date.weekday() for date in dates)
print(month_counts)
print(weekday_counts)
last_5_repositories = sorted(repos, key=lambda r: r["created_at"], reverse=True)[:5]
last_5_languages = [repo["language"] for repo in last_5_repositories]
print(last_5_repositories)
print(last_5_languages)


