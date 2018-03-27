import turtle

zelva = turtle.Turtle()
zelva2 = turtle.Turtle()
zelva2.left(120)
zelva3 = turtle.Turtle()
zelva3.right(120)
zelve = [zelva, zelva2, zelva3]

def kochova_krivulja(zelve, n, d):
    if n == 0:
        for zelva in zelve:
            zelva.forward(d)
    else:
        kochova_krivulja(zelve, n - 1, d / 3)
        for zelva in zelve:
            zelva.left(60)
        kochova_krivulja(zelve, n - 1, d / 3)
        for zelva in zelve:
            zelva.right(120)
        kochova_krivulja(zelve, n - 1, d / 3)
        for zelva in zelve:
            zelva.left(60)
        kochova_krivulja(zelve, n - 1, d / 3)

for z in zelve:
    z.speed(0)
kochova_krivulja(zelve, 5, 250)
