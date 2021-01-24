from turtle import Turtle, Screen
import turtle as t
import random as rd

# global attributes
tr = Turtle()

tr.shape('turtle')
tr.speed('normal')
t.colormode(255)


# tr.pensize(15)


# # square
# for _ in range(0, 15):
#     tr.pendown()
#     tr.forward(10)
#     tr.penup()
#     tr.forward(10)


# # shapes
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#
#     for _ in range(num_sides):
#         tr.forward(100)
#         tr.right(angle)
#
#
# for _ in range(3, 11):
#     draw_shape(_)
#     tr.pencolor(rd.choice(colours))

def change_color():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    color = (r, g, b)
    return color


# # random walk
# def random_walk():
#     fd = 20
#     ag = [
#         0,
#         90,
#         180,
#         270
#     ]
#     tr.setheading(rd.choice(ag))
#     tr.forward(fd)
#
#
# for _ in range(1, 200):
#     random_walk()
#     tr.color(change_color())


def spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tr.color(change_color())
        tr.circle(100)
        tr.setheading(tr.heading() + size_of_gap)


spirograph(10)
# exit
screen = Screen()
screen.exitonclick()
