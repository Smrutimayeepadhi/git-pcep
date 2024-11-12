from turtle import Turtle, Screen
from tkinter import *
import random
tim = Turtle()
screen = Screen()
screen.colormode(255)


def rgb_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_rgb = (r, g, b)#tuple immutable
    return random_rgb


directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fast")

for _ in range(50):
    tim.forward(30)
    tim.color(rgb_color())
    tim.setheading(random.choice(directions))

screen.exitonclick()
