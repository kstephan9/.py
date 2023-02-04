import math,turtle,threading

sine_line=[]
cos_line=[]
amp=100


for x in range(0,1000,10):
   sine_line.append((x/10,amp*math.sin(math.radians(x))))
   cos_line.append((x/10,amp*math.cos(math.radians(x))))

window=turtle.Screen()

myT=turtle.Turtle()
myT2=turtle.Turtle()

for x in range(0,len(sine_line)):
   myT2.setpos(cos_line[x][0],cos_line[x][1])
   myT.setpos(sine_line[x][0],sine_line[x][1])


turtle.done()
#turtle.done()
