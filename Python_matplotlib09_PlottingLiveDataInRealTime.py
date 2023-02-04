# https://www.youtube.com/watch?v=XDv6T4a0RNc&list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_&index=6

import random
from itertools import count
import os
import sys
from datetime import datetime, timedelta
from DefaultItems import LogFileFolder as LFF
from DefaultItems import DataFolder as DFF

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

    plt.style.use('fivethirtyeight')

    x_vals = [0, 1, 2, 3, 4, 5 ]
    y_vals = [0, 1, 3, 2, 3, 5 ]

    y = [0, 1, 3, 4, 6, 5, 7]

    #plt.plot(x_vals, y_vals, linestyle='solid')

    x_vals = []
    y_vals = []

    index = count()

    def animate(i):
        data = pd.read_csv(csv_data_file_and_path)
        x = data['x_value']
        y1 = data['total_1']
        y2 = data['total_2']

        plt.cla()
        plt.plot(x, y1, label='Channel 1')
        plt.plot(x, y2, label='Channel 2')
        plt.legend(loc='upper left')
        plt.tight_layout()

    ani = FuncAnimation(plt.gcf(), animate, interval=1000)

    filename = "Python_matplotlib09_PlottingLiveDataInRealTime_data.csv"
    csv_data_file_and_path = os.path.join(DFF,filename)




    print(csv_data_file_and_path)

    plt.show()


if __name__ == '__main__':
#    @crashreport
#    def main():
#        3/0
#    configure_crashreport(
#        )

    main()



