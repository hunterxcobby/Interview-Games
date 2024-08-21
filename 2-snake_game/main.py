#!/usr/bin/python3

import turtle 

# setup the screen
wn = turtle.Screen()
wn.title("Snake Game By Cobby")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

wn.mainloop()