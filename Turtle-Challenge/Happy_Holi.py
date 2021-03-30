from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()

screen.bgcolor("black")

tim.shape("circle")
tim.color("yellow")
tim.width(7)
tim.speed(10)
colors = ["peru", "ivory", "dark orange", "coral", "cyan", "hot pink", "gold", "ivory", "yellow", "red", "pink",
          "green", "blue", "light blue", "light green", ]


def H(size):
    tim.fd(size)
    tim.backward(size // 2)
    tim.rt(90)
    tim.fd(size // 2)
    tim.lt(90)
    tim.fd(size // 2)
    tim.backward(size)


def move(x, y):
    tim.up()
    tim.setposition(0, 0)
    tim.setheading(90)
    tim.lt(90)
    tim.fd(x)
    tim.rt(90)
    tim.fd(y)
    tim.pendown()


def A(size):
    tim.rt(19)
    tim.forward(size)
    tim.rt(141)
    tim.fd(size)
    tim.backward(size / 2)
    tim.rt(105)
    tim.fd(int(size / 3))


def P(size):
    tim.fd(size)
    tim.rt(105)
    tim.fd(size // 8)
    for i in range(8):
        tim.rt(20)
        tim.fd(size // 9)


def Y(size):
    tim.fd(size)
    tim.left(60)
    tim.fd(size // 2)
    tim.backward(size // 2)
    tim.rt(90)
    tim.fd(size // 1.5)


def O(size):
    tim.right(90)
    tim.circle(size // 2)


def L(size):
    tim.rt(90)
    tim.fd(int(size / 2))
    tim.back(int(size / 2))
    tim.lt(90)
    tim.fd(size)


def I(size):
    tim.fd(size)
    tim.rt(90)
    tim.circle(size // 8)


def Spiral():
    x = 1
    tim.speed(-30)
    while x < 260:
        tim.pencolor(colors[x % 9])
        tim.fd(10 + x)
        tim.rt(90.991)
        x = x + 1


def draw_leaf(leaf):  # cretes leaf function
    for i in range(0, 2):
        leaf.forward(90)
        leaf.right(40 + i)
        for j in range(0, 21):
            leaf.right(3)
            leaf.forward(5)
        leaf.right(145)


def draw_flower(pen):
    for i in range(0, 8):
        pen.color(colors[i % 8])
        pen.begin_fill()
        draw_leaf(pen)
        pen.end_fill()
        pen.right(10)


tim.width(1)
move(480, 240)
Spiral()
move(-480, 240)
Spiral()
tim.pencolor("cyan")
tim.width(8)
tim.width(5)
move(-450, -250)
draw_flower(tim)
move(450, -250)
draw_flower(tim)
move(102, 0)
H(60)
move(60, 0)
A(60)
move(10, 0)
P(60)
move(-20, 0)
P(60)
move(-60, 0)
Y(60)
move(70, -80)
H(60)
move(0, -80)
O(60)
move(-50, -80)
L(60)
move(-95, -80)
I(60)

screen.exitonclick()
