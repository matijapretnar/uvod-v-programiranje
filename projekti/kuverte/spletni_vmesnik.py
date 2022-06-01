from datetime import date
import bottle
import model

with open("skrivnost.txt") as f:
    SKRIVNOST = f.read()
vse_skupaj = model.VseSkupaj.iz_datoteke("stanje.json")


def poisci_kuverto(proracun, ime_polja):
    id_kuverte = bottle.request.forms.get(ime_polja)
    return proracun.kuverte[int(id_kuverte)] if id_kuverte else None


def poisci_racun(proracun, ime_polja):
    id_racuna = bottle.request.forms[ime_polja]
    return proracun.racuni[int(id_racuna)]


def proracun_trenutnega_uporabnika():
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime", secret=SKRIVNOST)
    if uporabnisko_ime is None:
        bottle.redirect("/prijava/")
    else:
        return vse_skupaj.poisci_uporabnika(uporabnisko_ime).proracun

def shrani_vse_skupaj():
    vse_skupaj.v_datoteko("stanje.json")



@bottle.get("/prijava/")
def prijava_get():
    return bottle.template("prijava.html", napaka=None)

@bottle.post("/prijava/")
def prijava_post():
    uporabnisko_ime = bottle.request.forms.getunicode("uporabnisko_ime")
    geslo_v_cistopisu = bottle.request.forms.getunicode("geslo")
    uporabnik = vse_skupaj.poisci_uporabnika(uporabnisko_ime, geslo_v_cistopisu)
    if uporabnik:
        bottle.response.set_cookie("uporabnisko_ime", uporabnisko_ime, path="/", secret=SKRIVNOST)
        bottle.redirect("/")
    else:
        return bottle.template("prijava.html", napaka="Napačno geslo")

@bottle.post("/odjava/")
def odjava_post():
    bottle.response.delete_cookie("uporabnisko_ime")
    bottle.redirect("/")

@bottle.get("/")
def zacetna_stran():
    bottle.redirect("/proracun/")


@bottle.get("/proracun/")
def nacrtovanje_proracuna():
    proracun = proracun_trenutnega_uporabnika()
    obiskal_pomoc = bottle.request.get_cookie("obiskal-pomoc", secret=SKRIVNOST) == "da"
    return bottle.template("proracun.html", proracun=proracun, obiskal_pomoc=obiskal_pomoc)


@bottle.get("/analiza/")
def analiza():
    return bottle.template("analiza.html", eno_besedilo="<strong>tra la la</strong> & hop sa sa")


@bottle.get("/pomoc/")
def pomoc():
    bottle.response.set_cookie("obiskal-pomoc", "da", path="/", secret=SKRIVNOST)
    return bottle.template("pomoc.html")


@bottle.post("/dodaj-transakcijo/")
def dodaj_transakcijo():
    proracun = proracun_trenutnega_uporabnika()
    opis = bottle.request.forms.getunicode("opis")
    znesek = int(bottle.request.forms["znesek"])
    datum = date.fromisoformat(bottle.request.forms["datum"])
    racun = poisci_racun(proracun, "racun")
    kuverta = poisci_kuverto(proracun, "kuverta")
    proracun.dodaj_transakcijo(opis, znesek, datum, racun, kuverta)
    shrani_vse_skupaj()
    bottle.redirect("/")


@bottle.post("/premakni-denar/")
def premakni_denar():
    proracun = proracun_trenutnega_uporabnika()
    kuverta1 = poisci_kuverto(proracun, "kuverta1")
    kuverta2 = poisci_kuverto(proracun, "kuverta2")
    znesek = int(bottle.request.forms["znesek"])
    model.Kuverta.premakni_denar(kuverta1, kuverta2, znesek)
    shrani_vse_skupaj()
    bottle.redirect("/")


@bottle.post("/dodaj-racun/")
def dodaj_racun():
    proracun = proracun_trenutnega_uporabnika()
    ime = bottle.request.forms.getunicode("ime")
    proracun.dodaj_racun(ime)
    shrani_vse_skupaj()
    bottle.redirect("/")


@bottle.post("/dodaj-kuverto/")
def dodaj_kuverto():
    proracun = proracun_trenutnega_uporabnika()
    ime = bottle.request.forms.getunicode("ime")
    proracun.dodaj_kuverto(ime)
    shrani_vse_skupaj()
    bottle.redirect("/")

@bottle.get("/static/<ime_datoteke:path>")
def static(ime_datoteke):
    return bottle.static_file(ime_datoteke, "static")


bottle.run(reloader=True, debug=True)
