colors = ['red', 'blue', 'brown', 'yellow', 'grey']

from turtle import *

for n in range (3,8):
    color(colors[n-3])
    for j in range(n):
        forward(60)
        left(360/n)

