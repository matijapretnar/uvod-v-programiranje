---
class: 'center, middle'
---

class: center, middle

# vsaka vrednost v Pythonu ima tip

# tip ~ množica vrednosti

class: center, middle

## Cela števila

### `int`

```python
3   -10   0   444   123456789   -9999999
```

--------------------------------------------------------------------------------

class: center, middle

## Števila s plavajočo vejico

### `float`

```python
3.14  -10.0  0.0  1.2345e20  -1.281e-16
```

--------------------------------------------------------------------------------

class: center, middle

## Logični (Booleovi) vrednosti

### `bool`

```python
True     False
```

--------------------------------------------------------------------------------

class: center, middle

## Kompleksna števila

### `complex`

```python
2 + 3j    4 - 2j    2.1 - 1.6j
```

--------------------------------------------------------------------------------

### Osnovne operacije na kompleksnih številih

```python
>>> (2 + 3j) * (4 - 2j)
(14+8j)
>>> 2.718281828459 ** 3.141592653590j
(-1-1.53976491138057e-13j)
>>> 1j
1j
>>> j
NameError: name 'j' is not defined
```

--------------------------------------------------------------------------------

class: center, middle

## Ničelna vrednost

### `NoneType`

```python
None
```

--------------------------------------------------------------------------------

### Z `None` predstavimo manjkajoče vrednosti

```python
>>> None
```

```python
def f(x):
    x + 2
```

```python
>>> f(5)
>>> 2 * f(5)
TypeError: unsupported operand type(s)
  for *: 'int' and 'NoneType'
```

--------------------------------------------------------------------------------

class: center, middle

## Nizi

### `str`

--------------------------------------------------------------------------------

### Med tipi lahko tudi **pretvarjamo**

```
>>> int(3.14)
3
>>> float(3)
3.0
>>> str(True)
'True'
>>> bool(4)
True
>>> bool('False')
True
```

--------------------------------------------------------------------------------

class: center, middle

## Funkcije

### `function` / `builtin_function_or_method`

```python
round    math.sin

f  # če imamo prej def f(x): return x + 2

lambda x: x + 2
```

--------------------------------------------------------------------------------

class: center, middle

## Tipi

### `type`

```python
int   float   str   list   type
```

V **nize** pretvarjamo s funkcijo `str`

```python
>>> str(True)
'True'
>>> str(10)
'10'
>>> str([1, 2, 3])
'[1, 2, 3]'
>>> str(['a', 'b', 'c'])
"['a', 'b', 'c']"
>>> str('abc')
'abc'
```

V **Booleove vrednosti** pretvarjamo z `bool`

```python
>>> bool(1)
True
>>> bool('niz')
True
>>> bool('')
False
>>> bool(0)
False
>>> bool([])
False
>>> bool('False')
True
>>> bool([0, 0, 0])
True
```

Pogojni stavek **samodejno pretvori** z `bool`

```python
if n != 0:
    ...
```

```python
if niz != '':
    ...
```

```python
if sez != []:
    ...
```

Pogojni stavek **samodejno pretvori** z `bool`

```python
if n:
    ...
```

```python
if niz:
    ...
```

```python
if sez:
    ...
```

V cela števila pretvarjamo s funkcijo `int`

```python
>>> int('123')
123
>>> int(5.213)
5
>>> int('osem')
...
ValueError: invalid literal
  for int() with base 10: 'osem'
>>> int('5.213')
...
ValueError: invalid literal
  for int() with base 10: '5.213'
```

V sezname pretvarjamo s funkcijo `list`

```python
>>> list('abc')
['a', 'b', 'c']
>>> list()
[]
>>> list((1, 2, 3))
[1, 2, 3]
>>> list({'a', 'b', 'c'})
['b', 'a', 'c']
```

V nabore pretvarjamo s funkcijo `tuple`

```python
>>> tuple('abc')
('a', 'b', 'c')
>>> tuple()
()
>>> tuple([1])
(1,)
>>> tuple({1, 2, 3})
(1, 2, 3)
```

V množice pretvarjamo s funkcijo `set`

