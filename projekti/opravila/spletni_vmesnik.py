import bottle
from datetime import date
from model import Model, Opravilo, Spisek

IME_DATOTEKE = "stanje.json"
try:
    moj_model = Model.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    moj_model = Model()


@bottle.get("/")
def osnovna_stran():
    return bottle.template(
        "osnovna_stran.html",
        neopravljena=moj_model.stevilo_zamujenih(),
        opravila=moj_model.aktualni_spisek.opravila if moj_model.aktualni_spisek else [],
        spiski=moj_model.spiski,
        aktualni_spisek=moj_model.aktualni_spisek
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
    moj_model.dodaj_opravilo(opravilo)
    moj_model.shrani_v_datoteko(IME_DATOTEKE)
    bottle.redirect("/")

@bottle.get("/dodaj-spisek/")
def dodaj_spisek_get():
    return bottle.template("dodaj_spisek.html", napake={}, polja={})

@bottle.post("/dodaj-spisek/")
def dodaj_spisek_post():
    ime = bottle.request.forms.getunicode("ime")
    polja = {"ime": ime}
    napake = moj_model.preveri_podatke_novega_spiska(ime)
    if napake:
        return bottle.template("dodaj_spisek.html", napake=napake, polja=polja)
    else:
        spisek = Spisek(ime)
        moj_model.dodaj_spisek(spisek)
        moj_model.shrani_v_datoteko(IME_DATOTEKE)
        bottle.redirect("/")


@bottle.post("/zamenjaj-opravljeno/")
def zamenjaj_opravljeno():
    indeks = bottle.request.forms.getunicode("indeks")
    opravilo = moj_model.aktualni_spisek.opravila[int(indeks)]
    opravilo.zamenjaj_opravljeno()
    moj_model.shrani_v_datoteko(IME_DATOTEKE)
    bottle.redirect("/")


@bottle.post("/zamenjaj-aktualni-spisek/")
def zamenjaj_aktualni_spisek():
    print(dict(bottle.request.forms))
    indeks = bottle.request.forms.getunicode("indeks")
    spisek = moj_model.spiski[int(indeks)]
    moj_model.aktualni_spisek = spisek
    moj_model.shrani_v_datoteko(IME_DATOTEKE)
    bottle.redirect("/")


@bottle.error(404)
def error_404(error):
    return "Ta stran ne obstaja!"


bottle.run(reloader=True, debug=True)
