import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

web = 'https://www.pinnacle.com/en/baseball/matchups'
page = requests.get(web)
soup = BeautifulSoup(page.text, 'html.parser')
odds =[ soup.find_all('span', attrs = {'class' : 'style_price__15SlF'})]
print(odds)
