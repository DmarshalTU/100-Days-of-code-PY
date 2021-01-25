from turtle import Turtle, Screen
import random as rd


is_race_on = False
sc = Screen()
sc.setup(width=500, height=400)
user_bet = sc.textinput(title="Make your bet:", prompt="Enter a color: ")
colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple"
]
start_y = [-70, -40, -10, 20, 50, 80]
turtles = []
for turtle_index in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=start_y[turtle_index])
    turtles.append(new_turtle)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You've won! The {winner_color} is the winner!")
            else:
                print(f"You've lost! The {winner_color} is the winner!")
        turtle.fd(rd.randint(0, 10))

sc.exitonclick()
