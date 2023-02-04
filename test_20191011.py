asdfasdfs
#
#
#

import os
import shutil
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# Prints: C:\Users\sdkca\Desktop
print("The Desktop path is: " + desktop)

def CreateAFolderIfNecessary(mypnf):
    if os.path.isdir(mypnf):
        print("mypnf: ", mypnf, " was a folder")
        return
    if os.path.exists(mypnf):
        print("pnf: ", mypnf, " existed.")
    else:
        print("pnf: ", mypnf, " did not exist.")
    return





dn = 'Excel'
pnf = os.path.join(desktop, dn)
#print(pnf)

CreateAFolderIfNecessary(pnf)

dn = 'aContainer'

#print(pnf)

CreateAFolderIfNecessary(pnf)

count = 0
my_extension = "txt"
my_extension_dot = ".txt"
my_target = my_extension
for (dirname, dirs, files) in os.walk(desktop):
    for filename in files:
        if filename.lower().endswith(my_extension):
            count = count + 1
            source = os.path.join(desktop, filename)
            target = os.path.join(desktop+"\\"+my_target, filename)
            #print(count, " ", filename, " ", source, target)
            if os.path.exists(target):
                print("target:", target, " exists" )
            else:
                print("dne source:", source, " target:", target)
                shutil.move(source, target)
print("count: ", count)