```python
>>> set('abc')
{'b', 'c', 'a'}
>>> set('abcabcabc')
{'b', 'c', 'a'}
>>> set()
set()
>>> set([1])
{1}
>>> set({1: 'a', 2: 'b'})
{1, 2}
```

V slovarje pretvarjamo s funkcijo `dict`

```python
>>> dict([(1, 2), (3, 4)])
{1: 2, 3: 4}
>>> dict()
{}
```

# Osnovni vgrajeni tipi

Vsaka vrednost v Pythonu ima svoj _tip_ oziroma _razred_ (ti dve besedi sta včasih v Pythonu imeli različna pomena, zdaj pa pomenita isto reč), ki opisuje njene osnovne lastnosti.

## Tipi števil `int` in `float`

Videli smo že, da zna Python računati tako s celimi števil kot s števili s plavajočo vejico. Prva pripadajo tipu `int` (_integer_), druga pa tipu `float` (_floating point number_). Razlika med njimi je vidna že na pogled, saj se druga prikazujejo z decimalno piko. Število, v katerem uporabimo decimalno piko, je tipa `float` tudi takrat, ko so vse decimalke enake nič. Če računamo s celimi števili, vedno uporabljamo vrednosti tipa `int`, saj pri tipu `float` prihaja do zaokrožitvenih napak:

```
>>> 7.0 ** 360 / 7.0 ** 342 1628413597910448.8
>>> 7 ** 18
1628413597910449
```

Pri zgornjem primeru smo res uporabili zelo velika števila, da smo dobili majhno napako, vendar je to zaradi tega, da smo imeli enostaven primer. Običajni izračuni so daljši, zato se tudi napake začnejo hitreje nabirati.

## Tip kompleksnih števil `complex`

Python pozna tudi kompleksna števila tipa `complex`, ki jih pišemo tako, da za vrednostjo imaginarnega dela napišemo črko `j` (črko `i` v programiranju raje uporabljamo za indekse). Običajno tudi `+` med realnim in imaginarnim delom pišemo brez presledka:

```
>>> 2 + 3j (2+3j)
>>> (1 + 1j) * (1 - 1j) (2+0j)
>>> (-1 + 0j)
** 0.5 (6.123233995736766e-17+1j)
>>> import math
>>> math.e
** (math.pi * 1j) + 1 1.2246467991473532e-16j
```

V zadnjih dveh primerih vidimo, da tudi pri kompleksnih številih prihaja do zaokrožitvenih napak (prva vrednost bi morala biti `1j`, druga pa `0+0j`), saj Python kompleksna števila predstavi s parom števil s plavajočo vejico. Tako kot pri tipu `float` tudi pri kompleksnih številih Python vse ostale vrednosti v računu, v katerem se pojavi kakšno kompleksno število, pretvori v tip `complex`. Tako kot deljenje `/`, ki dve celi števili pretvori v `float`, tudi potenciranje na negativno število samodejno ustvari kompleksna števila:

```
>>> (-1) ** 0.5 (6.123233995736766e-17+1j)
```

Kompleksna števila lahko ustvarimo tudi s funkcijo `complex`, ki ji lahko podamo tudi dva argumenta, da povemo obe komponenti:

```
>>> complex(3) (3+0j)
>>> complex(3, 4) (3+4j)
```

## Tip logičnih vrednosti `bool`

Logični vrednosti `True` in `False`, ki sta tipa `bool` (_boolean_ oz. Booleovi števili) že poznamo.

## Tip ničelne vrednosti `NoneType`

Tudi vrednost `None`, ki smo jo srečali takrat, kadar smo v funkciji pozabili napisati `return`, ima svoj tip, ki mu rečemo `NoneType`. Zdaj lahko tudi razumemo napako, ki smo jo dobili, ko smo `None` želeli uporabiti v računu:

```
def f(x):

:   x + 1
```

```
>>> 3 * f(2) Traceback (most recent call last): ... TypeError:
unsupported operand type(s) for *: 'int' and 'NoneType'
```

