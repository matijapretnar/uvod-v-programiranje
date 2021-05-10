import bottle
from datetime import date
from model import Stanje, Opravilo, Spisek

IME_DATOTEKE = "stanje.json"
try:
    stanje = Stanje.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    stanje = Stanje()


@bottle.get("/")
def osnovna_stran():
    return bottle.template(
        "osnovna_stran.html",
        neopravljena=stanje.stevilo_zamujenih(),
        opravila=stanje.aktualni_spisek.opravila if stanje.aktualni_spisek else [],
        spiski=stanje.spiski,
        aktualni_spisek=stanje.aktualni_spisek
    )


@bottle.post("/dodaj/")
def dodaj_opravilo():
    ime = bottle.request.forms.getunicode("ime")
    opis = bottle.request.forms.getunicode("opis")
    if bottle.request.forms['datum']:
        datum = date.fromisoformat(bottle.request.forms['datum'])
    else:
        datum = None
    opravilo = Opravilo(ime, opis, datum)
    stanje.dodaj_opravilo(opravilo)
    stanje.shrani_v_datoteko(IME_DATOTEKE)
    bottle.redirect("/")

@bottle.get("/dodaj-spisek/")
def dodaj_spisek_get():
    return bottle.template("dodaj_spisek.html", napake={}, polja={})

@bottle.post("/dodaj-spisek/")
def dodaj_spisek_post():
    ime = bottle.request.forms.getunicode("ime")
    polja = {"ime": ime}
    napake = stanje.preveri_podatke_novega_spiska(ime)
    if napake:
        return bottle.template("dodaj_spisek.html", napake=napake, polja=polja)
    else:
        spisek = Spisek(ime)
        stanje.dodaj_spisek(spisek)
        stanje.shrani_v_datoteko(IME_DATOTEKE)
        bottle.redirect("/")


@bottle.post("/zamenjaj-opravljeno/")
def zamenjaj_opravljeno():
    indeks = bottle.request.forms.getunicode("indeks")
    opravilo = stanje.aktualni_spisek.opravila[int(indeks)]
    opravilo.zamenjaj_opravljeno()
    stanje.shrani_v_datoteko(IME_DATOTEKE)
    bottle.redirect("/")


@bottle.post("/zamenjaj-aktualni-spisek/")
def zamenjaj_aktualni_spisek():
    print(dict(bottle.request.forms))
    indeks = bottle.request.forms.getunicode("indeks")
    spisek = stanje.spiski[int(indeks)]
    stanje.aktualni_spisek = spisek
    stanje.shrani_v_datoteko(IME_DATOTEKE)
    bottle.redirect("/")


@bottle.error(404)
def error_404(error):
    return "Ta stran ne obstaja!"


bottle.run(reloader=True, debug=True)
