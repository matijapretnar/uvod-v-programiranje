import turtle

z = turtle.Turtle()
def sierpinski(n, dolzina):
    if n > 0:
        for _ in range(3):
            sierpinski(n - 1, dolzina / 2)
            z.forward(dolzina)
            z.left(120)
    else:
        pass

def krivulja(n, dolzina, pojdi_desno, barva):
    z.color(barva)
    if n > 0:
        if pojdi_desno:
            z.right(60)
            krivulja(n - 1, dolzina / 2, not pojdi_desno, 'red')
            z.left(60)
            krivulja(n - 1, dolzina / 2, pojdi_desno, 'green')
            z.left(60)
            krivulja(n - 1, dolzina / 2, not pojdi_desno, 'blue')
            z.right(60)
        else:
            z.left(60)
            krivulja(n - 1, dolzina / 2, not pojdi_desno, 'red')
            z.right(60)
            krivulja(n - 1, dolzina / 2, pojdi_desno, 'green')
            z.right(60)
            krivulja(n - 1, dolzina / 2, not pojdi_desno, 'blue')
            z.left(60)
    else:
        z.forward(dolzina)

krivulja(5, 100, True, 'red')