import bottle
from model import Proracun

DATOTEKA_S_STANJEM = 'stanje.json'
try:
    proracun = Proracun.nalozi_stanje(DATOTEKA_S_STANJEM)
except:
    proracun = Proracun()

@bottle.get('/')
def zacetna_stran():
    return bottle.template('zacetna_stran.html', proracun=proracun)

@bottle.get('/zivjo/<ime>/')
def pozdravi(ime):
    return bottle.template('pozdrav.html',
        ime_osebe=ime
    )

@bottle.post('/dodaj/')
def dodaj_racun():
    proracun.nov_racun(bottle.request.forms.getunicode('ime'))
    bottle.redirect('/')

bottle.run(debug=True, reloader=True)