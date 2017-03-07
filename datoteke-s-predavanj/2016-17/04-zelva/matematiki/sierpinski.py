import turtle

zelva = turtle.Turtle()

def sierpinski(n, dolzina):
    '''Nariše trikotnik Sierpinskega reda n.'''
    for _ in range(3):
        if n > 0:
            sierpinski(n - 1, dolzina / 2)
        zelva.forward(dolzina)
        zelva.left(120)


def krivulja(n, dolzina):
    if n == 0:
        zelva.forward(dolzina)
    else:
        zelva.left(60)
        krivulja(n - 1, dolzina / 2)
        zelva.right(60)
        krivulja(n - 1, dolzina / 2)
        zelva.right(60)
        krivulja(n - 1, dolzina / 2)
        zelva.left(60)
