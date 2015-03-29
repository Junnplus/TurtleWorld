from swampy.TurtleWorld import *
import math

def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)

def polygon(t, n, length):
    angle = 360/n
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 2
    step_length = arc_length / n
    step_angle = float(angle) / n
    
    for i in range(n):
        fd(t,step_length)
        lt(t,step_angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)
