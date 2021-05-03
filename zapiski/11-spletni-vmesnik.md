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

# Spletni vmesnik

Uporabniku si običajno želimo ponuditi bolj prijazen vmesnik od tekstovnega. Včasih se je v ta namen uporabljalo posebne knjižnice za grafični vmesnik, na primer TkInter, ki je podprt tudi v Pythonovi standardni knjižnici. Vedno bolj pogosta alternativa grafičnemu vmesniku pa je spletni vmesnik, v katerem z uporabnikom komuniciramo prek HTML obrazcev. Prednost spletnega vmesnika je v enostavnem pisanju, pa tudi v tem, da je podprt na vseh napravah. Najprej si bomo pogledali, kako napišemo vmesnik za enega samega uporabnika, nato pa ga bomo razširili v storitev, s katero lahko dela več uporabnikov hkrati.

## Knjižnica `bottle`

Pri pisanju si bomo pomagali s knjižnico `bottle`, ki jo je enostavno uporabljati in enostavno namestiti, saj je sestavljena le iz ene datoteke `bottle.py`, ki jo lahko vključimo v svoj projekt. Program bo ob zagonu na našem računalniku pognal majhen spletni strežnik (običajno na naslovu `http://127.0.0.1:8080`), ki se bo odzival na uporabnikove zahteve v spletnem brskalniku. Spletni vmesnik v `bottle`-u gradimo prek funkcij, ki so povezane s spletnimi naslovi, ter vračajo HTML odziv. Na primer, enostaven strežnik, ki ob obisku vrhnje strani `/` vračal statičen odziv, bi napisali in pognali kot:

```python
import bottle

@bottle.get('/')
def osnovni_zaslon():
    return 'Opravila: program za vzbujanje slabe vesti'

bottle.run()
```

Z vrstico `@bottle.get('/')` knjižnici `bottle` sporočimo, naj vsaka zahteva strani `/` pokliče funkcijo `osnovni_zaslon`. Ta funkcija vrne niz, ki ga knjižnica `bottle` posreduje uporabnikovemu brskalniku v izris. Takih definicij funkcij je lahko več, na koncu pa sledi vrstica `bottle.run()`, ki požene strežnik.

Pri zagonu imamo več možnosti. Možnost `debug` omogoča izpisovanje napak (v javni verziji to ponavadi izklopimo, da zlobni hekerji ne bi imeli vpogleda v ozadje našega programa), možnost `reloader` pa ob vsaki spremembi kode ponovno požene strežnik. Med razvojem imamo običajno vklopljeni obe možnosti, zato strežnik ponavadi poženemo kot:

```python
bottle.run(debug=True, reloader=True)
```

## Predloge

Funkcije običajno vračajo HTML, na primer

```python
@bottle.get('/')
def osnovni_zaslon():
    return '''
        <h1>Opravila</h1>
        <h2>program za vzbujanje slabe vesti</h2>'
    '''
```

Ker bo HTML postal dolg in ker ga nočemo mešati s Pythonom, ga bomo shranili v ločeno datoteko, na primer `osnovni_zaslon.tpl`:

```html
<h1>Opravila</h1>
<h2>program za vzbujanje slabe vesti</h2>
```

ter klicali

```python
@bottle.get('/')
def osnovni_zaslon():
    return bottle.template('osnovni_zaslon.tpl')
```

Kot nakazujeta končnica `.tpl` in ime funkcije `bottle.template`, ne gre le za statičen HTML, temveč za predloge, ki jih lahko dopolnimo s svojimi podatki. Na primer, v predlogo lahko podamo število zamujenih opravil:

```python
@bottle.get('/')
def osnovni_zaslon():
    return bottle.template(
      'osnovni_zaslon.tpl',
      zamujena=model.stevilo_zamujenih()
    )
```

ki jih prikažemo kot:

```html
<h1>Opravila</h1>
<h2>program za vzbujanje slabe vesti</h2>
<p>
  Trenutno imate {{zamujena}} zamujenih opravil.
</p>
```

V predlogah lahko za `%` pišemo poljubno Python kodo, na primer:

