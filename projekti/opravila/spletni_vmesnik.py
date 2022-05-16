import bottle
from datetime import date
from model import Stanje, Opravilo, Kategorija

SIFRIRNI_KLJUC = "To je poseben šifrirni ključ"

def ime_uporabnikove_datoteke(uporabnisko_ime):
    return f"stanja_uporabnikov/{uporabnisko_ime}.json"


def stanje_trenutnega_uporabnika():
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime", secret=SIFRIRNI_KLJUC)
    if uporabnisko_ime == None:
        bottle.redirect("/prijava/")
    else:
        uporabnisko_ime = uporabnisko_ime
    ime_datoteke = ime_uporabnikove_datoteke(uporabnisko_ime)
    try:
        stanje = Stanje.preberi_iz_datoteke(ime_datoteke)
    except FileNotFoundError:
        stanje = Stanje.preberi_iz_datoteke("primer-stanja.json")
        stanje.shrani_v_datoteko(ime_datoteke)
    return stanje

def shrani_stanje_trenutnega_uporabnika(stanje):
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime", secret=SIFRIRNI_KLJUC)
    ime_datoteke = ime_uporabnikove_datoteke(uporabnisko_ime)
    stanje.shrani_v_datoteko(ime_datoteke)

def url_kategorije(id_kategorije):
    return f"/kategorija/{id_kategorije}/"


@bottle.get("/prijava/")
def prijava_get():
    return bottle.template(
        "prijava.tpl"
    )

@bottle.post("/prijava/")
def prijava_post():
    uporabnisko_ime = bottle.request.forms.getunicode("uporabnisko_ime")
    geslo = bottle.request.forms.getunicode("geslo")
    if uporabnisko_ime == geslo[::-1]:
        bottle.response.set_cookie("uporabnisko_ime", uporabnisko_ime, path="/", secret=SIFRIRNI_KLJUC)
        bottle.redirect("/")
    else:
        return "Napaka ob prijavi"

@bottle.post("/odjava/")
def odjava_post():
    bottle.response.delete_cookie("uporabnisko_ime", path="/")
    bottle.redirect("/")


@bottle.get("/")
def zacetna_stran():
    stanje = stanje_trenutnega_uporabnika()
    return bottle.template(
        "zacetna_stran.tpl",
        kategorije=stanje.kategorije,
    )

@bottle.get("/kategorija/<id_kategorije:int>/")
def prikazi_kategorijo(id_kategorije):
    stanje = stanje_trenutnega_uporabnika()
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
    stanje = stanje_trenutnega_uporabnika()
    ime = bottle.request.forms.getunicode("ime")
    kategorija = Kategorija(ime, opravila=[])
    napake = stanje.preveri_podatke_nove_kategorije(kategorija)
    if napake:
        polja = {"ime": ime}
        return bottle.template("dodaj_kategorijo.tpl", napake=napake, polja=polja)
    else:
        id_kategorije = stanje.dodaj_kategorijo(kategorija)
        shrani_stanje_trenutnega_uporabnika(stanje)
        bottle.redirect(url_kategorije(id_kategorije))


@bottle.post("/opravi/<id_kategorije:int>/<id_opravila:int>/")
def opravi(id_kategorije, id_opravila):
    stanje = stanje_trenutnega_uporabnika()
    kategorija = stanje.kategorije[id_kategorije]
    opravilo = kategorija.opravila[id_opravila]
    opravilo.opravi()
    shrani_stanje_trenutnega_uporabnika(stanje)
    bottle.redirect(url_kategorije(id_kategorije))

@bottle.post("/dodaj-opravilo/<id_kategorije:int>/")
def dodaj_opravilo(id_kategorije):
    stanje = stanje_trenutnega_uporabnika()
    kategorija = stanje.kategorije[id_kategorije]
    opis = bottle.request.forms.getunicode("opis")
    if bottle.request.forms["rok"]:
        rok = date.fromisoformat(bottle.request.forms["rok"])
    else:
        rok = None
    opravilo = Opravilo(opis, rok)
    kategorija.dodaj_opravilo(opravilo)
    shrani_stanje_trenutnega_uporabnika(stanje)
    bottle.redirect(url_kategorije(id_kategorije))


@bottle.error(404)
def error_404(error):
    return "Ta stran ne obstaja!"


bottle.run(debug=True, reloader=True)
