import bottle
from datetime import datetime
from model import ZbirkaVprasanj, Vprasanje, Odgovor

zbirka_vprasanj = ZbirkaVprasanj(ime='UVP 2018/19', datoteka='vprasanja.json')

@bottle.get('/')
def osnovna_stran():
    vprasanje = zbirka_vprasanj.trenutno_vprasanje
    return bottle.template('osnovna_stran.tpl', vprasanje=vprasanje)

@bottle.post('/glasuj/')
def glasuj():
    indeks_odgovora = int(bottle.request.forms['indeks_odgovora'])
    zbirka_vprasanj.glasuj(indeks_odgovora)
    bottle.redirect('/')


bottle.run(debug=True, reloader=True)
