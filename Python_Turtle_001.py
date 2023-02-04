# https://www.geeksforgeeks.org/turtle-programming-python/

import turtle
import math
import random

bob = turtle.Turtle()
bob.color("red", "yellow")
bob.speed(10)
bob.begin_fill()

for i in range(200):
    bob.forward(10)
    bob.left(math.sin(i/10)*25)
    bob.left(20)

bob.end_fill()

turtle.done()
