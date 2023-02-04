## https://www.youtube.com/watch?v=rNGJtWGQ3b8
# Gina Bueno

import csv, os, slack # import statements
from DefaultItems import DataFolder, OutputFolder

CSVFileName = "Python_Sysadmin_Tasks_001_test.csv"
my_csvfile = os.path.join(DataFolder,CSVFileName)
# read csv with ip addresses
print(my_csvfile)
with open(my_csvfile) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    # convert it to a list
    new_list = list(reader)
    # remove the first element in the list
#    new_list.pop(0)
    output = ''
    # loop through csv list
    for row in new_list:
        print("at xxx, row is: ", row)
        ip_addr = row[0]
        # ping each server
#        resp = os.system("ping -c 2 " + ip_addr)
        resp = os.system("ping " + ip_addr)
        if resp == 0:
            output += ip_addr + ', is up!\n'
        else:
            output += ip_addr + ', is down!\n'

# open csv for writing

Output_CSVFileName = "Python_Sysadmin_Tasks_001_test_output_file.csv"
my_csv_output_file = os.path.join(OutputFolder, Output_CSVFileName)


with open(my_csv_output_file,'w', newline='') as fd:
    fd.write(output)

# define parameters for slack
url = "https://hooks.slack.com/services/key-from-slack"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }

#call slack function
slack.slack(my_csv_output_file,url,headers)


