import turtle

zemlja = turtle.Turtle()
zemlja.shape('circle')
zemlja.color('darkblue')
zemlja.speed(0)
sonce = turtle.Turtle()
sonce.shape('circle')
sonce.color('red')
sonce.shapesize(2, 2)
sonce.speed(0)

m_zemlje = 1
m_sonca = 100000

x_sonca, y_sonca = 0, 0
x_zemlje, y_zemlje = 100, 0
vx_sonca, vy_sonca = 0, 0
vx_zemlje, vy_zemlje = 0, 30

dt = 0.1

while True:
    zemlja.goto(x_zemlje, y_zemlje)
    sonce.goto(x_sonca, y_sonca)
    m_sonca *= 0.9995

    dx = x_sonca - x_zemlje
    dy = y_sonca - y_zemlje
    d = (dx ** 2 + dy ** 2) ** 0.5
    f = (m_zemlje * m_sonca) / d ** 2
    fx = f * dx / d
    fy = f * dy / d

    vx_zemlje += fx / m_zemlje * dt
    vy_zemlje += fy / m_zemlje * dt
    vx_sonca -= fx / m_sonca * dt
    vy_sonca -= fy / m_sonca * dt

    x_zemlje += vx_zemlje * dt
    y_zemlje += vy_zemlje * dt
    x_sonca += vx_sonca * dt
    y_sonca += vy_sonca * dt
