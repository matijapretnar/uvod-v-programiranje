from datetime import date
import bottle
import model

proracun = model.Proracun.iz_datoteke("stanje.json")


def poisci_kuverto(proracun, ime_polja):
    id_kuverte = bottle.request.forms.get(ime_polja)
    return proracun.kuverte[int(id_kuverte)] if id_kuverte else None


def poisci_racun(proracun, ime_polja):
    id_racuna = bottle.request.forms[ime_polja]
    return proracun.racuni[int(id_racuna)]


@bottle.get("/")
def zacetna_stran():
    bottle.redirect("/proracun/")


@bottle.get("/proracun/")
def nacrtovanje_proracuna():
    return bottle.template("proracun.html", proracun=proracun)


@bottle.get("/analiza/")
def analiza():
    return bottle.template("analiza.html", eno_besedilo="<strong>tra la la</strong> & hop sa sa")


@bottle.get("/pomoc/")
def pomoc():
    return bottle.template("pomoc.html")


@bottle.post("/dodaj-transakcijo/")
def dodaj_transakcijo():
    opis = bottle.request.forms.getunicode("opis")
    znesek = int(bottle.request.forms["znesek"])
    datum = date.fromisoformat(bottle.request.forms["datum"])
    racun = poisci_racun(proracun, "racun")
    kuverta = poisci_kuverto(proracun, "kuverta")
    proracun.dodaj_transakcijo(opis, znesek, datum, racun, kuverta)
    proracun.v_datoteko("stanje.json")
    bottle.redirect("/")


@bottle.post("/premakni-denar/")
def premakni_denar():
    kuverta1 = poisci_kuverto(proracun, "kuverta1")
    kuverta2 = poisci_kuverto(proracun, "kuverta2")
    znesek = int(bottle.request.forms["znesek"])
    model.Kuverta.premakni_denar(kuverta1, kuverta2, znesek)
    proracun.v_datoteko("stanje.json")
    bottle.redirect("/")


@bottle.post("/dodaj-racun/")
def dodaj_racun():
    ime = bottle.request.forms.getunicode("ime")
    proracun.dodaj_racun(ime)
    proracun.v_datoteko("stanje.json")
    bottle.redirect("/")


@bottle.post("/dodaj-kuverto/")
def dodaj_kuverto():
    ime = bottle.request.forms.getunicode("ime")
    proracun.dodaj_kuverto(ime)
    proracun.v_datoteko("stanje.json")
    bottle.redirect("/")

@bottle.get("/static/<ime_datoteke:path>")
def static(ime_datoteke):
    return bottle.static_file(ime_datoteke, "static")


bottle.run(reloader=True, debug=True)
