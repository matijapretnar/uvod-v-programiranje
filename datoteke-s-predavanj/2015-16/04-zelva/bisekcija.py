import turtle

MERILO = 100
a = -3
b = 3

def narisi_puscico(zelva, velikost=5):
    zelva.right(90)
    zelva.forward(velikost)
    zelva.left(135)
    zelva.forward(velikost * 2 ** 0.5)
    zelva.left(90)
    zelva.forward(velikost * 2 ** 0.5)
    zelva.left(135)
    zelva.forward(velikost)
    zelva.left(90)

def poslji(zelva, x, y):
    x *= MERILO
    y *= MERILO
    zelva.setheading(zelva.towards(x, y))
    zelva.goto(x, y)


import math
f = math.cos

zelva = turtle.Turtle()
zelva.speed(10)

zelva.up()
poslji(zelva, a, 0)
zelva.down()
poslji(zelva, b, 0)
narisi_puscico(zelva)
zelva.up()
poslji(zelva, 0, a)
zelva.left(90)
zelva.down()
poslji(zelva, 0, b)
narisi_puscico(zelva)
zelva.up()
poslji(zelva, a, f(a))
zelva.down()

for i in range(a * MERILO, b * MERILO + 1):
    x = i / MERILO
    y = f(x)
    poslji(zelva, x, y)

# eps = 0.001

# while b - a < eps:
