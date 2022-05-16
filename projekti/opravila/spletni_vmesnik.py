import bottle
from datetime import date
from model import Stanje, Opravilo, Kategorija


IME_DATOTEKE = "stanje.json"
try:
    stanje = Stanje.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    stanje = Stanje(kategorije=[])


def url_kategorije(id_kategorije):
    return f"/kategorija/{id_kategorije}/"



@bottle.get("/")
def zacetna_stran():
    return bottle.template(
        "zacetna_stran.tpl",
        kategorije=stanje.kategorije,
    )

@bottle.get("/kategorija/<id_kategorije:int>/")
def prikazi_kategorijo(id_kategorije):
    kategorija = stanje.kategorije[id_kategorije]
    return bottle.template(
        "kategorija.tpl",
        kategorije=stanje.kategorije,
        aktualna_kategorija=kategorija,
        id_aktualne_kategorije=id_kategorije,
    )


@bottle.get("/dodaj-kategorijo/")
def dodaj_kategorijo_get():
    return bottle.template(
        "dodaj_kategorijo.tpl", napake={}, polja={}
    )


@bottle.post("/dodaj-kategorijo/")
def dodaj_kategorijo_post():
    ime = bottle.request.forms.getunicode("ime")
    kategorija = Kategorija(ime, opravila=[])
    napake = stanje.preveri_podatke_nove_kategorije(kategorija)
    if napake:
        polja = {"ime": ime}
        return bottle.template("dodaj_kategorijo.tpl", napake=napake, polja=polja)
    else:
        id_kategorije = stanje.dodaj_kategorijo(kategorija)
        bottle.redirect(url_kategorije(id_kategorije))


@bottle.post("/opravi/<id_kategorije:int>/<id_opravila:int>/")
def opravi(id_kategorije, id_opravila):
    kategorija = stanje.kategorije[id_kategorije]
    opravilo = kategorija.opravila[id_opravila]
    opravilo.opravi()
    bottle.redirect(url_kategorije(id_kategorije))

@bottle.post("/dodaj-opravilo/<id_kategorije:int>/")
def dodaj_opravilo(id_kategorije):
    kategorija = stanje.kategorije[id_kategorije]
    opis = bottle.request.forms.getunicode("opis")
    if bottle.request.forms["rok"]:
        rok = date.fromisoformat(bottle.request.forms["rok"])
    else:
        rok = None
    opravilo = Opravilo(opis, rok)
    kategorija.dodaj_opravilo(opravilo)
    bottle.redirect(url_kategorije(id_kategorije))


@bottle.error(404)
def error_404(error):
    return "Ta stran ne obstaja!"


bottle.run(debug=True, reloader=True)
