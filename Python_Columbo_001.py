#
#
#
from bs4 import BeautifulSoup
import requests

import pandas as pd

url = r"https://en.wikipedia.org/wiki/List_of_Columbo_episodes"

res = requests.get(url, verify = False)

soup = BeautifulSoup(res.text, 'lxml')

#mymatch = soup.find("table", class_ = 'wikitable plainrowheaders')

mymatch = soup.find("table", class_ = 'wikitable plainrowheaders')

print(mymatch)


#print(soup.prettify())
i = 0
for item in table.find_all("tr")[:-1]:
    i+=1
    print(i, item.text)
