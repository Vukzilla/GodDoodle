import turtle
import random

turtle.pensize(10)
turtle.speed('fastest')       

def click():
    direction = random.randint(1,2)
    angle = random.randint(30,360)
    distance = random.randint(50,200)
    color = random.randint(1,4)

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
    
    
    if color == 1:
        turtle.color('red')
    if color == 2:
        turtle.color('green')
    if color == 3:
        turtle.color('blue')
    if color == 4:
        turtle.color('black')

    turtle.penup()

turtle.listen()

turtle.onkey(click, 'space')

turtle.mainloop()
