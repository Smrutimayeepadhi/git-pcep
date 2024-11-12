#when you install the cologram package make sure that you write 'colorgram' not cologram
"""import colorgram

colors = colorgram.extract('166855_001.jpg', 10)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color  = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)"""

from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

tim.colormode(255)
image_color = [(172, 161, 150), (239, 230, 234), (217, 225, 233), (148, 84, 48), (229, 237, 233), (51, 105, 140), (135, 164, 184), (230, 202, 116), (8, 41, 71)]

tim.dot(30,random.choice(image_color))
screen.exitonclick()
