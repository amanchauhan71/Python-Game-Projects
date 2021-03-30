import turtle as t
import random

tim = t.Turtle()  # Create Object of tuple
t.colormode(255)


def random_color():  # Generate Random Color and return in form of tuple
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

# Set the directions
for _ in range(300):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
