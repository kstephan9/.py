from DefaultItems import DataFolder
from DefaultItems import Raw_2_FileLocation
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

    file_name = 'tblA010IncidentToAsset_V10.xlsx'
    full_path = Raw_2_FileLocation + "//" + file_name

    df = pd.read_excel(full_path)
    print(df.head(5))
    column_list = list(df.columns)
    print("\n")
    for mycol in column_list:
        print(mycol)
    # sellect first two rows, df.iloc[:2], last two rows, df.iloc[-2:]

    # print(df.iloc[:2])

    # print(df)
    # # select rows by column value and
    # # print(df[(df["unique_carrier"] == "AA") & (df["dist"] == "2475")])
    # print(df[(df["actual_elapsed_time"] > 500.0) & (df["unique_carrier"] == "AA")])


if __name__ == "__main__":
    main()