```html
<h1>Opravila</h1>
<h2>program za vzbujanje slabe vesti</h2>
<p>
  % if zamujena > 0:
  Trenutno imate {{zamujena}} zamujenih opravil.
  % else:
  Čestitamo, vse ste opravili pravočasno.
  % end
</p>
```

Sicer ni nujno, je pa lepo, da zamiki v predlogah sledijo gnezdenju HTML značk.Zaradi tega presledki v Python kodi niso pomembni, morate pa zato vsak zamik končati z `% end`.

Če želimo, lahko v predlogah uporabljamo tudi zanke, na primer, da prikažemo seznam vseh aktualnih opravil:

```python
@bottle.get('/')
def osnovni_zaslon():
    return bottle.template(
      'osnovni_zaslon.tpl',
      zamujena=model.stevilo_zamujenih(),
      opravila=model.aktualni_spisek.opravila,
    )
```

```html
<h1>Opravila</h1>
<h2>program za vzbujanje slabe vesti</h2>

<p>
  % if zamujena > 0:
  Trenutno imate {{zamujena}} zamujenih opravil.
  % else:
  Čestitamo, vse ste opravili pravočasno.
  % end
</p>
<ul>
  % for opravilo in opravila:
  <li>{{opravilo.ime}}</li>
  % end
</ul>
```

Vsaka prava HTML stran mora imeti glavo in telo, torej vsaj:

```html
<html>
  <head>
    <title>...</title>
  </head>
  <body>
    ...
  </body>
</html>
```

idealno pa še kaj več, na primer CSS datoteke za oblikovanje in podobno. Da ne bomo vsega tega pisali za vsako predlogo, bomo raje napisali eno skupno predlogo `osnova.tpl`:

```html
<html>
  <head>
    <title>Opravila</title>
  </head>
  <body>
    {{!base}}
    <footer>© 2021, Matija Pretnar</footer>
  </body>
</html>
```

ter na vsaki strani na vrhu napisali `% rebase('osnova.tpl')`, kar bo preostanek predloge vstavilo v del, označen z `{{!base}}`.

## Dinamične spletne strani

Spletne strani so lahko tudi odvisne od naslova. Na primer, če želimo prikazati določen spisek, lahko v datoteko `prikazi_spisek.tpl` napišemo

```html
% rebase('osnova.tpl')
<h1>{{spisek.ime}}</h1>
<ul>
  % for opravilo in opravila:
  <li>{{opravilo.ime}}</li>
  % end
</ul>
```

ter to povežemo s stranmi `/spisek/0/`, `/spisek/1/` in podobno kot:

```python
@bottle.get('/spisek/<indeks>/')
def prikazi_spisek(indeks):
    spisek = model.spiski[int(indeks)]
    return bottle.template('prikazi_spisek.tpl', spisek=spisek)
```

Deli naslovov označeni z `<ime_spremenljivke>` se bodo povezali z istoimenskimi argumenti funkcije. Če ne označimo posebej, bodo ti deli predstavljeni z nizi, zato smo zgoraj morali uporabiti funkcijo `int`. Če želimo, lahko dele naslovov omejimo na cela števila z:

```python
@bottle.get('/spisek/<indeks:int>/')
def prikazi_spisek(indeks):
    spisek = model.spiski[indeks]
    return bottle.template('prikazi_spisek.tpl', spisek=spisek)
```

V tem primeru pretvorba z `int` ni potrebna, hkrati pa bo `bottle` naslove kot na primer `/spisek/abc/` obravnaval kot neobstoječe ter to sporočil uporabniku. Prejšnja različica bi namreč v spremenljivko `indeks` shranila niz `'abc'`, ker bi ob pretvorbi `int(indeks)` sprožilo izjemo.

Včasih bomo poleg generiranih HTML strani želeli ponuditi tudi statične datoteke, na primer slike, CSS stile in podobno. To lahko storimo s še eno dinamično stranjo, ki glede na spremenljivi del naslova poišče datoteko ter jo posreduje nazaj:

