import os

adir = 'c:\\users\\ken.stephani\\desktop'

pnf = os.path.join(adir,"ken.txt")

os.chdir(adir)

print("wd is: ", os.getcwd())

print(os.path.expanduser(adir))

print("dirname of pnf is: ", os.path.dirname(pnf)) 

print("base name of pnf is: ", os.path.basename(pnf)) 

print(dir(os))

# Print all the current file names
for f in os.listdir():
    print(f)

os.chdir("S:\\BAEIT\\ITIL")

for entry in os.scandir():
    print("entry: ", entry) 

 # https://www.bogotobogo.com/python/python_traversing_directory_tree_recursively_os_walk.php

 #import os
path = "s:\\BAEIT"

#fname = []
#for root,d_names,f_names in os.walk(path):
#	for f in f_names:
#		fname.append(os.path.join(root, f))

#print("fname = %s" %fname)
print("Finished!")



 #
 # 
 # 
 #     