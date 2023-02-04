#
#
import os

from DefaultItems import DataFolder
from bs4 import BeautifulSoup
import lxml
import requests

my_url = "https://en.wikipedia.org/wiki/List_of_radio_soap_operas"

source = requests.get(my_url, verify=False).text

soup = BeautifulSoup(source, 'lxml')

print(soup.prettify())


#with open(my_url) as html_file:
#    soup = BeautifulSoup(html_file, 'lxml')




