# Nizi

V programih seveda ne delamo le s števili, temveč tudi z drugimi podatki, na primer besedili. V ta namen Python podpira nize, ki so strnjena zaporedja znakov.

```python
'Pozdravljen, svet!'    "niz"    '123'
```

## Osnovne operacije na nizih

Nize običajno pišemo v enojnih narekovajih, na primer `'to je primer niza'`. Nize lahko stikamo z operacijo `+` in množimo s celimi števili:

```python
>>> 'zala' + 'gasper'
'zalagasper'
>>> 'tro' + 4 * 'lo'
'trololololo'
`
```

Dolžino niza dobimo s funkcijo `len`:

```
>>> len('lokomotiva')
10
```

Nize lahko med seboj tudi primerjamo. Pri tem Python nize ureja leksikografsko, torej tako, kot bi bili urejeni v leksikonu ali kazalu: najprej primerja prvi črki, če sta ti dve enaki, pogleda drugi dve, in tako naprej. Pri tem velike črke pridejo na vrsto pred malimi, na šumnike pa se brez posebnih knjižnic Python ne spozna.

> > > 'beseda' == 'konj' False 'abak' <= 'abeceda' True ```

Na nizih imamo na voljo tudi predikat `in`, s katerim ugotovimo, ali se nek niz pojavlja kot podniz v drugem nizu. Na voljo je tudi `not in`, s katerim bolj berljivo zapišemo ravno nasprotno stvar:

