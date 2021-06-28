import sys
import time
import os
from yahoo_scrap import YahooInfoGet
import os
import datetime
import texttable
from color_config import *

#
# #
# class Test:
#     def __init__(self):
#         self.columns = 90
#
# os.get_terminal_size = Test

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def mystrlen(s):
    return max(len(line) for line in str(s).split('\n'))


def autodetectWidth(data):
    widths = [0] * len(data[0])
    for line in data:
        for i in range(len(line)):
            widths[i] = max(widths[i], mystrlen(line[i]))

    col = os.get_terminal_size().columns -12
    widths = [4,5,10,5,10,9]
    mm = sum(widths)
    widths = [int(x * 1.0 / mm * col)  for x in widths]
    return widths

def format_dict(stock):
    # stock['Ticker'] = f"{On_Black}" + stock['Ticker'] + f"{Color_Off}"
    if stock['Change'][0] == '+':
        stock['Price'] = f"{Green}" + stock['Price'] + f"{Color_Off}"
        stock['Change'] = f"{On_Green}" + stock['Change'] + f"{Color_Off}"
    elif stock['Change'][0] == '-':
        stock['Price'] = f"{Red}" + stock['Price'] + f"{Color_Off}"
        stock['Change'] = f"{On_Red}" + stock['Change'] + f"{Color_Off}"

    # if stock['PrePostChange'][0] == '+':
    #     stock['PrePostPrice'] = f"{Red}" + stock['Price'] + f"{Color_Off}"
    #     stock['PrePostChange'] = f"{On_Green}" + stock['PrePostChange'] + f"{Color_Off}"
    # elif stock['PrePostChange'][0] == '-':
    #     stock['PrePostPrice'] = f"{Red}" + stock['Price'] + f"{Color_Off}"
    #     stock['PrePostChange'] = f"{On_Red}" + stock['PrePostChange'] + f"{Color_Off}"

    return stock


def form_str(stocks):
    new_list = [['TICKER', 'PRICE','CHANGE', 'PPPrice','CHANGE', 'DAYRANGE']]
    len_list = [['TICKER', 'PRICE','CHANGE', 'PPPrice','CHANGE', 'DAYRANGE']]
    for stock in stocks:
        len_list.append(list(stock.values()))
        # stock = format_dict(stock)
        new_list.append([stock['Ticker'], stock['Price'][0:6], stock['Change'].replace(' ','').replace('00(','('), stock['PrePostPrice'][0:6], stock['PrePostChange'].replace(' ',''), stock['DayRange'].replace(' ','')])
        # new_list.append(['', '', '','','',''])

    table = texttable.Texttable()

    table.set_cols_align(["l", "l", "l","l","l","l"])
    table.set_cols_valign(["l", "l", "l","l","l","l"])
    table.set_deco(texttable.Texttable.HEADER)
    table.set_header_align(["l", "l", "l","l","l","l"])

    # table.header(['Ticker', 'Price', 'Change','PrePostPrice', 'Price ','Range'])
    table.set_cols_width(autodetectWidth(new_list))
    # table.set_cols_width([20,20,20,20,20,20])

    table.add_rows(new_list)
    # import pdb; pdb.set_trace()
    return table.draw()


while True:
    data_list = []
    LIST_OF_STOCKS = ['TIGR', 'AAPL', 'BB', 'CRSR', 'FLGT','SPY', 'C6L.SI', 'F83.SI','SENS']
    Test = False
    if Test:
        data_list = [{'Ticker': 'TIGR', 'Price': '26.62', 'PrePostPrice': '26.94', 'Change': '+2.54 (+10.55%)',
                      'PrePostChange': '+0.32 (1.20%)', 'DayRange': '24.23 - 26.84'},
                     {'Ticker': 'AAPL', 'Price': '133.70', 'PrePostPrice': '134.22', 'Change': '-0.28 (-0.21%)',
                      'PrePostChange': '+0.52 (0.39%)', 'DayRange': '133.23 - 134.32'},
                     {'Ticker': 'BB', 'Price': '13.14', 'PrePostPrice': '13.12', 'Change': '-0.27 (-2.01%)',
                      'PrePostChange': '-0.02 (-0.15%)', 'DayRange': '12.91 - 13.47'},
                     {'Ticker': 'CRSR', 'Price': '32.52', 'PrePostPrice': '32.63', 'Change': '+0.73 (+2.30%)',
                      'PrePostChange': '+0.11 (0.34%)', 'DayRange': '31.89 - 32.96'}]

    else:
        for stock in LIST_OF_STOCKS:
            yp = YahooInfoGet(stock)
            ans = yp.get_result()
            data_list.append(ans)

    now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    date_str = f"{Cyan}Updated Date: {now}{Color_Off}"
    col = os.get_terminal_size().columns

    right_side = col - len(date_str) - 12
    empty_space = right_side * ' '
    line_break = '-' * col
    var = {}
    var['empty_space'] = empty_space
    var['date_str'] = date_str
    var['line_break'] = line_break

    res_string = f"""\r
 {Yellow}WFSTOCK{Color_Off}%(empty_space)s%(date_str)s
%(line_break)s
""" % var

    clear_console()
    # res_string = ''
    res_string = res_string + form_str(data_list) + "\n\n"
    res_string = res_string.replace('\033[0m','\033[0m          ')
    print(res_string, end='\r')

    time.sleep(60 * 2)
