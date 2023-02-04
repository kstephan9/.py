# -*- coding: utf-8 -*-
"""
ated on Thu May 26 10:41:17 2022
uthor: ken.stephani
"""

import os
import glob
from DefaultItems import OutputFolder, ImageFolder

dir_path = os.path.dirname(os.path.realpath(__file__))

cwd = os.getcwd()

print("dir_path: ", dir_path)

#arr = os.listdir(OutputFolder)

 # Using '*' pattern 
print('\nNamed with wildcard *:')
#  for name in glob.glob(OutputFolder+"\\*.xlsx"):
for name in glob.glob(OutputFolder+"\\*[0-9]*.xlsx", recursive = True):
    print(name)
    
for name in glob.glob(ImageFolder+"\\*.*", recursive = True):
    print(name)
    
print("dir_path: ", dir_path)
          
print("cwd: ", cwd)
          