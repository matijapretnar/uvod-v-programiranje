# Slovarji & množice

```python
{'a': 1, 'b': 5, 'c': 10}    {}

{1: 'a', 5: 'b', 10: 'c'}
```

```python
nujne_telefonske_stevilke = {
  'center za obveščanje': 112,
  'policija': 113,
  'informacije': 1188,
  'točen čas': 195
}
```

```python
slo_ang = {
  'abak': 'abacus',
  'abalienacija': 'abalienation',
  'abderit': 'abderite',
  ...
  'žvrkljati': 'whisk'
}
```

```python
rimske_stevilke = {
    1: 'I', 2: 'II', 3: 'III', 4: 'IV',
    5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII',
    9: 'IX', 10: 'X', 20: 'XX', 30: 'XXX',
    40: 'XL', 50: 'L', 100: 'C', 500: 'D',
    1000: 'M'
}
```

```python
met_kocke = {
    1: 1/6, 2: 1/6, 3: 1/6,
    4: 1/6, 5: 1/6, 6: 1/6
}

met_dveh_kock = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36,
    6: 5/36, 7: 6/36, 8: 5/36, 9: 4/36,
    10: 3/36, 11: 2/36, 12: 1/36
}
```

```python
matrika = [
    [1, 1, 4, 1, 1, 1, 1, 1, 1, 1],
    [5, 2, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 4, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

redka_matrika = (6, 10, 1, {
    (0, 2): 4,
    (1, 0): 5,
    (1, 1): 2,
    (2, 4): 3,
    (4, 2): 4
})
```

```python
avtocestni_kriz = {
    'LJ': {'KR': 26, 'CE': 73, 'PO': 51, 'NM': 72},
    'KR': {'LJ': 26, 'JE': 35},
    'JE': {'KR': 35},
    'CE': {'MB': 54, 'LJ': 73},
    'MB': {'CE': 54, 'MS': 60},
    'MS': {'MB': 60},
    'PO': {'LJ': 51, 'KP': 64, 'GO': 63},
    'GO': {'PO': 63},
    'KP': {'PO': 64},
    'NM': {'LJ': 72}
}
```

.center[![Avtocestni križ](slike/avtoceste.png)]

## Osnovne operacije na slovarjih

```
>>> s = {'a': 6, 'b': 2, 'c': 3}
>>> len(s)
3
>>> max(s)
'c'
>>> 3 in s
False
```

Do vrednosti dostopamo **prek ključev**

```
>>> s = {'a': 6, 'b': 2, 'c': 3}
>>> s['a']
6
>>> s['b']
2
>>> s['d']
...
KeyError: 'd'
```

Slovarje lahko tudi **spreminjamo**

```
>>> slovar = {'a': 10, 'b': 20}
>>> slovar['a'] = 50
>>> slovar
{'b': 20, 'a': 50}
>>> slovar['c'] = 100
>>> slovar
{'b': 20, 'a': 50, 'c': 100}
```

Elemente lahko tudi **brišemo**

```
>>> slovar = {'a': 10, 'b': 20}
>>> slovar['a']
10
>>> del slovar['a']
>>> slovar
{'b': 20}
```

## Vgrajene metode na slovarjih

Za **varen dostop** uporabljamo metodo `get`

```
>>> s = {'a': 6, 'b': 2, 'c': 3}
>>> s.get('a')
6
>>> s.get('d')
>>> s.get('d', 0)
0
>>> s.get('a', 0)
6
```

Kaj so najpogostejše črke v Krstu pri Savici?

```
def prestej_pojavitve(niz):

:   pojavitve = {} for znak in niz: if znak in pojavitve:
    pojavitve[znak] += 1 else: pojavitve[znak] = 1 return pojavitve

def prestej_pojavitve(niz):

:   pojavitve = {} for znak in niz: pojavitve[znak] =
    pojavitve.get(znak, 0) + 1 return pojavitve
```

```
>>> prestej_pojavitve('abrakadabra')
```

Pripadajočo vrednost **snamemo** s `pop`

```
>>> slovar = {'a': 10, 'b': 20}
>>> slovar.pop('a')
10
>>> slovar
{'b': 20}
```

**Naključni par** snamemo s `popitem`

```
>>> slovar = {'a': 10, 'b': 20}
>>> slovar.popitem()
('b', 20)
>>> slovar.popitem()
('a', 10)
>>> slovar
{}
```

## Zanka `for`

Z zanko `for` se vozimo po **ključih slovarja**

```
for x in {'a': 1, 'b': 2, 'c': 3}:
    print(x)
```

--

```
c
a
b
```

Vrstni red je odvisen od različice Pythona

Metoda `keys` vrača **ključe** slovarja

```
for x in {'a': 1, 'b': 2, 'c': 3}.keys():
    print(x)
```

```
c
a
b
```

Metoda `values` vrača **vrednosti** slovarja

```
for x in {'a': 1, 'b': 2, 'c': 3}.values():
    print(x)
```

```
3
1
2
```

Metoda `items` vrača **pare** ključev in vrednosti

```
for x in {'a': 1, 'b': 2, 'c': 3}.items():
    print(x)
```

```
('c', 3)
('a', 1)
('b', 2)
```

