## Statične in razredne metode

## `property`

## Dedovanje

## Zgoščevalne tabele

- defaultdict

```{code-cell}

```

aa## Posebne metode

## Statične in razredne metode

## Dedovanje

# Razredi

objekte združujemo v razredih

# objekt ~ podatki + metode

## Objekti v istem razredu imajo različne podatke (atribute) ter enake metode

## Definicije lastnih razredov

Definicija razreda sestoji iz definicij **metod**

````python
```{code-cell}
````

# Izjeme & iterabilni objekti

## Sprožanje in lovljenje izjem

## Iteratorji

**Iteratorji** so objekti z metodo `__next__`

```
class IteratorCezNiz:
    def __init__(self, niz):
        self.niz = niz
        self.indeks = 0

    def __next__(self):
        if self.indeks < len(self.niz):
            self.indeks += 1
            return self.niz[self.indeks - 1]
        else:
            raise StopIteration
```

```
class Ponavljalec:
    def __init__(self, x, n):
        self.x = x
        self.n = n

    def __next__(self):
        if self.n > 0:
            self.n -= 1
            return self.x
        else:
            raise StopIteration
```

**Naslednjo vrednost** iteratorja dobimo prek funkcije `next`

```
>>> i = IteratorCezNiz('abc')
>>> next(i)
'a'
>>> next(i)
'b'
>>> next(i)
'c'
>>> next(i)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

Z iteratorji lahko predstavimo **neskončne sezname**

```
class IteratorFibonaccijevih:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        prejsnji_a = self.a
        prejsnji_b = self.b
        self.a = prejsnji_b
        self.b = prejsnji_a + prejsnji_b
        return prejsnji_a
```

## Iterabilni objekti

**Iterabilni objekti** (_iterable_) so objekti z metodo `__iter__`, ki vrne iterator

```
class Pes:
    ...
    def __iter__(self):
        x = self.glas + '!'
        n = self.veselje
        return Ponavljalec(x, n)
    ...
```

Funkcija `iter` vrne **iterator** objekta

```
>>> fido = Pes(glas='vuf')
>>> fido.razveseli()
>>> it = iter(fido)
>>> next(it)
'vuf!'
>>> next(it)
'vuf!'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

**Iterabilne** objekte lahko damo v **zanko** `for`

```
>>> fido = Pes(glas='vuf')
>>> fido.razveseli()
>>> for x in fido: print(x)
... 
vuf!
vuf!
```

Kako deluje `for x in obj: ...`?

1. pokliči `iter(obj)`, da dobiš iterator `itr`
2. pokliči `next(itr)`, da dobiš naslednjo vrednost
3. vrednost shrani v spremenljivko `x`
4. izvedi ukaze `...`
5. ponavljaj korake od 2 do 4, dokler korak 2 ne sproži izjeme `StopIteration`
6. ko dobiš izjemo, končaj

## Generatorji

**Generatorji** so iteratorji, definirani **podobno kot funkcije**

```
def en_dva_tri():
    yield 1
    yield 5 - 3
    yield 2 + 1
```

```
>>> for x in en_dva_tri(): print(x)
1
2
3
```

`en_dva_tri` je funkcija, ki ob **vsakem klicu** vrne **nov generator**.

Z generatorji lahko predstavimo **neskončne sezname**

```
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for x in fibonacci():
    print(x, end=', ')
```

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
144, 233, 377, 610, 987, 1597, 2584, 4181,
6765, 10946, 17711, 28657, 46368, 75025,
121393, 196418, 317811, 514229, 832040 ...
```

Z `yield from` predajamo vrednosti **drugega generatorja**

```
def odstevaj():
    for i in range(10, 0, -1):
        yield i
    yield 'Bum!'
```

```
def odstevaj():
    yield from range(10, 0, -1)
    yield 'Bum!'
```

Razponi s seznami in generatorji Generator deliteljev

Obstajajo tudi **izpeljani generatorji**

```
def generiraj_generator():
    for x in ...:
        if pogoj:
            yield f(x)
generator = generiraj_generator()
```

```
generator = (f(x) for x in ... if pogoj)
```

## Razstavljanje iterabilnih objektov

Kljub temu, da lahko do elementov nabora dostopamo z indeksi, je pogosto uporabno, da jih razstavimo. To storimo s hkratnim prireditvenim stavkom, v katerem na levi strani naštejemo več spremenljivk, na desni pa podamo nabor, ki ga želimo razstaviti:

