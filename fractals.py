# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 21:16:59 2021

@author: somak
"""

import turtle

bob = turtle.Turtle()



"""

def draw(t,length,n):
    if n==0:
        return
    angle=60
    t.fd(length*n)
    t.lt(angle)
    draw(t,length,n-1)
    t.rt(2*angle)
    draw(t,length,n-1)
    t.lt(angle)
    t.bk(length*n)
    
    
draw(bob,5,5)

"""


def koch(t,x):
    if x<=15:
        t.fd(x)
    else:
        koch(t,x/3)
        t.lt(60)
        koch(t,x/3)
        t.rt(120)
        koch(t,x/3)
        t.lt(60)
        koch(t,x/3)
        
koch(bob,500)   
        
        
        
turtle.exitonclick()
    

turtle.mainloop() 
turtle.bye()