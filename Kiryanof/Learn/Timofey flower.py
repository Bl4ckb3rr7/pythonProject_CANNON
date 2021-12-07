import turtle

turtle.shape('turtle')

turtle.speed(999)

def flower(a):
    number_of_petals = 360 / a
    for j in range(a):
        turtle.left(number_of_petals)
        for i in range(360):
            turtle.left(1)
            turtle.forward(1)

def inf(a, y, c):
    for j in range(1, c):
        turtle.left(180)
        for i in range(360):
            turtle.left(a + i)
            turtle.forward(y + i)
        turtle.left(180)
        for k in range(360):
            turtle.left(a + k)
            turtle.forward(y + j)


inf(1, 1, 2)
