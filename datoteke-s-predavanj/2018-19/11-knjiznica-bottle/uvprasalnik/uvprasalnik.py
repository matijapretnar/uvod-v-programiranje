import bottle
from model import ZbirkaVprasanj, Vprasanje, Odgovor

zbirka_vprasanj = ZbirkaVprasanj(ime='UVP 2018/19', vprasanja=[
    Vprasanje('Kakšno je danes vreme?', [
        Odgovor('sončno'),
        Odgovor('oblačno'),
        Odgovor('deževno'),
    ]),
    Vprasanje('Kakšno je bilo včeraj vreme?', [
        Odgovor('ne vem, sem bil ves dan na faksu'),
        Odgovor('mi je vseeno, sem matematik'),
    ]),
])
zbirka_vprasanj.odpri_vprasanje(0)

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
