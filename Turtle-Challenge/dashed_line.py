from turtle import Turtle, Screen

turtle_obj = Turtle()
turtle_obj.color("red", "green")

for _ in range(15):
    turtle_obj.forward(10)
    turtle_obj.penup()  # Pull the pen down – drawing when moving
    turtle_obj.forward(10)
    turtle_obj.pendown()  # Pull the pen up – no drawing when moving.

screen = Screen()
screen.exitonclick()
