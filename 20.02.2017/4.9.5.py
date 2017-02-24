from turtle import *
bgcolor("lightgreen")
color("blue")
pensize(2)
speed(-1)

def ds1(n, side):
    for i in range(n):
        forward(side)
        left(90)
        side = side + 1
        
def ds2(n, side):
    for i in range(n):
        forward(side)
        left(70)
        side = side + 1
ds1(100, 1)
ds2(100, 1)
