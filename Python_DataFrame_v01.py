
# https://www.youtube.com/watch?v=xvpNA7bC8cs&t=44s

import sys
sys.path.append(r'S:\BAEIT\ITIL\PerformanceManagementTeam\AssortedTasks\Learning\_Python\_Lib')


from DefaultItems import Raw_2Folder

import pandas as pd

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 10000)


class Test:
    pass


def main():
    ufo = pd.read_csv('http://bit.ly/uforeports')
    #print(ufo.head(3)) # list first three rows

    print(type(ufo.loc[0, :])) # Returns a "series". row 0, (index = 0), all columns.
    print(ufo.loc[0, :]) # row 0, (index = 0), all columns.

    print(ufo.loc[[100,1,2], :]) # rows 100, 1, 2 (index = 100, 1, 2), all columns.
    print(ufo.loc[0:2, :]) # rows 0 through 2 (index = 0 throug 2), all columns.

    print(ufo.loc[:, ['City', 'State']]) # rows 0 through 2 (index = 0 throug 2), all columns.

    print(ufo.loc[0:2, 'City': 'State']) # rows 0 through 2 columns 'City' through 'State'

    print(ufo[ufo.City=='Oakland']) # one method ...

    print(ufo.loc[ufo.City=='Oakland',:]) # rows where City is Oakland, all columns

    print(ufo.loc[ufo.City=='Oakland','State']) # rows where City is Oakland, State column only

    ################# iloc, filter by integer position

    print(ufo.iloc[:, 0:4]) # Returns a "series". row 0, (index = 0), all columns.

    print(ufo.iloc[0:3, :]) # Returns a "series". row 0, (index = 0), all columns.

    ####################### ix mix labels and integers

    drinks = pd.read_csv('http://bit.ly/drinksbycountry', index_col = 'country')
    print(drinks.head(3))

    print(drinks.ix['Albania', 0])

    print(drinks.ix[1, 'beer_servings'])

    print(drinks.ix['Albania':'Andorra', 0:2])

    print(ufo.ix[0:2, 0:2])


if __name__ == "__main__":
    main()


