import sys
import time
import os
from yahoo_scrap import YahooInfoGet
import os
import datetime
import texttable
#
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

    col = os.get_terminal_size().columns
    mm = sum(widths)
    widths = [int(x*1.0/mm * col)-2 for x in widths]
    return widths



def form_str(stocks):

    new_list = [['TICKER','PRICE','PREPOST_PRICE']]

    for stock in stocks:
        new_list.append(list(stock.values()))
        new_list.append(['','',''])


    table = texttable.Texttable()

    table.set_cols_align(["l", "l", "l"])
    table.set_cols_valign(["l", "l", "l"])
    table.set_deco(texttable.Texttable.HEADER)
    table.set_header_align(["l", "l", "l"])

    table.header(['Ticker','Price','PrePostPrice'])


    table.set_cols_width(autodetectWidth(new_list))
    table.add_rows(new_list)

    return table.draw()

while True:
    data_list = []
    LIST_OF_STOCKS = ['TIGR','AAPL','BB','CRSR','FLGT','C6L.SI','F83.SI']
    for stock in LIST_OF_STOCKS:
        yp = YahooInfoGet(stock)
        ans = yp.get_prices()
        data_list.append(ans)

    now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    date_str = "Updated Date: {}".format(now)
    col = os.get_terminal_size().columns

    right_side = col - len(date_str) - 10
    empty_space = right_side * ' '
    line_break = '-' * col
    var = {}
    var['empty_space'] = empty_space
    var['date_str'] = date_str
    var['line_break'] = line_break

    res_string = """\r
 WFSTOCK%(empty_space)s%(date_str)s
%(line_break)s
    """ % var


    clear_console()
    res_string  = res_string + form_str(data_list) + "\n\n"
    print(res_string, end = '\r')

    time.sleep(60*5)