> > > datum = (30, 'marec', 2016) dan, mesec, leto = datum dan 30 mesec 'marec' ```

V resnici gre pri hkratnih prireditvenih stavkih za sestavljanje in razstavljanje naborov. Pri razstavljanju je treba paziti, da je število spremenljivk na levi enako dolžini nabora na desni, saj v nasprotnem primeru pride do napake.

```
>>> a, b, c = 1, 'dva', 3
>>> (a + c) * b
'dvadvadvadva'
```

```
>>> nabor = (1, 'dva', 3)
>>> a, b, c = nabor
>>> (a + c) * b
'dvadvadvadva'
```

Na podoben način kot nabore lahko razstavljamo tudi sezname: Razstavimo lahko **vsak iterabilni** objekt

```
>>> a, b, c = [1, 2, 3]
>>> a + b + c
6
>>> x, y, z = 'ABC'
>>> 3 * z + 2 * y + x
'CCCBBA'
```

Toda seznami običajno nimajo definirane dolžine, zato lahko pri njihovem razstavljanju uporabimo tudi poseben vzorec, ki v spremenljivko shrani vse preostale elemente:

```
>>> x, y, *z = [1, 2, 3, 4, 5]
>>> x
1
>>> y
2
>>> z
[3, 4, 5]
```

Vzorec za preostale elemente se lahko pojavi tudi kje drugje kot na koncu:

```
>>> prva, *ostale = 'nek niz'
>>> prva
'n'
>>> ostale
['e', 'k', ' ', 'n', 'i', 'z']
```

Vzorec `*` se lahko pojavi tudi **na sredini**

```
>>> x, *y, z = [1, 2, 3, 4, 5]
>>> x
1
>>> y
[2, 3, 4]
>>> z
5
```

Vseeno pa vzorec za preostale elemente lahko uporabimo največ enkrat:

```
>>> *prva_polovica,*druga_polovica = [1, 2, 3, 4] Traceback (most
recent call last): ... SyntaxError: two starred expressions in
assignment
```

Na podoben način lahko razstavljamo tudi nabore, nize in ostale strukture, po katerih se lahko sprehajamo z zanko `for`, vendar bo v spremenljivki vedno shranjen seznam preostalih elementov:

## Funkcije s poljubno mnogo argumenti

Vzorec `*` se lahko pojavi tudi **v funkcijah**, kjer preostale argumente shrani v **nabor**

Vzorec za preostale elemente lahko uporabimo tudi v definicijah funkcij:

```
def vrni_zadnji_argument(*args):

:   return args[-1]
```

```
>>> vrni_zadnji_argument(10, 20, 30) 30
>>>
vrni_zadnji_argument(1) 1
```

```
def f(x, *args):
    return x * args
```

```
>>> f(2, 4, 6, 8)
(4, 6, 8, 4, 6, 8)
>>> f(5)
()
```

Tak vzorec na primer uporablja funkcija `max` (in njej podobne). Ta funkcija namreč deluje tako, da v primeru, ko dobi en argument, vrne njegov največji element, ko pa dobi več argumentov, pa vrne največjega:

```
>>> max([3, 5], [4, 1]) [4, 1]
>>> max([3, 5, 4, 1]) 5
>>> max(3, 5, 4, 1) 5
```

S pomočjo vzorca za preostale argumente bi tako funkcijo napisali tako, da bi najprej preverili, koliko argumentov smo dobili, nato pa ustrezno poiskali maksimum:

```
def maksimum(*argumenti):

:   ''' Ob več argumentih vrne največjega. Ob enem argumentu vrne
    njegov največji element. ''' if len(argumenti) == 0: # Če nismo
    dobili nobenega argumenta, return None # vrnemo None. if
    len(argumenti) == 1: # Če smo dobili en argument, kandidati =
    argumenti[0] # iščemo maksimum med njegovimi elementi. else: #
    Če smo dobili več argumentov, kandidati = argumenti # iščemo
    maksimum med njimi.

    # Uporabimo znan postopek za iskanje največjega elementa. najvecji
    = None for kandidat in kandidati: if najvecji is None or najvecji <
    kandidat: najvecji = kandidat return najvecji
```

```
>>> maksimum([3, 5], [4, 1]) [4, 1]
>>> maksimum([3, 5, 4,
1]) 5
>>> maksimum(3, 5, 4, 1) 5
```

V funkcijah vzorec `**` preostale imenovane argumente shrani v **slovar**

```
def f(x=2, **kwargs):
    for k, v in kwargs.items():
        print(k, x * '>>', v)
```

```
>>> f(x=4, y=3, z=4)
y
>>>>>>>> 3
z
>>>>>>>> 4
>>> f(y=3, z=4)
y
>>>> 3
z
>>>> 4
```

Vzorca `*` in `**` lahko uporabimo pri **klicih**

```
def f(x, y):
    return x + y
```

```
>>> f(1, 2)
3
>>> seznam = [1, 2]
>>> f(*seznam)
3
```

```
>>> '{a} --- {b}'.format(a=10, b=20)
'10 --- 20'
>>> slovar = {'a': 10, 'b': 20}
>>> '{a} --- {b}'.format(**slovar)
'10 --- 20'
```
