from turtle import Turtle, Screen

turtle_obj = Turtle()

turtle_obj.color("blue")

for _ in range(4):

    turtle_obj.forward(100)
    turtle_obj.left(90)

Screen = Screen()

Screen.exitonclick()