```
def najvecja_vrednost(s):

:   # Ideja je podobna kot pri seznamih: po vrsti gledamo vse pare
    ključev in # vrednosti v slovarju - vsakič, ko vidimo še večjo
    vrednost, si zapomnimo # njen ključ.

    # Ker slovarji niso urejeni po vrsti, ne moremo začeti s prvim
    elementom. # Lahko pa si pomagamo z metodo popitem(), ki iz
    slovarja odstrani naključen # ključ in njegovo vrednost. max_k,
    max_v = s.popitem() for k, v in s.items(): if v > max_v: max_k,
    max_v = k, v return max_k, max_v
```

Pare običajno **razstavimo v zanki**

```
for par in {'a': 1, 'b': 2, 'c': 3}.items():
    print(par[0], '->', par[1])
```

```
for k, v in {'a': 1, 'b': 2, 'c': 3}.items():
    print(k, '->', v)
```

```
c -> 3
a -> 1
b -> 2
```

```
knjiga_obrazov = {
    'Anka': {'Bogomir', 'Cvetka'},
    'Bogomir': {'Cvetka', 'Dragomir'},
    'Cvetka': {'Anka'},
    'Dragomir': {'Anka', 'Cvetka'},
}
```

```
>>> priporocila(knjiga_obrazov, 'Bogomir')
{'Anka'}
>>> priporocila(knjiga_obrazov, 'Cvetka')
{'Bogomir', 'Cvetka'}
```

## Množice

```python
{1, 2, 3, 4}    set()
```

```
def je_prastevilo(n):

:   

    if n <= 2:

    :   return n == 2

    d = 3 while d * d <= n: if n % d == 0: return False d += 2 return
    True
```

```
majhna_prastevila = {2, 3, 5, 7, ..., 997}

def je_prastevilo(n):
    if n <= majhna_prastevila[-1]:
        return n in majhna_prastevila
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True
```

Osnovne operacije na množicah

```python
>>> {1, 2, 3, 4} | {3, 4, 5, 6}
{1, 2, 3, 4, 5, 6}
>>> {1, 2, 3, 4} & {3, 4, 5, 6}
{3, 4}
>>> {1, 2, 3, 4} - {3, 4, 5, 6}
{1, 2}
>>> 1 in {1, 2, 3, 4}
True
>>> 2 in set()
False
>>> len({1, 2, 3, 2, 1, 2, 3, 2, 1})
3
```

Z zanko `for` se lahko vozimo **po množicah**:

```
for x in {'a', 'b', 'c'}:
    print(x)
```

```
c
b
a
```

Elemente v množico **dodamo** z metodo `add`

```
>>> mn = {10, 20, 30}
>>> mn.add(40)
>>> mn
{40, 10, 20, 30}
```

Element **odstranimo** z `remove`/`discard`

```
>>> mn = {10, 20, 30, 40}
>>> mn.remove(20)
>>> mn
{40, 10, 30}
>>> mn.remove(50)
...
KeyError: 50
```

```
>>> mn = {10, 20, 30, 40}
>>> mn.discard(20)
>>> mn.discard(50)
>>> mn
{40, 10, 30}
```

**Naključni** element **snamemo** s `pop`

```
>>> mn = {10, 20, 30}
>>> mn.pop()
20
>>> mn
{30, 10}
>>> mn.pop()
10
>>> mn
{30}
>>> mn.pop()
30
>>> mn
set()
```

**Več elementov** dodamo z `update`

```
>>> mn = {10, 20, 30}
>>> mn.update([40, 50])
>>> mn
{40, 10, 20, 50, 30}
```

Množico lahko dodamo tudi z `|=`

```
>>> mn = {10, 20, 30}
>>> mn |= {40, 50}
>>> mn
{40, 10, 20, 50, 30}
```

Množico lahko **presekamo** z `&=`

```
>>> mn = {10, 20, 30, 40}
>>> mn &= {30, 40, 50}
>>> mn
{40, 30}
```

Množico lahko **komplementiramo** z `-=`

```
>>> mn = {10, 20, 30, 40}
>>> mn -= {30, 40, 50}
>>> mn
{10, 20}
```

V čem se razlikujeta spodnja programa?

```
>>> mn &= {10, 20}
```

```
>>> mn = mn & {10, 20}
```

## Izpeljani slovarji in množice

Obstajajo tudi **izpeljane množice**

```
mnozica = set()
for x in ...:
    if pogoj:
        mnozica.add(f(x))
```

```
mnozica = {f(x) for x in ... if pogoj}
```

```
def direktna_slika(f, a):

:   slika = set() for x in a: slika.add(f(x)) return slika

def direktna_slika(f, a):

:   return {f(x) for x in a}
```

Obstajajo tudi **izpeljani slovarji**

```
slovar = {}
for x in ...:
    if pogoj:
        slovar[k(x)] = v(x)
```

```
slovar = {k(x): v(x) for x in ... if pogoj}
```

## Razlika med seznami in množicami

**Kdaj uporabimo** sezname, kdaj pa množice?

### Seznami: določen vrstni red in število pojavitev

```python
>>> [1, 2, 3] == [2, 1, 3]
False
>>> [1, 2, 3] == [1, 1, 2, 3]
False
```

### Množice: nedoločen vrstni red in število pojavitev

```python
>>> {1, 2, 3} == {2, 1, 3}
True
>>> {1, 2, 3} == {1, 1, 2, 3}
True
```

## Knjižnica `collections`
