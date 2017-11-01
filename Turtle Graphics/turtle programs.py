
import turtle
wn = turtle.Screen()
wn.bgcolor("light pink")
natalie = turtle.Turtle()
natalie.shape("turtle")
natalie.color("purple")
natalie.penup()
size = 20
for i in range(30):
   natalie.stamp()            
   size = size + 3          
   natalie.forward(size)
   natalie.right(24)           

import turtle

def draw_square(some_turtle):

    for i in range (1,5):
        some_turtle.forward(200)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    #Turtle courtney
    courtney  = turtle.Turtle()
    courtney.shape("turtle")
    courtney.color("lime green")
    courtney.speed(6)
    courtney.pensize(2)
    for i in range(1,37):
        draw_square(courtney)
        courtney.right(10)
    #Turtle asia
    asia = turtle.Screen()
    asia.shape("turtle")
    asia.color("blue")
    asia.speed(5)
    asia.pensize(2)
    size=1
    while (True):
        asia.forward(size)
        asia.right(91)
        size = size + 1

    window.exitonclick()

draw_art()

