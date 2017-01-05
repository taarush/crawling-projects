import requests
from bs4 import BeautifulSoup
import urllib.request
import time

url = "https://www.github.com/trending"
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text,"lxml")
titles = []
descriptions = []
for title in soup.findAll('div',{'class':"d-inline-block col-9 mb-1"}):
	repo_title = title.text
	titles.append(repo_title)
for description in soup.findAll('p',{'class':"col-9 d-inline-block text-gray m-0 pr-4"}):
	repo_desc = description.string
	descriptions.append(repo_desc)

for n in range(24):
	title = str(n) + " " + str(titles[n])
	description = descriptions[n]
	print(title)
	print(description)

