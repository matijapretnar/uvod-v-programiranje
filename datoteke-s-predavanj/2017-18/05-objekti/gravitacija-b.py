import turtle

def razdalja_med_telesoma(telo1, telo2):
    return ((telo1.x - telo2.x) ** 2 + (telo1.y - telo2.y) ** 2) ** 0.5

def vplivaj_s_teznostjo(telo1, telo2):
    '''Spremeni hitrost drugega telesa pod vplivom težnosti prvega.'''
    razdalja = razdalja_med_telesoma(telo1, telo2)
    velikost_pospeska = telo1.masa / (razdalja ** 2)
    pospesek_x = (telo1.x - telo2.x) / razdalja * velikost_pospeska
    pospesek_y = (telo1.y - telo2.y) / razdalja * velikost_pospeska
    telo2.vx += pospesek_x * dt
    telo2.vy += pospesek_y * dt

def premakni(telo):
    telo.x += telo.vx * dt
    telo.y += telo.vy * dt
    telo.goto(telo.x, telo.y)

dt = 0.1
sonce = turtle.Turtle()
sonce.shape('circle')
sonce.color('orange')
sonce.shapesize(2, 2)
sonce.goto(0, 0)
sonce.masa = 100000
sonce.x, sonce.y = 0, 0
sonce.vx, sonce.vy = 0, 0
zemlja = turtle.Turtle()
zemlja.shape('circle')
zemlja.color('green')
zemlja.masa = 200
zemlja.x, zemlja.y = 200, 0
zemlja.vx, zemlja.vy = 0, 20
zemlja.goto(200, 0)
zemlja.clear()
mars = turtle.Turtle()
mars.shape('circle')
mars.color('green')
mars.masa = 200
mars.x, mars.y = -150, 50
mars.vx, mars.vy = 5, 20
mars.goto(-200, 0)
mars.clear()

osoncje = [zemlja, mars, sonce]
while True:
    for telo1 in osoncje:
        for telo2 in osoncje:
            if telo1 != telo2:
                vplivaj_s_teznostjo(telo1, telo2)
    for telo in osoncje:
        premakni(telo)
