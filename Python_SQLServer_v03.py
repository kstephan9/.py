#
# https://www.youtube.com/watch?v=--aZ6K-PVtE
#

import pyodbc
import os
import urllib
import datetime
import sys

print("Python Version: ",sys.version)

def main():

    #### print out current working directory
    print("getcwd(): ",os.getcwd())

    server = 'gldds99603'

    db = 'r11_v01'

    cnxn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server
        + ';DATABASE=' + db + ';Trusted_Connection=yes')

    with cnxn:

        cursor = cnxn.cursor()
        cursor.execute("SELECT * from [AAAAAA]")

        #while 1:
        #    row = cursor.fetchone()

        #    if not row:
        #        break

         #   print("row.VIP: ",row.VIP)

        cursor.execute("SELECT * from [AAAAAA]")

        for row in cursor:
            print('row =%r' %(row,))

    #cursor.execute("UPDATE CommaDelimeter SET Name = 'Vaibhav' WHERE NAME = 'ABHE'")
    #cnxn.commit()

        #cnxn.close()


if __name__ == '__main__':
    main()


