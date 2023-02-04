# https://www.youtube.com/watch?v=UO98lJQ3QGI

import random
import os
import pandas as pd
from matplotlib import pyplot as plt

# plt.gcf()
# plt.gca()


def main():
    # list attributes and methods that are part of 'os'

    # print(dir(os))

    # print out current working directory
    print("getcwd(): ", os.getcwd())

    my_csv_file = 'Python_matplotlib05_MedianSalary_FillingArea_data.csv'
    # print(plt.style.available)
    plt.style.use('fivethirtyeight')
    plt.style.use('seaborn')
#    plt.xkcd()

    data = pd.read_csv(my_csv_file)
    ages = data['Age']
    dev_salaries = data['All_Devs']
    py_salaries = data['Python']
    js_salaries = data['JavaScript']

#    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
    fig1, (ax1) = plt.subplots()
    fig2, (ax2) = plt.subplots()

    ax1.plot(ages, dev_salaries, color='#44444444', linestyle='--', label='All Devs')

    ax2.plot(ages, py_salaries, color='#44444444', label='Python')

    ax2.plot(ages, js_salaries, color='#44444444', label='JavaScript')

    ax1.legend()

    plt.grid(True)

    ax1.legend()
    ax1.set_xlabel('Ages')
    ax1.set_ylabel('Median Salary')
    ax1.set_title('Median Salary (USD) by Age')

    ax2.legend()
    ax2.set_xlabel('Ages')
    ax2.set_ylabel('Median Salary')
#    ax2.set_title('Median Salary (USD) by Age')

    plt.tight_layout()
    plt.savefig('Python_matplotlib05_MedianSalary_FillingArea.png')

    plt.show()

    #fig1.savefig('fig1.png')
    #fig2.savefig('fig2.png')

if __name__ == '__main__':
    main()
