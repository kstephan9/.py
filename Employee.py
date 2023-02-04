# %load Employee.py
# https://www.youtube.com/watch?v=-ARI4Cz-awo&t=635s
#
# Logging Basics - Loggint to Files, Setting Levels, and Formatting
#
# Corey Schafer
#

import logging
import sys
import os
from DefaultItems import LogFileFolder




#print("elog: ", elog)

print("Entered Employee.py")
print("Python Version: ",sys.version)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

suffix = '.log'
elog = os.path.join(LogFileFolder, 'employee' + suffix)

file_handler = logging.FileHandler(elog)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

#logging.basicConfig(filename = 'employee.log',
#    level = logging.INFO, format='%(levelname)s:%(name)s:%(asctime)s:%(levelname)s:%(message)s')

#logger = logging.getLogger() 

class Employee:
    def __init__(self, first, last):
            self.first = first
            self.last = last
            
            logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def e_sort(emp):
        return emp.name
        
    
def main():
    #logger.info("xyz")

    empl_1 = Employee('Nora', 'Stephani')
    empl_2 = Employee('Nick', 'Stephani')
    empl_3 = Employee('Uri', 'Stephani')

    employees = [empl_1, empl_2, empl_3]

    s_emplooyees = sorted(employees, key=e_sort)

    print("Reached 'main' of Employee")

if __name__ == "__main__": 
    main()




