# https://www.youtube.com/watch?v=XDv6T4a0RNc&list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_&index=6

import random
import os
from datetime import datetime, timedelta
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

def main():
    # list attributes and methods that are part of 'os'

    #print(dir(os))

    #### print out current working directory
    print("getcwd(): ",os.getcwd())

    filename = 'Python_matplotlib08_PlottingtimeSeriesData_data.csv'

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



    data = pd.read_csv(filename)
    
    data['Date'] = pd.to_datetime(data['Date'])

    data.sort_values('Date', inplace=True)
    
    price_date = data['Date']
    price_close = data['Close']

 #   plt.plot_date(dates, y, linestyle='solid')
    plt.plot_date(price_date, price_close, linestyle='solid')

    plt.gcf().autofmt_xdate()
 #   date_format = mpl_dates.DateFormatter('%b, %d %Y')
    
 #   plt.gca().xaxis.set_major_formatter(date_format)
    
 #   plt.xscale('log')
 #   plt.yscale('log')
    #cbar = plt.colorbar()
    #cbar.set_label('Satisfaction')



    plt.title('Bitcoin Prices')
    plt.xlabel('Date')
    plt.ylabel('Closing Prices')

    plt.legend()
    
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()



