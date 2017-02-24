from turtle import *
bgcolor("lightgreen")
color("pink")
shape("turtle")
def sd(number, side, thickness):
    pensize(thickness)
    for i in range(number):
        for j in range (4):
            forward(side)
            left(90)
        penup()
        goto(-10*(i+1),-10*(i+1))
        side = side + 20
        pendown()

sd(5, 20, 4)
