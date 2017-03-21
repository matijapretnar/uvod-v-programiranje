import turtle

turtle.shape('turtle')
turtle.shapesize(2, 2)
turtle.speed(6)

def narisi_veckotnik(n, d=100):
    for x in range(n):
        turtle.forward(d)
        turtle.left(360 / n)

def narisi_zvezdico(n, d=100):
    for x in range(n):
        turtle.forward(d)
        turtle.right(180 - 180 / n)
