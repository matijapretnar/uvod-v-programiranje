import turtle

sonce = turtle.Turtle()
sonce.shape('circle')
sonce.color('orange')
sonce.shapesize(2, 2)
sonce.goto(0, 0)
sonce_m = 100000
sonce_x, sonce_y = 0, 0
sonce_vx, sonce_vy = 0, 0
zemlja = turtle.Turtle()
zemlja.shape('circle')
zemlja.color('green')
zemlja_m = 200
zemlja_x, zemlja_y = 200, 0
zemlja_vx, zemlja_vy = 0, 20
zemlja.goto(200, 0)
zemlja.clear()
dt = 0.1
while True:
    sonce.goto(sonce_x, sonce_y)
    zemlja.goto(zemlja_x, zemlja_y)
    dx = sonce_x - zemlja_x
    dy = sonce_y - zemlja_y
    razdalja = (dx ** 2 + dy ** 2) ** 0.5
    f = (zemlja_m * sonce_m) / (razdalja ** 2)
    fx = dx / razdalja * f
    fy = dy / razdalja * f
    zemlja_vx += fx / zemlja_m * dt
    zemlja_vy += fy / zemlja_m * dt
    sonce_vx -= fx / sonce_m * dt
    sonce_vy -= fy / sonce_m * dt
    zemlja_x += zemlja_vx * dt
    zemlja_y += zemlja_vy * dt
    sonce_x += sonce_vx * dt
    sonce_y += sonce_vy * dt
