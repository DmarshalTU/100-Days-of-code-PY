from turtle import Turtle, Screen

tr = Turtle()
sc = Screen()


def move_fd():
    tr.fd(10)


def turn_lt():
    tr.lt(10)


def turn_rt():
    tr.rt(10)


def move_bk():
    tr.bk(10)


def clr_scr():
    tr.clear()
    tr.penup()
    tr.home()
    tr.pendown()


sc.listen()
sc.onkey(move_fd, 'w')
sc.onkey(turn_lt, 'a')
sc.onkey(turn_rt, 'd')
sc.onkey(move_bk, 's')
sc.onkey(clr_scr, 'c')

sc.exitonclick()
