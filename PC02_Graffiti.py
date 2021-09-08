#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Jade Singer
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("skyblue4")
panel.bgpic(image)

#=======Add your code here======
t = turtle.Turtle()
turtle.title("Bezos pointing at Hagrid's Hut")

t.penup()
t.goto(100,-200)
t.pendown()
#GreyRectangleChimmney
t.goto(100,-200)
t.pen(pencolor ="Gray40",fillcolor ="SeaShell3",pensize = 4, speed = 12)
t.begin_fill()

t.fd(30)
t.lt(90)
t.fd(50)
t.lt(90)
t.fd(30)
t.lt(90)
t.fd(50)
t.lt(90)

t.end_fill()

t.goto(130,-200)
#BrownRoofTriangle1
t.pen(pencolor ="sienna4",fillcolor ="sienna",pensize = 5, speed = 12)
t.begin_fill()

t.bk(100)
t.rt(120)
t.bk(100)
t.rt(120)
t.bk(100)
t.rt(120)

t.end_fill()
#GreyRectangle1
t.pen(pencolor ="Gray40",fillcolor ="SeaShell3",pensize = 4, speed = 12)
t.begin_fill()

t.bk(100)
t.rt(90)
t.fd(150)
t.rt(90)
t.bk(100)
t.rt(90)
t.fd(150)

t.end_fill()
#GreyRectangle2
t.penup()
t.goto(130,-200)
t.pendown()

t.pen(pencolor ="Gray40",fillcolor ="SeaShell3",pensize = 4, speed = 12)
t.begin_fill()

t.rt(90)
t.rt(90)
t.fd(50)
t.lt(90)
t.fd(150)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(150)
t.rt(90)
t.fd(100)

t.end_fill()

#GreyRectangleChimmney2
t.penup()
t.goto(250,-200)
t.pendown()

t.pen(pencolor ="Gray40",fillcolor ="SeaShell3",pensize = 4, speed = 12)
t.begin_fill()

t.rt(90)
t.fd(30)
t.rt(90)
t.fd(50)
t.rt(90)
t.fd(30)
t.rt(90)
t.fd(50)
t.rt(90)

t.end_fill()

#BrownRoofTriangle2
t.penup()
t.goto(130,-250)
t.pendown()
t.pen(pencolor ="sienna4",fillcolor ="sienna",pensize = 5, speed = 12)
t.begin_fill()

t.fd(150)
t.lt(120)
t.fd(150)
t.lt(120)
t.fd(150)
t.lt(120)

t.end_fill()

#Bricks1
t.pen(pencolor ="Gray40", pensize = 4, speed = 12)

t.penup()
t.goto(50,-210)
t.pendown()
t.fd(15)

t.penup()
t.goto(100,-220)
t.pendown()
t.fd(10)

t.penup()
t.goto(80,-240)
t.pendown()
t.fd(15)

t.penup()
t.goto(40,-260)
t.pendown()
t.fd(10)

t.penup()
t.goto(110,-280)
t.pendown()
t.fd(10)

t.penup()
t.goto(70,-300)
t.pendown()
t.fd(15)

t.penup()
t.goto(30,-330)
t.pendown()
t.fd(10)

t.penup()
t.goto(120,-340)
t.pendown()
t.fd(10)

#Bricks2
t.pen(pencolor ="Gray40", pensize = 4, speed = 12)

t.penup()
t.goto(130,-260)
t.pendown()
t.fd(15)

t.penup()
t.goto(270,-260)
t.pendown()
t.fd(10)

t.penup()
t.goto(260,-260)
t.pendown()
t.fd(15)

t.penup()
t.goto(140,-320)
t.pendown()
t.fd(10)

t.penup()
t.goto(180,-340)
t.pendown()
t.fd(15)

t.penup()
t.goto(250,-310)
t.pendown()
t.fd(15)

t.penup()
t.goto(260,-290)
t.pendown()
t.fd(10)

t.penup()
t.goto(200,-270)
t.pendown()
t.fd(10)

#BrownDoor1
t.penup()
t.goto(50,-319)
t.pendown()

t.pen(pencolor ="SaddleBrown",fillcolor ="SaddleBrown",pensize = 5, speed = 10)
t.begin_fill()

t.fd(20)
t.rt(90)
t.fd(30)
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(30)
t.rt(90)
t.end_fill()

#BrownDoor2
t.penup()
t.goto(210,-309)
t.pendown()

t.pen(pencolor ="SaddleBrown",fillcolor ="SaddleBrown",pensize = 5, speed = 10)
t.begin_fill()

t.fd(30)
t.rt(90)
t.fd(40)
t.rt(90)
t.fd(30)
t.rt(90)
t.fd(40)
t.rt(90)

t.end_fill()

#Window1
t.penup()
t.goto(80,-250)
t.pendown()

t.pen(pencolor ="DarkOrange4",fillcolor ="DarkGoldenrod2",pensize = 3, speed = 10)
t.begin_fill()

t.fd(20)
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(20)
t.rt(90)

t.end_fill()

#Window2
t.penup()
t.goto(135,-270)
t.pendown()

t.pen(pencolor ="DarkOrange4",fillcolor ="DarkGoldenrod2",pensize = 3, speed = 10)
t.begin_fill()

t.fd(40)
t.rt(90)
t.fd(40)
t.rt(90)
t.fd(40)
t.rt(90)
t.fd(40)


t.end_fill()
turtle.done()
#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
