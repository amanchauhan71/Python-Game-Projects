from turtle import Turtle, Screen
import random


turtle_obj = Turtle()
turtle_obj.color("red", "green")
colours = ["dark goldenrod", "gold", "peru", "saddle brown", "deep pink", "plum", "purple"]


def draw_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        turtle_obj.forward(100)
        turtle_obj.left(angle)


for shape_sides in range(3, 11):
    turtle_obj.color(random.choice(colours))
    draw_shapes(shape_sides)

screen = Screen()
screen.exitonclick()
