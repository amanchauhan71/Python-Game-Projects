import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():  # Generate Random Color and return in form of tuple
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")


# Draw the spiral graph by using the size gaps and taking random colors
def draw_spiral_graph(size_of_gaps):
    for _ in range(int(360 / size_of_gaps)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gaps)


draw_spiral_graph(10)  # calling spiral graphs
screen = t.Screen()
screen.exitonclick()
