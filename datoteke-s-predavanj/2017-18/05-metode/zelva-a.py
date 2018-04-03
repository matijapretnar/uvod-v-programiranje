import turtle

zelva = turtle.Turtle()
zelva.forward(100)

def kochova_krivulja(n, d):
    if n == 0:
        zelva.forward(d)
    else:
        kochova_krivulja(n - 1, d / 3)
        zelva.left(60)
        kochova_krivulja(n - 1, d / 3)
        zelva.right(120)
        kochova_krivulja(n - 1, d / 3)
        zelva.left(60)
        kochova_krivulja(n - 1, d / 3)
        