```python
@bottle.get('/static/<ime_dat:path>')
def server_static(ime_dat):
  pot = 'staticne_datoteke'
  return bottle.static_file(ime_dat, root=pot)
```

Tako bi zahteva na spletni naslov `/static/ozadje.png` v imeniku na računalniku poiskala ter posredovala datoteko `staticne_datoteke/ozadje.png`.

## Obrazci

Poleg naslovov pa podatke lahko vnašamo tudi v obrazce. Na primer, če želimo iskati po opravilih, si lahko na osnovno stran dodamo obrazec:

```html
<form action="/isci/">
  iskalni niz: <input type="text" name="iskalni_niz">
  <input type="submit" value="Išči!">
</form>
```

Vsak obrazec ima atribut `action`, ki sporoča, na katero naj ob oddaji pošlje vnešene podatke (če manjka, ob oddaji naredi novo poizvedbo na trenutno stran), ter več polj, vsako z atributom `name`. Tako bi za iskanje morali napisati funkcijo, vezano na naslov `/isci/`, ki bi do podatkov dostopala prek slovarja `bottle.request.query`:

```python
@bottle.get('/isci/')
def sestej():
    iskalni_niz = bottle.request.query['iskalni_niz']
    return bottle.template(
        'rezultati_iskanja.tpl',
        rezultati=model.isci(iskalni_niz)
    )
```

Če gre za nize, je bolje uporabiti posebno metodo `getunicode`, ki ustrezno poskrbi za znake kot so šumniki in podobno:

```python
@bottle.get('/isci/')
def sestej():
    iskalni_niz = bottle.request.getunicode('iskalni_niz')
    return bottle.template(
        'rezultati_iskanja.tpl',
        rezultati=model.isci(iskalni_niz)
    )
```

## Metoda POST in preusmeritve

Sodobni brskalniki si pri poizvedbah dopuščajo kar nekaj svobode. Na primer, zahtevo za začetno stran spletne učilnice lahko pošljejo že ko napišemo `uciln...`, saj vedo, da gre za stran, ki jo pogosto obiskujemo, in jo želijo ponuditi čimprej. To je že dobro, nočemo pa, da bi na primer samodejno poslali zahtevo za spletni nakup. V ta namen obstajajo poizvedbe _POST_, ki so namenjene spreminjanju stanja. Poizvedbam, ki smo jih uporabljali do zdaj, pa pravimo poizvedbe _GET_. Poizvedbe POST v obrazcih označimo z atributom `method="POST"`, na primer:

```html
<form action="/dodaj_opravilo/" method="POST">
  ime: <input type="text" name="ime">
  opis: <input type="text" name="opis">
  <input type="submit" value="Dodaj!">
</form>
```

Podatke, poslane prek poizvedb POST obdelamo podobno kot prej, le da jih namesto iz `request.query` preberemo iz `request.forms`:

```python
@bottle.post('/dodaj_opravilo/')
def dodaj_opravilo():
    ime = bottle.request.forms['ime']
    opis = bottle.request.forms['opis']
    if ime:
        opravilo = model.Opravilo(ime, opis)
        model.dodaj_opravilo(opravilo)
        bottle.redirect('/')
    else:
        return 'Ime mora biti neprazno'
```

Opazimo lahko, da na koncu poizvedbe nismo vrnili strani z odzivom, temveč smo uporabnika preusmerili nazaj na začetno stran. Recimo, da bi uporabniku prikazali stran, nato pa bi ta v brskalniku pritisnil gumb za osvežitev (iz navade, ker se kakšna slika ni naložila, ...). V tem primeru bi brskalnik zopet poslal isto poizvedbo, ki bi dodala še eno opravilo. Sodobni brskalniki pred ponovnim pošiljanjem takih poizvedb opozorijo (da ne bi dvakrat kupili letalskih vozovnic), še bolje pa je, da uporabnika preusmerimo na novo stran, ki jo dobi s poizvedbo GET in osvežuje po mili volji. Če je prišlo do napake v vnosu, pa uporabniku lahko vrnemo stran (običajno z do sedaj izpolnjenimi podatki), saj spremembe nismo naredili.
