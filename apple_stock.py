""" Apple_Stock module - pulls and parses stock data from Nasdaq.com """
from urllib2 import Request, urlopen, URLError, HTTPError
from bs4 import BeautifulSoup

URL = 'https://www.nasdaq.com/symbol/aapl/historical'

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
    We will be returning a dictionary with the date, closing price data """
    soup = BeautifulSoup(data, features="lxml")

    stock_data = {}

    table_data = soup.find("div", class_="genTable")
    row_data = table_data.find_all("tr")
    for row in row_data:
        column = row.find_all('td')
        if not column:
            continue
        if column[0].get_text() == '\n':
            continue
        date = column[0].get_text().strip()
        stock_data[date] = {}
        stock_data[date]['Closing'] = column[4].get_text().strip()
    return stock_data

def print_data(dict_data):
    """ Prints out the stock data """
    print("{:10} : {:7}").format('Date', 'Closing Price')
    for date, statistics in dict_data.items():
        print("{:10} : {:7}").format(date, statistics['Closing'])

def main():
    """ Main function - nested functions to load the data from the CSV,
    process the data, and finally print the processed data """
    print_data(process_data(download_data(URL)))

if __name__ == "__main__":
    main()
