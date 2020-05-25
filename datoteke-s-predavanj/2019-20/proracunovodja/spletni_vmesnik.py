from datetime import date
import bottle
from model import Proracun

DATOTEKA_S_STANJEM = 'stanje.json'
try:
    proracun = Proracun.nalozi_stanje(DATOTEKA_S_STANJEM)
except:
    proracun = Proracun()

def poisci_racun(ime_polja):
    ime_racuna = bottle.request.forms.getunicode(ime_polja)
    return proracun.poisci_racun(ime_racuna)

def poisci_kuverto(ime_polja):
    ime_kuverte = bottle.request.forms.getunicode(ime_polja)
    return proracun.poisci_kuverto(ime_kuverte or None)

@bottle.get('/')
def zacetna_stran():
    bottle.redirect('/proracun/')

@bottle.get('/proracun/')
def nacrtovanje_proracuna():
    return bottle.template('proracun.html', proracun=proracun)

@bottle.get('/analiza/')
def analiza():
    return bottle.template('analiza.html')

@bottle.get('/pomoc/')
def pomoc():
    return bottle.template('pomoc.html')


@bottle.post('/dodaj-preliv/')
def dodaj_preliv():
    znesek = int(bottle.request.forms['znesek'])
    datum = date.today().strftime('%Y-%m-%d')
    opis = bottle.request.forms.getunicode('opis')
    racun = poisci_racun('racun')
    kuverta = poisci_kuverto('kuverta')
    proracun.nov_preliv(znesek, datum, opis, racun, kuverta)
    bottle.redirect('/')

@bottle.post('/premakni-denar/')
def premakni_denar():
    kuverta1 = poisci_kuverto('kuverta1')
    kuverta2 = poisci_kuverto('kuverta2')
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
    kuverta = poisci_kuverto('kuverta')
    proracun.odstrani_kuverto(kuverta)
    bottle.redirect('/')


bottle.run(debug=True, reloader=True)