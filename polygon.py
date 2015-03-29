from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()

def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)

def polygon(t, n, length):
    angle = 360/n
    for i in range(n):
        fd(t, length)
        lt(t, angle)
