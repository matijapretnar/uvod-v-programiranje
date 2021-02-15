# Zanke


## Zanka `while`

Tako bi z zanko `while` lahko napisali tudi Evklidov algoritem:

```
def gcd(m, n):

:   '''Vrne največji skupni delitelj števil m in n.''' while n !=
    0: m, n = n, m % n return m
```


Koliko je najmanjši $n$, da velja

$$\frac{1}{1} + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n} > 15$$

## A: knjižnica `turtle`

## B: iskanje ničle funkcije

## Neobvezni argumenti z `None`


Število samoglasnikov

```
>>> stevilo_samoglasnikov('UVP je zakon!!!')
4
>>> stevilo_samoglasnikov('čmrlj')
0
>>> stevilo_samoglasnikov('otorinolaringolog')
8
```

Po vseh znakih danega niza se lahko sprehodimo z zanko `for`:

```
def je_samoglasnik(crka):

:   return crka in 'aeiouAEIOU'

def stevilo_samoglasnikov(niz):

:   '''Vrne število samoglasnikov v danem nizu.''' stevilo = 0 for
    znak in niz: if je_samoglasnik(znak): stevilo += 1 return stevilo

def brez_samoglasnikov(niz):

:   '''Vrne niz enak danemu, le da smo iz njega izpustili vse
    samoglasnike.''' niz_brez_samoglasnikov = '' for znak in niz:
    if not je_samoglasnik(znak): niz_brez_samoglasnikov += znak
    return niz_brez_samoglasnikov
```

```
>>> stevilo_samoglasnikov('Uvod v programiranje') 7
>>>
brez_samoglasnikov('Uvod v programiranje') 'vd v prgrmrnj'
```
