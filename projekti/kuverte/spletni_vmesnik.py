from datetime import date
import bottle
import model

proracun = model.Proracun.iz_datoteke("stanje.json")

@bottle.get("/")
def zacetna_stran():
    return bottle.template(
        "zacetna_stran.html",
        proracun=proracun,
    )

@bottle.get("/racun/<id_racuna:int>/")
def racun(id_racuna):
    return bottle.template(
        "racun.html",
        racun=proracun.racuni[id_racuna],
    )

@bottle.post("/nalozi/<id_racuna:int>/")
def nalozi(id_racuna):
    racun = proracun.racuni[id_racuna]
    opis = bottle.request.forms["opis"]
    znesek = float(bottle.request.forms["znesek"])
    transakcija = model.Transakcija(opis, znesek, date.today())
    racun.dodaj_transakcijo(transakcija)
    bottle.redirect("/")


bottle.run(reloader=True, debug=True)
