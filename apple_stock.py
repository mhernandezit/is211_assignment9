from bs4 import BeautifulSoup
import pprint
import urllib.request

URL = 'https://www.nasdaq.com/symbol/aapl/historical'

with urllib.request.urlopen(URL) as data:
    pageData = BeautifulSoup(data, features="lxml")

appleStockData = {}

stockData = pageData.find("div", class_="genTable")
tableData = stockData.find_all("tr")

for row in tableData:
    table = row.find_all('td')
    try:
        date = table[0].get_text().strip()
        if date is '':
            continue
        appleStockData[date] = {}
        appleStockData[date]['Closing'] = table[4].get_text().strip()
    except IndexError:
        pass
"""
for table in stockData:
    rows = table.find_all('tr')
    for row in rows:
        tableData = row.find_all('td')
        date = tableData[0].get_text().strip()
        if date is '':
            continue
        appleStockData[date] = {}
        appleStockData[date]['Closing'] = tableData[4].get_text().strip()
"""
pprint.pprint(appleStockData)