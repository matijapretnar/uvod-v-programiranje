import turtle

zelva = turtle.Turtle()

def sierpinski(n, dolzina=100):
    if n == 0:
        zelva.forward(dolzina)
        zelva.left(120)
        zelva.forward(dolzina)
        zelva.left(120)
        zelva.forward(dolzina)
        zelva.left(120)
    else:
        sierpinski(n - 1, dolzina / 2)
        zelva.left(60)
        zelva.forward(dolzina / 2)
        zelva.right(60)
        sierpinski(n - 1, dolzina / 2)
        zelva.right(60)
        zelva.forward(dolzina / 2)
        zelva.left(60)
        sierpinski(n - 1, dolzina / 2)
        zelva.left(180)
        zelva.forward(dolzina / 2)
        zelva.left(180)

sierpinski(1)