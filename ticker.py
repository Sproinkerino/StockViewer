import requests


class StockPrice:
    def __init__(self, key):
        pass

    def request_data(self, ticker):
        url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey={}'.format(ticker, APIKEY)
        r = requests.get(url)
        data = r.json()

        return (data)


if __name__ == '__main__':
    APIKEY = 'T0DFJKUHBBH1SZQ0'

    data_list = []
    LIST_OF_STOCKS = ['TIGR','AAPL','BB','CRSR']
    for stock in LIST_OF_STOCKS:
        sp = StockPrice(APIKEY)
        data = sp.request_data(stock)
        data_list.append(data)
    print([x['Global Quote'] for x in data_list])
