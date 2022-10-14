import turtle
import random

def challenge063():
    def square():
        for i in range(0, 4):
            turtle.forward(100)
            turtle.right(90)

    turtle.fillcolor('blue')
    colourlist = ['blue', 'black', 'red']
    turtle.penup()
    turtle.goto(-200, 0)
    for i in range(0, 3):
        turtle.begin_fill()
        turtle.fillcolor(colourlist[i])
        turtle.pendown()
        square()
        turtle.penup()
        turtle.forward(200)
        turtle.end_fill()

    turtle.exitonclick()


def challenge064():
    turtle.goto(0,0)
    for i in range(0,5):
        turtle.forward(100)
        turtle.right(144)
    turtle.exitonclick()


def challenge066():
    colourlist = ['blue','red','orange','yellow','black','green']
    turtle.goto(0,0)
    for i in range(0,8):
        turtle.pencolor(colourlist[random.randint(0,5)])
        turtle.forward(100)
        turtle.right(45)
    turtle.exitonclick()


def challeng067:
    turtle.goto(0,0)
    for i in range(10):
        turtle.right(36)
        for j in range(0,8):
            turtle.forward(50)
            turtle.right(45)
    turtle.exitonclick()