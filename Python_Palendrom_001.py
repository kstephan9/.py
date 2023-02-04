import pandas as pd
import random
nn = 2

# using list comprehension + randrange()
# to generate random number list
r = [random.randrange(1, 1000, 1) for i in range(1000)]


#r = range(0, 1000)
#print(r)
i1 = 0
i2 = 0
for rx in r:
    rx_str = str(rx)
    rx_str = rx_str.zfill(3)
    rx_rev = rx_str[::-1]
    i1 = i1 + 1
    IsOrIsNot = "N"
    #print("rx_str:<", rx_str, "> rx_rev:<", rx_rev, ">")
    if rx_str == rx_rev:
        IsOrIsNot = "Y"
        i2 = i2 + 1

#    print('{0:0>4}\t{1:0>3}\t{2:0>3}\t{3}'.format(i1, rx_str, rx_rev, IsOrIsNot))

#s = "nora"
#s_str = str(s)
#print(s, s_str.zfill(2))
#sf = s_str.zfill(2)
#print(sf, sf[::-1])

print(i2)
