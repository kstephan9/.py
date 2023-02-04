## https://www.youtube.com/watch?v=rNGJtWGQ3b8
# Gina Bueno

import json
import csv, os, slack # import statements
from DefaultItems import JSONDataFolder, OutputFolder

JSONFileName = "incident_ServiceNow_20191021.json"
my_csvfile = os.path.join(JSONDataFolder,JSONFileName)
# read csv with ip addresses
print(my_csvfile)
#json.loads()
#json.dumps(json object, indent=2, sort_keys=True)

with open(my_csvfile) as csvfile:
    data = json.load(csvfile)

#print(json.dumps(data,indent=2, sort_keys=True))
#print(data)
# loop through csv list
for rec in data['records']:
    print("At xxx, rec[number] is: ", rec['number'])

# open csv for writing

Output_JSONFileName = "incident_ServiceNow_20191021_output.json"
my_json_output_file = os.path.join(OutputFolder, Output_JSONFileName)


with open(my_json_output_file,'w', newline='') as fd:
    json.dump(data, fd, indent=2)




'''
# define parameters for slack
url = "https://hooks.slack.com/services/key-from-slack"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }

#call slack function
slack.slack(my_csv_output_file,url,headers)

'''

