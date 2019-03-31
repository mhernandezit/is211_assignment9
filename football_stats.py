""" Football Stats module - pulls and parses data from cbssports.com """
from urllib2 import Request, urlopen, URLError, HTTPError
from bs4 import BeautifulSoup

URL = ("https://www.cbssports.com/nfl/stats/"
       "playersort/nfl/year-2018-season-regular-category-touchdowns")

def download_data(url):
    """Download the CSV at the url provided, return a URLlib response object"""
    try:
        req = Request(url)
        response = urlopen(req)
    except HTTPError:
        pass
    except URLError:
        pass
    return response

def process_data(data):
    """ Convert the data into a beautifulsoup object, and parse the object
    for table data.
    We will be returning a dictionary with the player name as the key, and
    the Position, Team and TD data as values """
    td_data = BeautifulSoup(data, features="lxml")
    player_data = td_data.find_all("tr", class_={"row1", "row2"})
    top20_data = {}
    for player in player_data[:20]:
        player_name = player.contents[0].get_text()
        top20_data[player_name] = {}
        top20_data[player_name]['Position'] = player.contents[1].get_text()
        top20_data[player_name]['Team'] = player.contents[2].get_text()
        top20_data[player_name]['TD'] = player.contents[6].get_text()
    return top20_data

def print_data(dict_data):
    """ Print function to retrieve and print out the dictionary items """
    print('{:20} : {:8} : {:6} : {:6}').format('Player', 'Position', 'Team', 'TD')
    for player, stats in dict_data.items():
        print('{:20} : {:8} : {:6} : {:6}').format(player, stats['Position'],
                                                   stats['Team'], stats['TD'])

def main():
    """ Main function - nested to download, process and display the data """
    print_data(process_data(download_data(URL)))

if __name__ == "__main__":
    main()
