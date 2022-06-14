from tokenize import Name
import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
import time


web = 'https://sportsbook.draftkings.com/leagues/baseball/88670847'
page = requests.get(web)
from csv import writer
time.sleep(1)
soup = BeautifulSoup(page.content, 'html.parser')
odds = soup.find('tbody', class_='sportsbook-table__body')

with open('odds.csv', 'w', newline = '', encoding = 'utf8') as f :
    thewriter = writer(f)
    header = ['DraftKings', 'Team', 'Moneyline', 'Total', 'Run Line']
    sportsbook = 'DRAFTKINGS'
    thewriter.writerow(header)

    for odd in odds :
        name = odd.find('div', class_='event-cell__name-text').text.replace('\n', '')
        moneyline = odd.find('span', class_='sportsbook-odds american no-margin default-color').text.replace('\n', '')
        total1 = soup.find('div', class_='sportsbook-outcome-cell')
        for total2 in total1 :
            total = total2.find('span', class_='sportsbook-odds american default-color')
        runline = odd.find('span', class_='sportsbook-odds american default-color').text.replace('\n', '')
        info = [name, moneyline, total, runline]
        thewriter.writerow(info)
        #print(f'Team : {name.text}')
        #print(f'Moneyline : {moneyline.text}')
        #print(f'Total : {total.text}')
        #print(f'Run Line : {runline.text}')
        #print('-------------------------------------------------------------------------')

