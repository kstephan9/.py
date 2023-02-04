# https://www.youtube.com/watch?v=XDv6T4a0RNc&list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_&index=6

import random
from itertools import count
import os
import sys
from datetime import datetime, timedelta
from DefaultItems import LogFileLocation
from DefaultItems import DataFileLocation

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from matplotlib.animation import FuncAnimation

def main():
    # list attributes and methods that are part of 'os'

    #print(dir(os))

    #### print out current working directory
    print("getcwd(): ",os.getcwd())

    print("Version of Python: " + os.path.dirname(sys.executable))

    print(pd.__version__)

    plt.style.use('seaborn')

    dates = [
            datetime(2019, 5, 24),
            datetime(2019, 5, 25),
            datetime(2019, 5, 26),
            datetime(2019, 5, 27),
            datetime(2019, 5, 28),
            datetime(2019, 5, 29),
            datetime(2019, 5, 30)
            ]

    y = [0, 1, 3, 4, 6, 5, 7]

#    plt.plot_date(dates, y, linestyle='solid')


#    date_format = mpl_dates.DateFormatter('%b, %d %Y')


    filename = 'Python_matplotlib09_PlottingTimeSeriesData.csv'
    csv_data_file_and_path = os.path.join(DataFileLocation, filename)

    print(csv_data_file_and_path)

    data = pd.read_csv(csv_data_file_and_path)

    data['Date'] = pd.to_datetime(data['Date'])
    data.sort_values('Date', inplace=True)

    price_date = data['Date']
    price_close = data['Close']


    #date_format = mpl_dates.DateFormatter('%b, %d %Y')
    #plt.gca().xaxis.set_major_formatter(date_format)

    plt.plot_date(price_date, price_close, linestyle='solid')
    plt.gcf().autofmt_xdate()

    x_vals = [0, 1, 2, 3, 4, 5 ]
    y_vals = [0, 1, 3, 2, 3, 5 ]

    x_vals = []
    y_vals = []

    index = count() # uses iteratortool

    def animate(i):
        x_vals.append(next(index))
        y_vals.append(random.randint(0, 5))

        plt.cla()
        plt.plot(x_vals, y_vals)

#    ani = FuncAnimation(plt.gcf(),  animate, interval=1000)



    plt.title('Bitcoin Prices - Time Series Data')
    plt.xlabel('Date')
    plt.ylabel('Closing Prices')

    plt.legend()

    #plt.plot(x_vals, y_vals)

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()



