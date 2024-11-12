from turtle import Turtle, Screen
import random
tim = Turtle()
screen = Screen()
screen.colormode(255)
def rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)  
    b = random.randint(0, 255)
    rgb_color = (r, g, b)    
    return rgb_color  
tim.speed("fastest")       
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.circle(70)
        tim.color(rgb())
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)# for changing and getting the heading
draw_spirograph(5)

screen.exitonclick()