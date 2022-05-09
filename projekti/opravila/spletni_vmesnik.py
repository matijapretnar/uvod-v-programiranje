import bottle
from model import Opravilo, Stanje

IME_DATOTEKE = "stanje.json"
try:
    stanje = Stanje.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    stanje = Stanje(kategorije=[])

@bottle.get("/")
def zacetna_stran():
    return bottle.template(
        "zacetna_stran.tpl",
        kategorije=stanje.kategorije
    )

@bottle.get("/pozdravi/<ime>/")
def pozdravi(ime):
    return f"<h1>Živjo, {ime}!</h1>"

@bottle.get("/kategorija/<id_kategorije:int>/")
def pokazi_kategorijo(id_kategorije):
    kategorija = stanje.kategorije[id_kategorije]
    return bottle.template(
        "kategorija.tpl",
        id_kategorije=id_kategorije,
        kategorija=kategorija
    )

@bottle.post("/opravi/<id_kategorije:int>/<id_opravila:int>/")
def opravi(id_kategorije, id_opravila):
    kategorija = stanje.kategorije[id_kategorije]
    opravilo = kategorija.opravila[id_opravila]
    opravilo.opravi()
    return bottle.redirect("/")

@bottle.post("/dodaj/<id_kategorije:int>/")
def dodaj(id_kategorije):
    kategorija = stanje.kategorije[id_kategorije]
    novo_opravilo = Opravilo(opis=bottle.request.forms["opis_novega_opravila"], rok=None)
    kategorija.dodaj_opravilo(novo_opravilo)
    return bottle.redirect("/")



bottle.run(debug=True, reloader=True)
