from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.voanews.com/a/trump-offers-contradictory-explanation-for-comey-firing/4417821.html'
html_doc = urlopen(url)
soup = BeautifulSoup(html_doc, "html.parser")

print(soup)

print("tile", soup.title)

