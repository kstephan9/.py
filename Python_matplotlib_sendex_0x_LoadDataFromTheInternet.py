# https://www.youtube.com/watch?v=q7Bo_J8x_dw&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF

from DefaultItems import DataFileLocation
from pathlib import Path

import matplotlib.pyplot as plt
import urllib
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
import csv


class Test:
    pass


def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)

    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


def graph_data(stock):

    # https://www.alphavantage.co/documentation/

    # stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/' + stock + '/chartdata;type=quote;range=10y/csv'

    stock_price_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + stock + '&interval=5min&apikey=L3QDINANAICKM4KJ&datatype=csv'

    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    source_code = source_code.replace('\r', '')

    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source:
        split_line = line.split(',')
        if 'timestamp' not in line and len(line) > 0:
            stock_data.append(split_line)

    # %Y = full year 2019
    # %y = partial year 19
    # %m = number of month
    # %d = number of day
    # %H = hours
    # %M = minutes
    # %S = seconds
    # 12-06-2019 is %m-%d-%Y

    print(type(stock_data))

    plotme = [0, 0]
    plotme2 = [0, 0]
    for line in stock_data:
        # print("line: ", line, " len: ", len(line), pd.to_datetime(line[0]), line[1])
        # plotme.append(pd.to_datetime(line[0]))
        # plotme.append(line[1])

        plotme = [pd.to_datetime(line[0]), line[1]]
        # print(plotme)
        plotme2.append(plotme)

    for line in plotme2:
        print("line: ", line)

#    date, openp, highp, lowp, closep, volume = np.loadtxt(stock_data, delimiter=',', skiprows=1, unpack=True, usecols=0,
#                                                          converters={0: bytespdate2num('%Y-%m-%d %H:%M:%S')}, #encoding='bytes')

    x = []
    y = []

    FileName = 'Mode_FlightData.csv'
    FileName = 'csvtest.csv'

    datafile = DataFileLocation + '\\' + FileName

    with open(datafile, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(int(row[0]))
            y.append(int(row[1]))

    plt.plot(x, y, label='Loaded from file')
    # plt.plot([], [], color='m', label='Sleeping', linewidth=5)
    # plt.plot([], [], color='c', label='Eating', linewidth=5)
    # plt.plot([], [], color='r', label='Working', linewidth=5)
    # plt.plot([], [], color='k', label='Playing', linewidth=5)

    # plt.stackplot(days, sleeping, eating, working, playing, colors=['m', 'c', 'r', 'k'])

    color_list = ['c', 'm', 'r', 'b']

    # plt.pie(slices, labels=activities, colors=color_list, startangle=90, shadow=True, explode=(0, 0.1, 0, 0),
    #        autopct='%1.1f%%')

    plt.legend()

    plt.show()

#    import numpy as np

    x, y = np.loadtxt(datafile, delimiter=',', unpack=True)
    plt.plot(x, y, label='Loaded from a csv file')

    plt.legend()

    plt.show()


def main():
    graph_data('TSLA')


if __name__ == "__main__":
    main()
