import turtle

zemlja = turtle.Turtle()
zemlja.shape('circle')
zemlja.color('blue')
m_zemlje = 1
x_zemlje, y_zemlje = 150, 0
vx_zemlje, vy_zemlje = 0, 30

sonce = turtle.Turtle()
sonce.shape('circle')
sonce.shapesize(2, 2)
sonce.color('red')
m_sonca = 100000
x_sonca, y_sonca = 0, 0
vx_sonca, vy_sonca = 0, 0

dt = 0.01
zemlja.goto(x_zemlje, y_zemlje)
sonce.goto(x_sonca, y_sonca)
zemlja.clear()
sonce.clear()

while True:
    m_sonca *= 1.01
    zemlja.goto(x_zemlje, y_zemlje)
    sonce.goto(x_sonca, y_sonca)

    dx = x_zemlje - x_sonca
    dy = y_zemlje - y_sonca
    d = (dx ** 2 + dy ** 2) ** 0.5
    f = m_zemlje * m_sonca / d ** 2

    vx_zemlje -= dt * f * dx / (d * m_zemlje)
    vy_zemlje -= dt * f * dy / (d * m_zemlje)
    vx_sonca += dt * f * dx / (d * m_sonca)
    vy_sonca += dt * f * dy / (d * m_sonca)

    x_zemlje += dt * vx_zemlje
    y_zemlje += dt * vy_zemlje
    x_sonca += dt * vx_sonca
    y_sonca += dt * vy_sonca