``` `
>>> 'gram' in 'Uvod v programiranje' True
>>> 'liter' in
'Uvod v programiranje' False
>>> not ('liter' in 'Uvod v
programiranje') True
>>> 'liter' not in 'Uvod v programiranje'
True
```

Nize lahko pišemo tudi z dvojnimi narekovaji, ki jih ponavadi uporabimo takrat, kadar v nizu želimo uporabiti enojni narekovaj: `"Tole je kr'neki!"`. V tem primeru niza ne moremo pisati med enojnimi narekovaji, saj bi Python po narekovaju za `kr` mislil, da je konec niza.

Včasih želimo uporabiti obe vrsti narekovajev. V tem primeru si pomagamo z _ubežnimi znaki_. To so znaki, ki jih na običajni način ne moremo zapisati, zato uporabimo poseben zapis, ki se začne z znakom `\`. Tedaj lahko pišemo `'"Tole je kr'neki," je rekla.'` ali pa `""Tole je kr'neki," je rekla."`. Ubežne znake brez težav lahko pišemo tudi tedaj, kadar ni treba `'"Grem v rudnik," je rekla.'`. Z ubežnimi znaki lahko zapišemo tudi znak za novo vrstico `\n`, za tabulator `\t` in seveda tudi za poševnico `\\`, saj je ne moremo pisati le kot `\`, ker bi Python to razumel kot začetek ubežnega znaka.

Nize lahko pišemo tudi med tri enojne (`'''`) ali tri dvojne (`"""`) narekovaje. V tem primeru za en sam narekovaj ne potrebujemo ubežnega znaka. Take nize lahko pišemo tudi čez več vrstic.

```
>>> 'Tole je kr'neki!'
                   ^
SyntaxError: invalid syntax
```

```
>>> "Tole je kr'neki!"
"Tole je kr'neki!"
>>> '"Grem v rudnik," je rekla.'
'"Grem v rudnik," je rekla.'
>>> '''"Tole je kr'neki," je rekla.'''
'"Tole je kr\'neki," je rekla.'
>>> 'niz' == "niz"
True
>>> 'niz' + "niz" + '''niz''' + """niz"""
'nizniznizniz'
```

Funkcija, ki vrne ustrezen pozdrav

```python
>>> pozdrav('Matija')
'Dober dan, gospod profesor.'
>>> pozdrav('Anja')
'Pozdravljena, gospa asistentka.'
>>> pozdrav('Filip')
'Pozdravljeni, gospod asistent.'
>>> pozdrav('Francelj')
'Živjo, Francelj!'
```

## Indeksi in rezine

Do posameznega znaka v nizu pridemo z _indeksi_. Z izrazom `niz[i]` dostopamo do `i`-tega znaka v danem nizu:

```
>>> 'rekurzija'[3]
'u'
>>> 'rekurzija'[0]
'r'
>>> 'rekurzija'[-1]
'a'
```

Indeksi se začnejo šteti z 0\. Če uporabimo negativna števila, lahko štejemo tudi od zadaj, vendar tam začnemo šteti z -1 (saj je -0 = 0).

```
0   1   2   3   4   5   6   7   8
 R   E   K   U   R   Z   I   J   A
-9  -8  -7  -6  -5  -4  -3  -2  -1
```

Na podoben način lahko dostopamo tudi do podnizov. Če napišemo `niz[i:j]` bomo dobili niz, ki mu pravimo _rezina_ in sega od vključno `i`-tega do vključno `j - 1`-tega znaka. Če kakšno od meja izpustimo, bomo vzeli vse znake od začetka oziroma do konca.

```
>>> 'rekurzija'[2]
'k'
>>> 'rekurzija'[6]
'i'
>>> 'rekurzija'[2:6]
'kurz'
>>> 'rekurzija'[:6]
'rekurz'
>>> 'rekurzija'[2:]
'kurzija'
```

Število samoglasnikov

```
>>> stevilo_samoglasnikov('UVP je zakon!!!')
4
>>> stevilo_samoglasnikov('čmrlj')
0
>>> stevilo_samoglasnikov('otorinolaringolog')
8
```

Najdaljši podniz, ki je palindrom

```
>>> max_podpalindrom('otorinolaringolog')
'ooriroo'
>>> max_podpalindrom('ventrilokvist')
'tilit'
>>> max_podpalindrom('neradodaren')
'neradodaren'
```

Pišemo lahko tudi `niz[i:j:k]`, s čimer vzamemo le vsak `k`-ti znak:

```
>>> 'rekurzija'[1:8]
'ekurzij'
>>> 'rekurzija'[1:8:1]
'ekurzij'
>>> 'rekurzija'[1:8:2]
'euzj'
>>> 'rekurzija'[1:8:3]    
'erj'
>>> 'rekurzija'[::-1]
'ajizruker'
```

## Vgrajene metode

Na nizih obstaja kup **vgrajenih metod**

```python
>>> '&'.join(['a', 'b', 'c'])
'a&b&c'
>>> 'lokomotiva'.replace('o', 'u')
'lukumutiva'
>>> '  x  y  z  '.strip()
'x  y  z'
>>> 'lokomotiva'.upper()
'LOKOMOTIVA'
>>> 'to je stavek'.split()
['to', 'je', 'stavek']
```

```
>>> yoda('Jaz sem Yoda!')
'Yoda jaz sem!'
>>> yoda('Kdo si ti?')
'Ti kdo si?'
```

.center[![](slike/yoda.jpg)]

S `count` **preštejemo** elemente

```python
>>> [1, 5, 3, 5, 1, 4, 5].count(5)
3
>>> (1, 5, 3, 5, 1, 4, 5).count(5)
3
>>> 'lokomotiva'.count('o')
3
```

- `s.count(t)`

  : Vrne število pojavitev podniza `t` v nizu `s`. Klic

  ```
  `s.count(t, i)` deluje podobno, le da začne šteti šele pri
  indeksu `i`, klic `s.count(t, i, j)` pa konča šteti pri indeksu
  `j`.
  ```

Z `index` **poiščemo mesto** danega elementa

```python
>>> [1, 5, 3, 5, 1, 4, 5].index(5)
1
>>> (1, 5, 3, 5, 1, 4, 5).index(5)
1
>>> 'lokomotiva'.index('o')
1
```

```
>>> [1, 5, 3, 5, 1, 4, 5].index(5, 2)  
3
>>> (1, 5, 3, 5, 1, 4, 5).index(5, 2)  
3
>>> 'lokomotiva'.index('o', 2)
3
```

```
`s.find(t)`

:   Vrne najmanjši indeks v nizu `s`, kjer se niz `t` pojavi kot
    podniz. Podobno kot prej klic `s.find(t, i)` začne iskati pri
    indeksu `i`, klic `s.find(t, i, j)` pa konča pri indeksu `j`. Če
    niza ni, metoda vrne `-1`. Metoda `s.index` se obnaša enako kot
    `s.find`, le da v primeru, ko podniza ne najde, sproži napako.
```

- `s.join(sez)`

  : Z ločilom `s` skupaj stakne vse nize iz seznama `sez`.

- `s.replace(t1, t2)`

  : Vrne kopijo niza `s`, v katerem smo vse pojavitve podniza `t1`

  ```
  zamenjali s podnizi `t2`. Klic `s.replace(t1, t2, n)` pa zamenja
  le prvih `n` pojavitev.
  ```

- `s.strip()`

  : Vrne kopijo niza `s`, v katerem smo odstranili vse bele znake

  ```
  (presledki, tabulatorji, nove vrste) z začetka in konca. Klic
  `s.strip(t)` z začetka in konca odstrani vse znake iz niza `t`.
  ```

- `s.lower()` / `s.upper()` / `s.title()` / `s.capitalize()` / `s.swapcase()`

  : Vrne kopijo niza `s`, kjer: vse črke zamenjamo z malimi / vse

  ```
  črke zamenjamo z velikimi / vsem besedam damo veliko začetnico /
  na začetku niza damo veliko začetnico / male črke zamenjamo z
  velikimi in obratno.
  ```

- `s.split()`

  : Vrne seznam besed v nizu `s` (ločene glede na bele znake). Klic

  ```
  `s.split(t)` loči glede na podniz `t`. Klic `s.split(t, n)` vrne
  niz razbit na prvih `n` ločilih.
  ```

- `s.isdigit()` / `s.isalpha()` / `s.islower()` / `s.isupper()` / `s.isalnum()` / `s.isspace()`

  : Vrne `True`, če je niz `s` neprazen in so vsi znaki: števke /

  ```
  črke / male črke / velike črke / črke ali številke / beli znaki.
  ```

## Vse v Pythonu je objekt, `__add__`

## Branje in pisanje s konzole

Funkcija `print` **izpiše** dani niz

```
>>> print('Pozdravljen, svet!')
*Pozdravljen, svet!
>>> print('"Grem v rudnik", je rekla.')
*"Grem v rudnik", je rekla.
>>> print("Tole je kr'neki!")   
*Tole je kr'neki!
>>> print('Tole je kr\'neki!')   
*Tole je kr'neki!
>>> print('en\ndva\ntri')
*en
*dva
*tri
```

`print` poleg nizov izpisuje tudi druge vrednosti

```
>>> print(1 + 1)
*2
>>> print(3 + 4 < 5)
*False
```

Izpišemo lahko tudi več vrednosti

```
>>> print('a', 123, None)
*a 123 None
```

Funkcija `print` ne vrne **ničesar**

```
>>> 1 + 1
2
>>> print(1 + 1)
*2
>>> 1 + (1 + 1)
3
>>> 1 + print(1 + 1)
*2
TypeError: unsupported operand type(s)
  for *: 'int' and 'NoneType'
```

Kaj izpiše ukaz `print(print(42))`

Kaj vrne ukaz `print(print(42))`

`print`, `input`

## Pretvorbe med tipi

`str`, `int`, `bool`, v pogojnih stavkih

## Ubežni znaki

## `f`-nizi

Z metodo `format` v nizu **zapolnimo luknje**

```python
>>> '{0} ima {1}'.format('mama', 'stol')
'mama ima stol'
>>> niz = '{0} vzklika: "{1}, {1}, {1}!"'
>>> niz.format('Mama', 'joj')
'Mama vzklika: "joj, joj, joj!"'
>>> niz.format('Tone', 'FMF')
'Tone vzklika: "FMF, FMF, FMF!"'
```

Argumente lahko tudi **oblikujemo**

```python
>>> a, b = 22, 7
>>> '{0}/{1} = {2:.5}'.format(a, b, a / b)
'pi = 3.1429'
>>> 'popust znaša {0:.2%}'.format(1 / 3)
'popust znaša 33.33%'
>>> '{0:*^30}'.format('NASLOV')
'************NASLOV************'
```

Od Pythona 3.6 naprej uporabljamo **`f`-nize**

```python
>>> a, b = 22, 7
>>> f'{a}/{b} = {a / b:.5}'
'22/7 = 3.1429'
>>> f'popust znaša {1 / 3:.2%}'
'popust znaša 33.33%'
>>> f'{"NASLOV":*^30}'
'************NASLOV************'
```
