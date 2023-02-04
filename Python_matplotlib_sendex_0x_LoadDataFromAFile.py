# https://www.youtube.com/watch?v=q7Bo_J8x_dw&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF

from DefaultItems import DataFileLocation
from pathlib import Path

import matplotlib.pyplot as plt


import csv


class Test:
    pass


def main():
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

    import numpy as np

    x, y = np.loadtxt(datafile, delimiter=',', unpack=True)
    plt.plot(x, y, label='Loaded from a csv file')

    plt.legend()

    plt.show()


if __name__ == "__main__":
    main()
