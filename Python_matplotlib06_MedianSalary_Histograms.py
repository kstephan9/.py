# https://www.youtube.com/watch?v=XDv6T4a0RNc&list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_&index=6

import random
import os
import pandas as pd
from matplotlib import pyplot as plt

def main():
    # list attributes and methods that are part of 'os'

    #print(dir(os))

    #### print out current working directory
    print("getcwd(): ",os.getcwd())

#    ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]

    filename = 'Python_matplotlib06_MedianSalary_Histograms_data.csv'

    data = pd.read_csv(filename)
    ids = data['Responder_id']
    ages = data['Age']
    
    bins_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    plt.hist(ages, bins=bins_list, edgecolor='black', log=True)

    median_age = 29
    mycolor = '#fc4f30'
    
    plt.axvline(median_age, color = mycolor
                , label='Age Median'
                , linewidth=2)
    plt.legend()

    plt.title('Ages of Respondents')
    plt.xlabel('Ages')
    plt.ylabel('Total Respondents')
    
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()



