import colorgram as cl
import turtle as t
from turtle import Turtle, Screen
import random as rd


def cl_extract():
    colors = cl.extract('image.jpg', 30)

    rgb = []

    for _ in colors:
        c = _.rgb
        tpl = (c.r, c.g, c.b)
        rgb.append(tpl)
    return rgb


tr = Turtle()
t.colormode(255)
tr.speed('fastest')
tr.hideturtle()
tr.setheading(225)
tr.penup()
tr.fd(300)
tr.setheading(0)
number_of_dots = 100

for dots in range(1, number_of_dots + 1):
    tr.dot(20, rd.choice(cl_extract()))
    tr.penup()
    tr.fd(50)

    if dots % 10 == 0:
        tr.setheading(90)
        tr.fd(50)
        tr.setheading(180)
        tr.fd(500)
        tr.setheading(0)

screen = Screen()
screen.exitonclick()
