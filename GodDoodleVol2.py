import turtle
import random

width = 1000
height= 1000

screen = turtle.Screen()
screen.setup(width, height)

turtle.Screen().title("God Doodle")

turtle.pensize(10)
turtle.speed('fastest')       

def click():
    turtle.color('yellow')

    x = random.randint(-width, width)
    y = random.randint(-height, height)

    direction = random.randint(1,2)
    angle = random.randint(1,360)
    distance = random.randint(50,500)

    turtle.goto(x, y)

    turtle.pendown()

    if direction == 1:
        turtle.forward(distance)
        dir2 = random.randint(1,2)
        if dir2 == 1:
            turtle.left(angle)
        if dir2 == 2:
            turtle.right(angle)
    if direction == 2:
        turtle.backward(distance)
        dir2 = random.randint(1,2)
        if dir2 == 1:
            turtle.left(angle)
        if dir2 == 2:
            turtle.right(angle)



    turtle.penup()

turtle.listen()

turtle.onkey(click, 'space')
turtle.onkeypress(click, 'space')

turtle.mainloop()
