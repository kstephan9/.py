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

    filename = 'Python_matplotlib07_ScatterPlot_data.csv'

    
    bins_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    plt.style.use('seaborn')
    
    x = [5,7,8,5,6,7,9,2,3,4,4,4,2,6,3,6,8,6,4,1]
    y = [7,4,3,9,1,3,2,5,2,4,8,7,1,6,4,9,7,7,5,1]

    colors_list = [7,5,9,7,5,7,2,5,3,7,1,2,8,1,9,2,5,6,7,5]

    size_list = [209, 486, 381, 255, 191, 315, 185, 228, 174,
        538, 239, 394, 300, 153, 273, 293, 436, 501, 397, 539]

    data = pd.read_csv(filename)
    view_count = data['view_count']
    likes = data['likes']
    ratio = data['ratio']
    
    #plt.xlim(0,10)
    #plt.ylim(0,10)
    plt.scatter(view_count, likes, c=ratio
                , cmap='summer'
                , marker='o'
                , edgecolor='black'
                , linewidth=1,alpha=0.75)
    cbar = plt.colorbar()
    cbar.set_label('Like/Dislike Ratio')
    
    plt.xscale('log')
    plt.yscale('log')
    #cbar = plt.colorbar()
    #cbar.set_label('Satisfaction')

    median_age = 29
    mycolor = '#fc4f30'



    plt.legend()

    plt.title('Trending YouTube Videos')
    plt.xlabel('View Count')
    plt.ylabel('Total Likes')
    
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()



