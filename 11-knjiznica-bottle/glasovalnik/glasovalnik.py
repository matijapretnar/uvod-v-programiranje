import bottle
from model import ZbirkaVprasanj, Vprasanje, Odgovor

zbirka_vprasanj = ZbirkaVprasanj(ime='UVP 2018/19', vprasanja=[
    Vprasanje('Kakšno je danes vreme?', [
        Odgovor('sončno'),
        Odgovor('oblačno'),
        Odgovor('deževno'),
    ]),
    Vprasanje('Kakšno bo pa jutri vreme?', [
        Odgovor('tako kot danes'),
        Odgovor('drugačno kot danes'),
    ]),
])
zbirka_vprasanj.odpri_vprasanje(0)

@bottle.get('/')
def osnovna_stran():
    vprasanje = zbirka_vprasanj.trenutno_vprasanje
    if vprasanje == None:
        return 'Trenutno ni odprtega vprašanja!'
    else:
        return bottle.template('osnovna_stran.tpl', vprasanje=vprasanje)

@bottle.post('/glasuj/')
def osnovna_stran():
    odgovor = int(bottle.request.forms['glas'])
    zbirka_vprasanj.trenutno_vprasanje.glasuj_za_odgovor(odgovor)
    redirect(...)

bottle.run(debug=True, reloader=True)