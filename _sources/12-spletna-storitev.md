---
jupytext:
  cell_metadata_filter: '-all'
  formats: 'md:myst'
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.1
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Spletna storitev

Spletni vmesnik iz prejšnjega poglavja vedno deluje z enim samim stanjem, ki ga prikaže vsakemu uporabniku, ki do njega dostopa s spletnim brskalnikom. Dokler spletni strežnik teče samo na lokalnem računalniku, to še ni tako slabo, če pa bi do strežnika imelo dostop več ljudi, je pa to tako neuporabno kot nevarno. Tako bomo spletni vmesnik popravili v pravo spletno storitev, ki bo skrbela za ustrezno sledenje uporabnikov.

## Piškotki

Spletni protokoli so pisani tako, da morajo biti v vsaki poizvedbi vsi podatki, ki jih strežnik potrebuje za odziv. Recimo, da na spletu iščemo za "Evklidov algoritem" in kliknemo povezavo za naslednjo stran rezultatov. V tem primeru naš brskalnik na strežnik ne pošlje poizvedbe "vrni naslednjo stran" temveč na primer "vrni drugo stran rezultatov iskanja za Evklidov algoritem". Če bi si namreč strežnik moral zapomniti vse prejšnje poizvedbe, bi mu hitro zmanjkalo prostora.

Na podoben način moramo poskrbeti tudi za podatke o prijavljenem uporabniku. Ena možnost je, da bi uporabniško ime in geslo prek obrazcev posredovali v vsaki poizvedbi, vendar bi to izjemno hitro postalo nerodno. Namesto tega bomo uporabili _piškotke_. Ti so majhni kosi podatkov, ki jih strežnik v odzivu pošlje uporabniku, uporabnik pa jih nato samodejno priloži vsaki nadaljnji poizvedbi. Ko se bo uporabnik prijavil z uporabniškim imenom in geslom, si bo strežnik izmislil posebno šifro ter jo vrnil uporabniku. Ko bo uporabnik vsaki svoji nadaljnji poizvedbi priložil to šifro, bo strežnik vedel, za koga gre.

Prijavo naredimo preko obrazca, ki pošlje poizvedbo POST, ki jo lahko obdelamo kot:

```python
@bottle.post('/prijava/')
def prijava():
  uporabnisko_ime = bottle.request.forms['uporabnisko_ime']
  geslo = bottle.request.forms['geslo']
  if model.preveri_uporabnika(uporabnisko_ime, geslo):
      bottle.response.set_cookie('uporabnisko_ime', uporabnisko_ime, path='/')
      bottle.redirect('/')
  else:
    return 'Napačni podatki za prijavo'
```

Ko preverimo pravilnost uporabniškega imena in gesla (kako to natančno storimo, bomo pogledali kasneje), uporabniku v odzivu nastavimo piškotek ter ga preusmerimo na osnovno stran. To storimo prek funkcije `bottle.response.set_cookie`, ki ji posredujemo tri argumente: ime piškotka (nastavimo lahko več piškotkov), vrednost ter pot, na kateri velja (piškotki lahko veljajo samo na določenih podstraneh).

V spletnem vmesniku smo stanje prebrali iz fiksne datoteke:

```python
IME_DATOTEKE = 'stanje.json'
stanje = Stanje.preberi_iz_datoteke(IME_DATOTEKE)
```

Sedaj pa bo vsak uporabnik imel svoje stanje. V ta namen si napišemo pomožno funkcijo, ki stanje prijavljenega uporabnika prebere iz datoteke, neprijavljenega uporabnika pa preusmeri na stran za prijavo:

```python
def stanje_trenutnega_uporabnika():
    uporabnisko_ime = bottle.response.get_cookie('uporabnisko_ime')
    if uporabnisko_ime:
        return Stanje.preberi_iz_datoteke(f"{uporabnisko_ime}.json")
    else:
        bottle.redirect('/prijava/')
```

Sedaj moramo še vsako spletno stran popraviti, da ne uporablja fiksnega stanja, temveč uporabnikovo. Na primer, namesto

```python
@bottle.post('/dodaj_opravilo/')
def dodaj_opravilo():
    ime = bottle.request.forms['ime']
    opis = bottle.request.forms['opis']
    if ime:
        opravilo = stanje.Opravilo(ime, opis)
        stanje.dodaj_opravilo(opravilo)
        bottle.redirect('/')
    else:
        return 'Ime mora biti neprazno'
```

moramo pisati

```python
@bottle.post('/dodaj_opravilo/')
def dodaj_opravilo():
    stanje = stanje_trenutnega_uporabnika()
    ime = bottle.request.forms['ime']
    opis = bottle.request.forms['opis']
    if ime:
        opravilo = stanje.Opravilo(ime, opis)
        stanje.dodaj_opravilo(opravilo)
        bottle.redirect('/')
    else:
        return 'Ime mora biti neprazno'
```

Za odjavo uporabnika moramo le pobrisati piškotek:

```python
@bottle.post('/odjava/')
def odjava():
    bottle.response.delete_cookie('uporabnisko_ime', uporabnisko_ime, path='/')
    bottle.redirect('/')
```

Ker piškotke na strežnik pošilja uporabnik, moramo biti previdni, da ne bi tega kdo izkoristil za nepooblaščeni dostop do strežnika. V kodi, kot jo imamo zgoraj, bi namreč uporabnik lahko svoj piškotek `uporabnisko_ime` popravil na neko drugo vrednost (na primer `admin`) ter s tem dobil dostop do drugega računa. To enostavno rešimo tako, da strežnik piškotek nastavi na vrednost, ki jo lahko prebere le on sam. V knjižnici Bottle to storimo tako, da funkcijam za delo s piškotki podamo še dodaten argument `secret`, v katerem podamo niz, ki je dostopen le strežniku. S pomočjo te vrednosti bo strežnik vrednost piškotka zašifriral, preden jo bo poslal uporabniku, ter odšifriral, ko jo bo dobil nazaj. Tako bi lahko na primer na vrhu strežnikove kode nastavili

```python
SIFRA = 'to šifro pozna le strežnik'
```

nato pa pisali

```python
    bottle.response.set_cookie('uporabnisko_ime', uporabnisko_ime, path='/', secret=SIFRA)
```

ali

```python
    bottle.response.get_cookie('uporabnisko_ime', , secret=SIFRA)
```

Tako uporabnik v piškotku `uporabnisko_ime` ne vidi svojega uporabniškega imena, temveč nekaj podobnega

```
"!lc+Jr/Oo32xFThrc1feEJfrPyJBiWO9SU0IVgU1QLGI=?gAWVHwAAAAAAAABdlCiMD3Vwb3JhYm5pc2tvX2ltZZSMBWFkbWlulGUu"
```

Paziti moramo, da šifre ne ponesreči kje ne objavimo, saj bi z njeno pomočjo lahko nekdo ustvaril ustrezen zašifriran piškotek. Ena možnost je, da jo preberemo iz datoteke:

```python
with open('sifra.txt') as d:
    SIFRA = d.read()
```

ime datoteke `sifra.txt` pa dodamo v `.gitignore`, da je ne bi po nesreči dodali v javni Git repozitorij.
