import requests
from bs4 import BeautifulSoup


class YahooInfoGet:
    def __init__(self, ticker):
        self.ticker = ticker
        self.URL = URL = 'https://sg.finance.yahoo.com/quote/{}/'.format(ticker)
        page = requests.get(URL)
        self.soup = BeautifulSoup(page.content, 'html.parser')
        self.price = None
        self.pre_post_price = None
        self.change = None
        self.pre_post_change = None
        self.pre_post_price = None
        self.range = None

    def get_yahoo_price(self, key):
        price = self.soup.find_all("span", {"class": key})
        try:
            price = price[0].contents[0]
        except BaseException:
            price = 'NA'
        return price



    def get_yahoo_change(self, key):
        price = self.soup.find_all("span", {"class": [key + " C($positiveColor)", key + " C($negativeColor)"]})
        try:
            price = price[0].contents[0]
        except BaseException:
            price = 'NA'
        return price

    def get_result(self):
        self.get_prices()
        self.get_change()
        self.get_range()
        return {'Ticker': self.ticker, 'Price': self.price, 'PrePostPrice': self.pre_post_price, 'Change': self.change,
                'PrePostChange': self.pre_post_change, 'DayRange': self.range
                }

    def get_prices(self):
        self.price = self.get_yahoo_price("Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
        self.pre_post_price = self.get_yahoo_price("C($primaryColor) Fz(24px) Fw(b)")

    def get_change(self):
        self.change = self.get_yahoo_change("Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px)")
        self.pre_post_change = self.get_yahoo_change("Trsdu(0.3s) Mstart(4px) D(ib) Fz(24px)")

    def get_range(self):



        range = self.soup.findAll(attrs={"data-test" : "DAYS_RANGE-value"})
        try:
            range = range[0].contents[0]
        except BaseException:
            range = 'NA'

        self.range = range


if __name__ == '__main__':
    data_list = []
    LIST_OF_STOCKS = ['TIGR', 'AAPL', 'BB', 'CRSR']
    for stock in LIST_OF_STOCKS:
        yp = YahooInfoGet(stock)
        ans = yp.get_result()
        data_list.append(ans)
    print(data_list)
