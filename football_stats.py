from bs4 import BeautifulSoup
import pprint
import urllib.request

URL = "https://www.cbssports.com/nfl/stats/playersort/nfl/year-2018-season-regular-category-touchdowns"

with urllib.request.urlopen(URL) as data:
    tdData = BeautifulSoup(data, features="lxml")

playerData = tdData.find_all("tr", class_={"row1","row2"})

top20Data = {}

for player in playerData[:20]:
    playerName = player.contents[0].get_text()
    top20Data[playerName] = {}
    top20Data[playerName]['Position'] = player.contents[1].get_text()
    top20Data[playerName]['Team'] = player.contents[2].get_text()
    top20Data[playerName]['Total Touchdowns'] = player.contents[6].get_text()

pprint.pprint(top20Data, width=30)