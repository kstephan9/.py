import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
fred = turtle.Turtle()
sc = turtle.Screen()
sc.reset()

sc.setworldcoordinates(0,-1.5,360,1.5)

for angle in range(180):
    y = math.sin(math.radians(angle))
    fred.goto(angle,y)

wn.exitonclick()

