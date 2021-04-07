from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()  # Inherit the turtle properties so no need to
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20  # Each time when you press up they move the 20 pixel
        self.goto(self.xcor(), new_y)  # Change the position

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

