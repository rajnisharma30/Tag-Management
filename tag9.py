#crawling of a web page fetching headings and subheadings
from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/Transhumanism'
# get contents from url
content = requests.get(url).content
# get soup
soup = BeautifulSoup(content, 'lxml')  # choose lxml parser
# find the tag : <div class="toc">
tag = soup.find('div', {'class': 'toc'})  # id="toc" also works
# get all the links
links = tag.findAll('a')  # <a href='/path/to/div'>topic</a>
# print them
for link in links:
    print(link.text)  # get text from <a>
