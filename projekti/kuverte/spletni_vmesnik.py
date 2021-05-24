from datetime import date
import bottle
from model import Uporabnik

PISKOTEK_UPORABNISKO_IME = "uporabnisko_ime"
SKRIVNOST = "to je ena skrivnost"


def poisci_racun(proracun, ime_polja):
    ime_racuna = bottle.request.forms.getunicode(ime_polja)
    return proracun.poisci_racun(ime_racuna)


def poisci_kuverto(proracun, ime_polja):
    ime_kuverte = bottle.request.forms.getunicode(ime_polja)
    return proracun.poisci_kuverto(ime_kuverte or None)


def shrani_stanje(uporabnik):
    uporabnik.v_datoteko()


def trenutni_uporabnik():
    uporabnisko_ime = bottle.request.get_cookie(
        PISKOTEK_UPORABNISKO_IME, secret=SKRIVNOST
    )
    if uporabnisko_ime:
        return podatki_uporabnika(uporabnisko_ime)
    else:
        bottle.redirect("/prijava/")


def podatki_uporabnika(uporabnisko_ime):
    return Uporabnik.iz_datoteke(uporabnisko_ime)


@bottle.get("/")
def zacetna_stran():
    bottle.redirect("/proracun/")


@bottle.get("/registracija/")
def registracija_get():
    return bottle.template("registracija.html", napaka=None)


@bottle.post("/registracija/")
def registracija_post():
    uporabnisko_ime = bottle.request.forms.getunicode("uporabnisko_ime")
    geslo_v_cistopisu = bottle.request.forms.getunicode("geslo")
    if not uporabnisko_ime:
        return bottle.template("registracija.html", napaka="Vnesi uporabniško ime!")
    try:
        Uporabnik.registracija(uporabnisko_ime, geslo_v_cistopisu)
        bottle.response.set_cookie(
            PISKOTEK_UPORABNISKO_IME, uporabnisko_ime, path="/", secret=SKRIVNOST
        )
        bottle.redirect("/")
    except ValueError as e:
        return bottle.template(
            "registracija.html", napaka=e.args[0]
        )


@bottle.get("/prijava/")
def prijava_get():
    return bottle.template("prijava.html", napaka=None)


@bottle.post("/prijava/")
def prijava_post():
    uporabnisko_ime = bottle.request.forms.getunicode("uporabnisko_ime")
    geslo_v_cistopisu = bottle.request.forms.getunicode("geslo")
    if not uporabnisko_ime:
        return bottle.template("registracija.html", napaka="Vnesi uporabniško ime!")
    try:
        Uporabnik.prijava(uporabnisko_ime, geslo_v_cistopisu)
        bottle.response.set_cookie(
            PISKOTEK_UPORABNISKO_IME, uporabnisko_ime, path="/", secret=SKRIVNOST
        )
        bottle.redirect("/")
    except ValueError as e:
        return bottle.template(
            "prijava.html", napaka=e.args[0]
        )

@bottle.post("/odjava/")
def odjava():
    bottle.response.delete_cookie(PISKOTEK_UPORABNISKO_IME, path="/")
    bottle.redirect("/")


@bottle.get("/proracun/")
def nacrtovanje_proracuna():
    uporabnik = trenutni_uporabnik()
    return bottle.template(
        "proracun.html", proracun=uporabnik.proracun, uporabnik=uporabnik
    )


@bottle.get("/analiza/")
def analiza():
    trenutni_uporabnik()
    return bottle.template("analiza.html")


@bottle.get("/pomoc/")
def pomoc():
    return bottle.template("pomoc.html")


@bottle.post("/dodaj-preliv/")
def dodaj_preliv():
    uporabnik = trenutni_uporabnik()
    znesek = int(bottle.request.forms["znesek"])
    datum = date.today().strftime("%Y-%m-%d")
    opis = bottle.request.forms.getunicode("opis")
    racun = poisci_racun(uporabnik.proracun, "racun")
    kuverta = poisci_kuverto(uporabnik.proracun, "kuverta")
    uporabnik.proracun.nov_preliv(znesek, datum, opis, racun, kuverta)
    shrani_stanje(uporabnik)
    bottle.redirect("/")


@bottle.post("/premakni-denar/")
def premakni_denar():
    uporabnik = trenutni_uporabnik()
    kuverta1 = poisci_kuverto(uporabnik.proracun, "kuverta1")
    kuverta2 = poisci_kuverto(uporabnik.proracun, "kuverta2")
    znesek = int(bottle.request.forms["znesek"])
    uporabnik.proracun.premakni_denar(kuverta1, kuverta2, znesek)
    shrani_stanje(uporabnik)
    bottle.redirect("/")


@bottle.post("/dodaj-racun/")
def dodaj_racun():
    uporabnik = trenutni_uporabnik()
    uporabnik.proracun.nov_racun(bottle.request.forms.getunicode("ime"))
    shrani_stanje(uporabnik)
    bottle.redirect("/")


@bottle.post("/dodaj-kuverto/")
def dodaj_kuverto():
    uporabnik = trenutni_uporabnik()
    uporabnik.proracun.nova_kuverta(bottle.request.forms.getunicode("ime"))
    shrani_stanje(uporabnik)
    bottle.redirect("/")


@bottle.post("/odstrani-kuverto/")
def odstrani_kuverto():
    uporabnik = trenutni_uporabnik()
    kuverta = poisci_kuverto(uporabnik.proracun, "kuverta")
    uporabnik.proracun.odstrani_kuverto(kuverta)
    shrani_stanje(uporabnik)
    bottle.redirect("/")


bottle.run(debug=True, reloader=True)