Napaka `TypeError` nam pravi, da smo nekje zamešali tipe. V tem primeru smo z operacijo `*` poskušali pomnožiti `int` in `NoneType`, torej neko celo število in vrednost `None` (saj je to edina vrednost tipa `NoneType`). Rezultat klica `f(2)` je torej `None`, zato smo verjetno pozabili na `return`.

## Pretvorbe med tipi

V zgornjih računih vidimo, da Python števila avtomatično pretvori na skupni imenovalec. Na primer, če število tipa `int` pomnožimo s številom tipa `float`, bo končni rezultat vedno `float`:

```
>>> 2 * 3.0 6.0
```

Pretvorbo lahko opravimo tudi sami s pomočjo funkcij `int` in `float`:

```
>>> float(2) 2.0
>>> int(3.1415) 3
```

Funkcijo `int` bomo pogosto uporabili za to, da danemu število s plavajočo vejico odbijemo decimalke in ga s tem pretvorimo v celo število. Pozor, ta funkcija niti ne zaokroži na najbližje celo število, niti ne zaokroži:

```
>>> int(3.999) 3
>>> int(-3.1) -3
>>> int(-3.9999) -3

Pretvorbe v logične vrednosti so malo bolj
```

posebne: vsa neničelna števila in vsi neprazni nizi se pretvorijo v `True`, ničla in prazen niz pa v `False`.

>

> > > bool(4) True bool(0) False bool(0.00000001) True bool('False') True bool('') False

Tudi v drugo smer so pretvorbe malo posebne: `True` se pretvori v število 1 ali pa niz `'True'`, `False` pa v število 0 oziroma niz `'False'`.

>

> > > int(True) 1 float(False) 0.0 str(False) 'False' bool(str(False)) True

Pretvorbe v logične vrednosti se v pogojnih stavkih izvajajo avtomatično. Evklidov algoritem bi lahko zato, če bi želeli, pisali tudi kot:

```
def gcd(m, n):

:   

    if n:

    :   return gcd(n, m % n)

    else:

    :   return m
```

## Tip nizov `str`

Nizi v Pythonu so tipa `str` (_string_). Druge vrednosti lahko pretvorimo v nize s pomočjo funkcije `str`:

```
>>> str(1234) '1234'
>>> str(1 / 3) '0.3333333333333333'
>>> str(2 < 3) 'True'
```

Pretvorbe lahko naredimo tudi v drugo smer, če le napišemo ustrezen niz:

```
>>> int('123') 123
>>> float('3.14') 3.14
>>> int('12 +
34') Traceback (most recent call last): ... ValueError: invalid
literal for int() with base 10: '12 + 34'
```

Zadnja napaka pravi, da niz `12 + 34` ni veljaven zapis celega števila v desetiškem sistemu.

## Tip tipov `type`

Če želimo, lahko tip ugotovimo tudi s funkcijo `type`:

```
>>> type(3) <class 'int'>
>>> type(3.14) <class 'float'>
>>> type(3.0) <class 'float'>
>>> type(10 // 2) <class
'int'>
>>> type(10 / 2) <class 'float'>
>>> type('abc')
<class 'str'>
>>> type(None) <class 'NoneType'>
```

Ta funkcija vrača vrednosti, ki predstavljajo tipe. Do teh vrednosti lahko dostopamo tudi direktno prek vgrajenih konstant `int`, `str`, ...

```
>>> type(3) == int True
>>> type(3.0) == bool False
```

Te vgrajene konstante so posebne, saj se hkrati obnašajo kot tipi in kot funkcije, ki pretvarjajo v dane tipe:

```
>>> type(int('123')) == int True
>>> type(str(3.14)) == float
False
```

Kot smo povedali na začetku, imajo vse vrednosti v Pythonu svoj tip. Tako ga imajo tudi vrednosti, ki predstavljajo tipe, in sicer tip `type`. Vrednost `type`, ki predstavlja ta tip tipov, pa ima spet tip `type`, s čimer se zgodba zaključi.

```
>>> type(3) <class 'int'>
>>> type(type(3)) <class 'type'>
>>> type(int) <class 'type'>
>>> type(type) <class 'type'>
```
