from turtle import Turtle as tr
import random as rd


class Food(tr):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = rd.randint(-200, 200)
        random_y = rd.randint(-200, 200)
        self.goto(random_x, random_y)
