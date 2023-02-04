# https://www.geeksforgeeks.org/turtle-programming-python/

from turtle import *
import time

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

def DrawSquare(length=1):

    oldPos = pos()
    setheading(0)
    pendown()

    for n in range(0, 4):
        forward(length)
        left(90)

    setpos(oldPos)

def Scale(x=1, y=1):
    screen = Screen()
    screen.setworldcoordinates(- (SCREEN_WIDTH / (x * 2)), - (SCREEN_HEIGHT / (y * 2)), (SCREEN_WIDTH / (x * 2)), (SCREEN_HEIGHT / (y * 2)))

setup(SCREEN_WIDTH, SCREEN_HEIGHT)
mode("world")

penup()
goto(-25, -25)

# TESTS

Scale(1, 1) # normal size
DrawSquare(50)
time.sleep(2)

Scale(1, 2)  # twice as tall
time.sleep(2)

Scale(2, 1)  # twice as wide
time.sleep(2)

Scale(2, 2)  # twice as big
time.sleep(2)

Scale(1, 1)  # back to normal

done()

#Just set Scale(1, 2) to make anything you draw twice as big in the Y dimension. Either before or after you draw it.
