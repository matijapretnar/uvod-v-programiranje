# Spletni vmesnik

## Knjižnica `bottle`

Spletni vmesnik v `bottle`-u gradimo **prek funkcij**

```
import bottle

@bottle.get('/')
def pozdravi():
    return 'Živjo!'

bottle.run()
```

Možnost `debug` omogoča **izpisovanje napak**

```
bottle.run(debug=True)
```

Možnost `reloader` **samodejno požene** strežnik ob spremembi kode

```
bottle.run(reloader=True)
```

Med razvojem imamo običajno vklopljeni **obe možnosti**

```
bottle.run(debug=True, reloader=True)
```

## Dinamične spletne strani

Funkcije lahko sprejmejo tudi **argumente**

```
@bottle.get('/<ime>/')
def pozdravi(ime):
    return 'Živjo, {}!'.format(ime)
```

V spletne naslove lahko dajemo tudi **filtre**

```
@bottle.get('/kvadriraj/<n>')
def kvadriraj(n):
    n = int(n)
    return '{}^2 = {}'.format(n, n ** 2)
```

```
@bottle.get('/kvadriraj/<n:int>')
def kvadriraj(n):
    return '{}^2 = {}'.format(n, n ** 2)
```

## Predloge

Funkcije običajno vračajo **HTML**

```
@bottle.get('/<ime>/')
def pozdravi(ime):
    return 'Živjo, <b>{}</b>!'.format(ime)
```

Besedilo **iz predloge** ustvarimo s `template`

```
@bottle.get('/<ime>/')
def pozdravi(ime):
  return bottle.template('zivjo.tpl', ime=ime)
```

`views/zivjo.tpl`

```
<html>
  <head>
    <title>Pozdravna stran za {{ime}}</title>
  </head>
  <body>
    Živjo, <b>{{ime}}</b>!
  </body>
</html>
```

Za `%` pišemo poljubno **Python kodo**

```
vrstica besedila
% a = 7 * 6
odgovor je {{a}}
```

--------------------------------------------------------------------------------

```
vrstica besedila
odgovor je 42
```

Presledki **niso pomembni**, vendar moramo zamike končati s `% end`

```
%        if 3 < 7:
%   a = 42
% else:
%        a = 100
% end
odgovor je {{a}}
```

--------------------------------------------------------------------------------

```
odgovor je 42
```

Vse vrstice brez `%` gradijo **izpis**

```
<ul>
% for i in range(5):
    <li>{{i ** 2}}</li>
% end
</ul>
```

--------------------------------------------------------------------------------

```
<ul>
   <li>0</li>
   <li>1</li>
   <li>4</li>
   <li>9</li>
   <li>16</li>
</ul>
```

Za **skupne dele predlog** uporabimo `rebase`

```
<html>
  <body>
     To je moja prva stran.
     <footer>© 2019, Ime Priimek</footer>
  </body>
</html>
```

```
<html>
  <body>
     To je moja druga stran.
     <footer>© 2019, Ime Priimek</footer>
  </body>
</html>
```

Za **skupne dele predlog** uporabimo `rebase`

```
<html>
  <body>
     {{!base}}
     <footer>© 2019, Ime Priimek</footer>
  </body>
</html>
```

```
% rebase('osnova.tpl')
To je moja prva stran.
```

```
% rebase('osnova.tpl')
To je moja druga stran.
```

S funkcijo `static_file` lahko ponujamo tudi **statične datoteke** (slike, CSS stili, ...)

```
@bottle.get('/static/<ime_dat:path>')
def server_static(ime_dat):
  pot = '/pot/do/mape/z/datotekami'
  return bottle.static_file(ime_dat, root=pot)
```

### Spletna ogrodja

## Obrazci

Podatke vnašamo prek **obrazcev**

```
<form action="/sestej/">
  a: <input type="text" name="a">
  b: <input type="text" name="b">
  <input type="submit" value="a + b">
</form>
```

Podatke preberemo iz `request.query`

```
@bottle.get('/sestej/')
def sestej():
    a = bottle.request.query['a']
    b = bottle.request.query['b']
    return '{} + {} = {}'.format(a, b, a + b)
```

Vsi podatki so prenešeni **kot nizi**

```
@bottle.get('/sestej/')
def sestej():
    a = int(bottle.request.query['a'])
    b = int(bottle.request.query['b'])
    return '{} + {} = {}'.format(a, b, a + b)
```

**Unicode** moramo zahtevati eksplicitno

```
@bottle.get('/pozdravi/')
def pozdravi():
  ime = bottle.request.query['ime']
  return 'Živjo, {}!'.format(ime)
```

```
@bottle.get('/pozdravi/')
def pozdravi():
  ime = bottle.request.query.getunicode('ime')
  return 'Živjo, {}!'.format(ime)
```

## Metoda `POST` in preusmeritve

Obrazce, ki **spreminjajo** stanje, pošiljamo z metodo **POST**

```
<form action="/sestej/" method="POST">
  <input type="radio" name="glas" value="da">
    Da
  <input type="radio" name="glas" value="ne">
    Ne
  <input type="submit" value="glasuj">
</form>
```

Podatke, poslane prek POST poizvedb, preberemo iz `request.forms`

```
@bottle.post('/glasuj/')
def glasuj():
    glas = bottle.request.forms['glas']
    model.zabelezi_glas(glas)
    return 'Glas je bil uspešno zabeležen!'
```

Po uspešno izvedeni POST poizvedbi naredimo **preusmeritev**

```
@bottle.post('/glasuj/')
def glasuj():
    glas = bottle.request.forms['glas']
    model.zabelezi_glas(glas)
    return 'Glas je bil uspešno zabeležen!'
```

Če preusmeritve ne naredimo, lahko osveževanje vodi do **večkratnih sprememb**.

Po uspešno izvedeni POST poizvedbi naredimo **preusmeritev**

```
@bottle.post('/glasuj/')
def glasuj():
    glas = bottle.request.forms['glas']
    model.zabelezi_glas(glas)
    bottle.redirect('/glasuj/')

@bottle.get('/glasuj/')
def glasuj_rezultat():
    return 'Glas je bil uspešno zabeležen!'
```
