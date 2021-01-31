import turtle
import math
bob = turtle.Turtle()

def arc(t,radius,angle):
    arc_length=2*math.pi*radius*angle/360
    n=int(arc_length/3)
    step_length=arc_length/n
    step_angle=angle/n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

"""
for i in range(10):
    arc(bob,100,72)
    bob.lt(108)
    arc(bob,100,72)
"""

"""
for i in range(7):
    arc(bob,100,360/7)
    bob.lt(180-2*180/7)
    arc(bob,100,360/7)
    bob.lt(180/7)
"""

for i in range(20):
    arc(bob,300,18)
    bob.lt(162)
    arc(bob,300,18)

turtle.mainloop()
