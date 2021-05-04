import bottle
from datetime import date
from model import Model, Opravilo

IME_DATOTEKE = "stanje.json"
try:
    moj_model = Model.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    moj_model = Model()


@bottle.get("/")
def osnovna_stran():
    return bottle.template(
        "osnovna_stran.tpl",
        neopravljena=moj_model.stevilo_zamujenih(),
        opravila=moj_model.aktualni_spisek.opravila,
    )


@bottle.post("/dodaj/")
def dodaj_opravilo():
    ime = bottle.request.forms.getunicode("ime")
    opis = bottle.request.forms.getunicode("opis")
    datum = date.today()
    opravilo = Opravilo(ime, opis, datum)
    moj_model.dodaj_opravilo(opravilo)
    moj_model.shrani_v_datoteko(IME_DATOTEKE)
    bottle.redirect("/uspesno-dodajanje/")


@bottle.get("/uspesno-dodajanje/")
def uspesno_dodajanje():
    return "Uspešno si dodXXXal"


@bottle.post("/opravi/")
def opravi_opravilo():
    indeks = bottle.request.forms.getunicode("indeks")
    opravilo = moj_model.aktualni_spisek.opravila[int(indeks)]
    opravilo.opravi()
    moj_model.shrani_v_datoteko(IME_DATOTEKE)
    bottle.redirect("/")


@bottle.error(404)
def error_404(error):
    return "Ta stran ne obstaja!"


bottle.run(reloader=True, debug=True)
