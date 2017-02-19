colors = ['red', 'blue', 'brown', 'yellow', 'grey']

from turtle import *

for i in range(0,5):
    color(colors[i])
    begin_fill()
    for j in range(2):       
        forward(30)
        left(90)
        forward(60)
        left(90)
    forward(30)
    end_fill()
