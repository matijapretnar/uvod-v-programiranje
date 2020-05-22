from datetime import date
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


@bottle.post('/dodaj-preliv/')
def dodaj_preliv():
    znesek = int(bottle.request.forms['znesek'])
    datum = date.today().strftime('%Y-%m-%d')
    opis = bottle.request.forms.getunicode('opis')
    racun = proracun.poisci_racun(bottle.request.forms['racun'] or None)
    kuverta = proracun.poisci_kuverto(bottle.request.forms['kuverta'] or None)
    proracun.nov_preliv(znesek, datum, opis, racun, kuverta)
    bottle.redirect('/')

@bottle.post('/premakni-denar/')
def premakni_denar():
    kuverta1 = proracun.poisci_kuverto(bottle.request.forms['kuverta1'] or None)
    kuverta2 = proracun.poisci_kuverto(bottle.request.forms['kuverta2'] or None)
    znesek = int(bottle.request.forms['znesek'])
    proracun.premakni_denar(kuverta1, kuverta2, znesek)
    bottle.redirect('/')

@bottle.post('/dodaj-racun/')
def dodaj_racun():
    proracun.nov_racun(bottle.request.forms.getunicode('ime'))
    bottle.redirect('/')

@bottle.post('/dodaj-kuverto/')
def dodaj_kuverto():
    proracun.nova_kuverta(bottle.request.forms.getunicode('ime'))
    bottle.redirect('/')

@bottle.post('/odstrani-kuverto/')
def odstrani_kuverto():
    kuverta = proracun.poisci_kuverto(bottle.request.forms['kuverta'] or None)
    proracun.odstrani_kuverto(kuverta)
    bottle.redirect('/')


bottle.run(debug=True, reloader=True)