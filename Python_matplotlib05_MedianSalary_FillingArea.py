#https://www.youtube.com/watch?v=UO98lJQ3QGI

import random
import os
import pandas as pd
from matplotlib import pyplot as plt

def main():
    # list attributes and methods that are part of 'os'

    #print(dir(os))

    #### print out current working directory
    print("getcwd(): ",os.getcwd())

    my_csv_file = 'Python_matplotlib05_MedianSalary_FillingArea_data.csv'
    # print(plt.style.available)
    plt.style.use('fivethirtyeight')
#    plt.xkcd()

    data = pd.read_csv(my_csv_file)
    ages = data['Age']
    dev_salaries = data['All_Devs']
    py_salaries = data['Python']
    js_salaries = data['JavaScript']

    plt.plot(ages, dev_salaries, color='#44444444'
        , linestyle='--', label='All Devs')

    plt.plot(ages, py_salaries, color='#44444444'
        , label='Python')

    overall_median = 57287


    # first fill-between
    
#    plt.fill_between(ages, py_salaries, overall_median
#        , where=(py_salaries > overall_median)
#        , interpolate=True, alpha=0.25)
    
    # second fill-between
    
#    plt.fill_between(ages, py_salaries, overall_median
#        , where=(py_salaries <= overall_median)
#        , interpolate=True, alpha=0.25, color='red')



    # first fill-between - b
    
    plt.fill_between(ages, py_salaries, dev_salaries
        , where=(py_salaries > dev_salaries)
        , interpolate=True, alpha=0.25, label='Above Avg.')
    
    # second fill-between - b
    
    plt.fill_between(ages, py_salaries, dev_salaries
        , where=(py_salaries <= dev_salaries)
        , interpolate=True, alpha=0.25, color='red', label='Below Avg.')


    plt.legend()

    plt.grid(True)

    plt.xlabel('Ages')
    plt.ylabel('Median Salary')
    plt.title('Median Salary (USD) by Age')

    plt.tight_layout()
    plt.savefig('Python_matplotlib05_MedianSalary_FillingArea.png')
    
    plt.show()


if __name__ == '__main__':
    main()



