import random

poskusi, v_krogu = 0, 0
while True:
    poskusi += 1
    x, y = random.random(), random.random()
    if x ** 2 + y ** 2 <= 1:
        v_krogu += 1
    if poskusi % 10000 == 0:
        pi = 4 * v_krogu / poskusi
        print(poskusi, pi)
