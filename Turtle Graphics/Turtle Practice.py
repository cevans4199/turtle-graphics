from turtle import *

def draw_star (x,y, points, line, fill):
    penup ()
    goto(x,y)
    pendown()

    turn=180 - (360 / points)

    color (line, fill)

    begin_fill ()
    for i in range (points):
        forward(200)
        left(turn)
    end_fill()

speed(10)

draw_star (0,0, 102, "blue", "red")
draw_star (100,100,102, "green", "purple")
draw_star (200,200, 102, "black", "purple")
draw_star (300,300,102, "green", "black")
