import requests
import json
KEY = 'DILVCCGLUZUKVBPLUSFQCGYCMSOW4F4L'
from color_config import *




class TD_Helper:
    def __init__(self):
        pass

    def get_data(self, symbol):
        try:
            r = requests.get(f'https://api.tdameritrade.com/v1/marketdata/quotes?apikey={KEY}&symbol={symbol}')
        except:
            r = requests.get(f'https://api.tdameritrade.com/v1/marketdata/quotes?apikey={KEY}&symbol={symbol}')
        return self.format_data(r.json())

    def format_data(self, res):
        # new_dict = {}
        # for k, r in res.items():
        #     r = {k: v for k, v in r.items() if k in ['lastPrice','symbol','netPercentChangeInDouble','highPrice','lowPrice','netChange']}
        # new_dict[k] = r
        return(res)

if __name__ == '__main__':
    td = TD_Helper()
    td.get_data('BB')