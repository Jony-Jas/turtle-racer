from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=120 - (i * 50))
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            if turtle.pencolor() != user_bet:
                print(f"You've Lost! The {turtle.pencolor()} is the winner")
            else:
                print(f"You've won! The {turtle.pencolor()} is the winner")
            is_race_on = False
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
