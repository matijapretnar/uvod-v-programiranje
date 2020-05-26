from datetime import date
import bottle
import os
import random
from model import Proracun

proracuni = {}
for ime_datoteke in os.listdir('shranjeni_proracuni'):
    st_uporabnika, koncnica = os.path.splitext(ime_datoteke)
    proracuni[st_uporabnika] = Proracun.nalozi_stanje(os.path.join('shranjeni_proracuni', ime_datoteke))

def poisci_racun(ime_polja):
    ime_racuna = bottle.request.forms.getunicode(ime_polja)
    proracun = proracun_uporabnika()
    return proracun.poisci_racun(ime_racuna)

def poisci_kuverto(ime_polja):
    ime_kuverte = bottle.request.forms.getunicode(ime_polja)
    proracun = proracun_uporabnika()
    return proracun.poisci_kuverto(ime_kuverte or None)

def proracun_uporabnika():
    st_uporabnika = bottle.request.get_cookie('st_uporabnika')
    if st_uporabnika is None:
        st_uporabnika = str(random.randint(0, 2 ** 40))
        proracuni[st_uporabnika] = Proracun()
        bottle.response.set_cookie('st_uporabnika', st_uporabnika, path='/')
    return proracuni[st_uporabnika]

def shrani_proracun_uporabnika():
    st_uporabnika = bottle.request.get_cookie('st_uporabnika')
    proracun = proracuni[st_uporabnika]
    proracun.shrani_stanje(os.path.join('shranjeni_proracuni', f'{st_uporabnika}.json'))

@bottle.get('/')
def zacetna_stran():
    bottle.redirect('/proracun/')

@bottle.get('/proracun/')
def nacrtovanje_proracuna():
    proracun = proracun_uporabnika()
    return bottle.template('proracun.html', proracun=proracun)

@bottle.get('/analiza/')
def analiza():
    return bottle.template('analiza.html')

@bottle.get('/pomoc/')
def pomoc():
    return bottle.template('pomoc.html')


@bottle.post('/dodaj-preliv/')
def dodaj_preliv():
    proracun = proracun_uporabnika()
    znesek = int(bottle.request.forms['znesek'])
    datum = date.today().strftime('%Y-%m-%d')
    opis = bottle.request.forms.getunicode('opis')
    racun = poisci_racun('racun')
    kuverta = poisci_kuverto('kuverta')
    proracun.nov_preliv(znesek, datum, opis, racun, kuverta)
    shrani_proracun_uporabnika()
    bottle.redirect('/')

@bottle.post('/premakni-denar/')
def premakni_denar():
    proracun = proracun_uporabnika()
    kuverta1 = poisci_kuverto('kuverta1')
    kuverta2 = poisci_kuverto('kuverta2')
    znesek = int(bottle.request.forms['znesek'])
    proracun.premakni_denar(kuverta1, kuverta2, znesek)
    shrani_proracun_uporabnika()
    bottle.redirect('/')

@bottle.post('/dodaj-racun/')
def dodaj_racun():
    proracun = proracun_uporabnika()
    proracun.nov_racun(bottle.request.forms.getunicode('ime'))
    shrani_proracun_uporabnika()
    bottle.redirect('/')

@bottle.post('/dodaj-kuverto/')
def dodaj_kuverto():
    proracun = proracun_uporabnika()
    proracun.nova_kuverta(bottle.request.forms.getunicode('ime'))
    shrani_proracun_uporabnika()
    bottle.redirect('/')

@bottle.post('/odstrani-kuverto/')
def odstrani_kuverto():
    proracun = proracun_uporabnika()
    kuverta = poisci_kuverto('kuverta')
    proracun.odstrani_kuverto(kuverta)
    shrani_proracun_uporabnika()
    bottle.redirect('/')


bottle.run(debug=True, reloader=True)