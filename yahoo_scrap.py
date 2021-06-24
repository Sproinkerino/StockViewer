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

    def get_yahoo_price(self, key):
        price = self.soup.find_all("span", {"class": key})
        try:
            price = price[0].contents[0]
        except BaseException:
            price = 'NA'
        return price

    def get_prices(self):
        self.price = self.get_yahoo_price("Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
        self.pre_post_price = self.get_yahoo_price("C($primaryColor) Fz(24px) Fw(b)")
        return {'Ticker': self.ticker, 'Price': self.price, 'PrePostPrice': self.pre_post_price}




if __name__ == '__main__':
    data_list = []
    LIST_OF_STOCKS = ['TIGR','AAPL','BB','CRSR']
    for stock in LIST_OF_STOCKS:
        yp = YahooInfoGet(stock)
        ans = yp.get_prices()
        data_list.append(ans)
    print(data_list)


