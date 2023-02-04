import os
import csv
import random
import time
from DefaultItems import LogFileLocation
from DefaultItems import DataFileLocation

x_value = 0
total_1 = 1000
total_2 = 1000

fieldnames = ["x_value", "total_1", "total_2"]

filename = "Python_matplotlib09_PlottingLiveDataInRealTime_data.csv"
csv_data_file_and_path = os.path.join(DataFileLocation,filename)

print(csv_data_file_and_path)

with open(csv_data_file_and_path, 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open(csv_data_file_and_path, 'a', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "x_value": x_value,
            "total_1": total_1,
            "total_2": total_2
        }

        csv_writer.writerow(info)
        print(x_value, total_1, total_2)

        x_value += 1
        total_1 = total_1 + random.randint(-6, 8)
        total_2 = total_2 + random.randint(-5, 6)

    time.sleep(1)
