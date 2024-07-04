import turtle

screen = turtle.Screen()
screen.bgcolor("white")

tur = turtle.Turtle()
tur.speed(0)
tur.hideturtle()

def draw_petal(size, color):
    tur.color(color)
    tur.begin_fill()
    tur.circle(size, 60)
    tur.left(120)
    tur.circle(size, 60)
    tur.end_fill()

def draw_stem():
    tur.color("green")
    tur.pensize(5)
    tur.right(90)
    tur.forward(200)
    tur.pensize(1)

tur.penup()
tur.goto(0, 0)
tur.pendown()

for _ in range(6):
    draw_petal(100, "red")
    tur.left(60)

tur.penup()
tur.goto(0, 0)
tur.pendown()
tur.right(30)
for _ in range(6):
    draw_petal(80, "orange")
    tur.left(60)

tur.penup()
tur.goto(0, 0)
tur.pendown()
tur.right(30)
for _ in range(6):
    draw_petal(60, "yellow")
    tur.left(60)

tur.penup()
tur.goto(0, -30)
tur.setheading(270)
tur.forward(65)
tur.pendown()
tur.left(90)

draw_stem()

tur.penup()
tur.goto(0, -230)
tur.pendown()

tur.hideturtle()
turtle.done()