from DefaultItems import DataFolder

import sys

import pandas as pd


class Test:
    pass


def main():
    # %Y = full year 2019
    # %y = partial year 19
    # %m = number of month
    # %d = number of day
    # %H = hours
    # %M = minutes
    # %S = seconds
    # 12-06-2019 is %m-%d-%Y

    file_name = 'Mode_FlightData.csv'
    full_path = DataFolder + "//" + file_name

    df = pd.read_csv(full_path, index_col='flight_date')

    # sellect first two rows, df.iloc[:2], last two rows, df.iloc[-2:]

    print(df.iloc[:2])

    print(df)
    # select rows by column value and
    # print(df[(df["unique_carrier"] == "AA") & (df["dist"] == "2475")])
    print(df[(df["actual_elapsed_time"] > 500.0) & (df["unique_carrier"] == "AA")])


if __name__ == "__main__":
    main()
