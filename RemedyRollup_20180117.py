# %load RemedyRollup_20180117.py
# Standard import for pandas, numpy and matplot
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Read in the csv file and display some of the basic info
    # sales=pd.read_csv("sample-salesv2.csv",parse_dates=['date'])
#    sales = pd.read_csv("data/RemedyRollup_20180117_j.csv", parse_dates=['Submit Date'])
    sales = pd.read_csv("data/RemedyRollup_20180117_j.csv")
    print("Data types in the file:")
    print(sales.dtypes)
    print("Summary of the input file:")
    print(sales.describe())
    print("Basic unit price stats:")
    print(sales['Calendar Days'].describe())

    # Filter the columns down to the ones we need to look at for customer sales
    customers = sales[['Assignee.Full Name', 'Calendar Days', 'Submit Date']]

    # Group the customers by name and sum their sales
    customer_group = customers.groupby('Assignee.Full Name')
    sales_totals = customer_group.sum()

    # Create a basic bar chart for the sales data and show it
    bar_plot = sales_totals.sort(columns='Status', ascending=False).plot(kind='bar', legend=None, title="Total Sales by Customer")
    bar_plot.set_xlabel("Customers")
    bar_plot.set_ylabel("Sales ($)")
    plt.show()

    # Do a similar chart but break down by category in stacked bars
    # Select the appropriate columns and group by name and category
    customers = sales[['Assignee.Full Name', 'Status', 'Calendar Days', 'Submit Date']]
    category_group = customers.groupby(['Assignee.Full Name', 'Status']).sum()

    # Plot and show the stacked bar chart
    stack_bar_plot = category_group.unstack().plot(kind='bar', stacked=True, title="Total Sales by Customer", figsize=(9, 7))
    stack_bar_plot.set_xlabel("Assignee.Full Name")
    stack_bar_plot.set_ylabel("Calendar Days")
    stack_bar_plot.legend(["Total", "Belts", "Shirts", "Shoes"], loc=9, ncol=4)
    plt.show()

    # Create a simple histogram of purchase volumes
    purchase_patterns = sales[['ext price', 'date']]
    purchase_plot = purchase_patterns['ext price'].hist(bins=20)
    purchase_plot.set_title("Purchase Patterns")
    purchase_plot.set_xlabel("Order Amount($)")
    purchase_plot.set_ylabel("Number of orders")
    plt.show()

    # Create a line chart showing purchases by month
    purchase_patterns = purchase_patterns.set_index('date')
    month_plot = purchase_patterns.resample('M', how=sum).plot(title="Total Sales by Month", legend=None)
    fig = month_plot.get_figure()

    # Show the image, then save it
    plt.show()
    fig.savefig("output\total-sales.png")


    print(dir(os.path))



if __name__ == '__main__':
    main()


