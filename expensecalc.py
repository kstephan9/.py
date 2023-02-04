
exp = []
stopped = False


while not stopped:
    e = int(input("what is the expense? ") )
    
    if e!=0:
        exp.append(e)
    else:
        stopped = True

print(exp)
print("total:", sum(exp), max(exp), min(exp))    

