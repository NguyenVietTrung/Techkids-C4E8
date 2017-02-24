from turtle import *
bgcolor("lightgreen")
color("blue")
pensize(2)
speed(-1)
def ds(n, side):
    for i in range(n):
        for j in range(4):
            forward(side)
            left(90)
        left(360/n)

ds(20, 50)        
