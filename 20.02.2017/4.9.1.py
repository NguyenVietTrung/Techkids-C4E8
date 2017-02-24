from turtle import *
bgcolor("lightgreen")
color("pink")

def sd(number, side, thickness):
    pensize(thickness)
    for i in range(number):
        for j in range (4):
            forward(side)
            left(90)
        penup()
        forward(side*2)
        pendown()

sd(5, 20, 5)
