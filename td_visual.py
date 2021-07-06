from TD_helper import TD_Helper
from color_config import *
import time
import os
import art

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def format_dict(stock):
    # stock['Ticker'] = f"{On_Black}" + stock['Ticker'] + f"{Color_Off}"
    if type(stock['netChange']) == str :
        return stock
    if stock['netChange'] > 0:
        stock['lastPrice'] =f"{Black}" + f"{On_Green}" + str(stock['lastPrice']) + f"{Color_Off}" + f"{Color_Off}"
        stock['netChange'] = f"{Black}" + f"{On_Green}"+ str(stock['netChange'] * 100) + '%' +  f"{Color_Off}" + f"{Color_Off}"
        stock['netPercentChangeInDouble'] =f"{Black}" + f"{On_Green}" + str(stock['netPercentChangeInDouble']) + f"{Color_Off}" + f"{Color_Off}"
    elif stock['netChange'] < 0:
        stock['lastPrice'] = f"{On_Red}" + str(stock['lastPrice']) + f"{Color_Off}"
        stock['netChange'] = f"{On_Red}" + str(stock['netChange'] * 100)  + "%" + f"{Color_Off}"
        stock['netPercentChangeInDouble'] = f"{On_Red}" + str(stock['netPercentChangeInDouble']) + f"{Color_Off}"

    # if stock['PrePostChange'][0] == '+':
    #     stock['PrePostPrice'] = f"{Red}" + stock['Price'] + f"{Color_Off}"
    #     stock['PrePostChange'] = f"{On_Green}" + stock['PrePostChange'] + f"{Color_Off}"
    # elif stock['PrePostChange'][0] == '-':
    #     stock['PrePostPrice'] = f"{Red}" + stock['Price'] + f"{Color_Off}"
    #     stock['PrePostChange'] = f"{On_Red}" + stock['PrePostChange'] + f"{Color_Off}"

    return stock


def get_visual(var):
    var = format_dict(var)
    print(art.text2art(var['symbol'], font ='small')[0:-10])
    text = """
    Price: %(lastPrice)s
    Change: %(netChange)s (%(netPercentChangeInDouble)s)
    High: %(highPrice)s Low: %(lowPrice)s
    Open: %(openPrice)s Close: %(closePrice)s"""

    print(text % var)




if __name__ == '__main__':
    tickers = ['BB', 'AAPL', 'TIGR', 'FLGT','SPY']
    while True:
        td = TD_Helper()
        res = td.get_data(','.join(tickers))
        t = 0
        while t < 60:
            for key, val in res.items():
                clear_console()
                get_visual(val)
                time.sleep(8)

                t = t + 5


