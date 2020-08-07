---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: 1.5.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Zanke

Rekurzivni klici nam omogočajo, da se pri izvajanju poljubno mnogokrat vrnemo na poljubne konce programa. V veliki večini primerov pa nam je dovolj že to, da ponovimo določen del programa. Temu so namenjene zanke.

## Zanka `while`


Z zanko `while` določene ukaze izvajamo toliko časa, dokler velja dani pogoj. Pišemo jo kot

```{code-block}
while pogoj:
    # stavki, ki jih ponavljamo
    # od prvega do zadnjega,
    # dokler velja pogoj
```

Na primer, program

```{code-cell}
n = 12
while n < 1000:
    n = n * 2
    print(n)
```

bo `n` nastavil na 12, nato pa ga toliko časa podvojeval in izpisoval, dokler njegova vrednost ne bo presegla 1000.

V programih bomo pogostokrat novo vrednost spremenljivke izračunali tako, da bomo spremenili staro (zato tudi govorimo o spremenljivkah). Na primer, ko bomo šteli vsa praštevila med 1 in 1000000, bomo imeli spremenljivko, ki bo imela na začetku vrednost 0, nato pa jo bomo ob vsakem praštevilu povečali za 1\. V ta namen lahko namesto `n = n * 2` pišemo kar operator `n *= 2`, saj je `*=` operacija, ki spremenljivko na levi pomnoži z vrednostjo na desni. Tudi za ostale operacije obstajajo podobne bližnjice, na primer `-=`, `*=`, `//=` in tako naprej.

```{code-cell}
x = 3
x += 2
x *= 4
x
```

Zgornji program bi tako na krajše lahko napisali kot:

```{code-cell}
n = 12
while n < 1000:
    n *= 2
    print(n)
```


Za primer izračunajmo stopnjo največje potence števila 2, ki še deli število 1580160\. To storimo tako, da število zaporedoma celoštevilsko delimo z 2 in ob vsakem deljenju števec stopnje povečamo za 1\. Ukaze ponavljamo toliko časa, dokler je ostanek pri deljenju z 2 enak 0:

```{code-cell}
n = 1580160
stopnja = 0
while n % 2 == 0:
    n //= 2
    stopnja += 1
    print(stopnja)
stopnja
```

Program bi lahko pretvorili tudi v splošnejšo funkcijo:

```{code-cell}
def celostevilski_logaritem(n, k):
    """Vrne stopnjo največje potence števila k, ki še deli n."""
    stopnja = 0
    while n % k == 0:
        n //= k
        stopnja += 1
    return stopnja
```

```{code-cell}
celostevilski_logaritem(81, 3)
```
```{code-cell}
celostevilski_logaritem(1580160, 2)
```

Isto funkcijo bi lahko napisali tudi z rekurzijo:

```{code-cell}
def celostevilski_logaritem_rek(n, k):
    """Vrne stopnjo največje potence števila k, ki še deli n."""
    if n % k == 0:
        return 1 + celostevilski_logaritem_rek(n // k, k)
    else:
        return 0
```

```{code-cell}
celostevilski_logaritem_rek(81, 3)
```
```{code-cell}
celostevilski_logaritem_rek(1580160, 2)
```

Vseeno v praksi za tiste programe, pri katerih neko stvar ponavljamo toliko časa, dokler velja določen pogoj, raje uporabimo zanko `while`, saj je učinkovitejša (vsaj v Pythonu, v drugih jezikih je rekurzija ravno tako učinkovita). Poleg tega se Python pritoži, če gremo pri rekurziji pregloboko. Običajno se to zgodi takrat, kadar smo rekurzijo napisali tako, da se ne ustavi. Vendar računalnik tega ne more vedeti, zato se Python ustavi po določenem številu klicev ustavi:

```{code-cell}
celostevilski_logaritem_rek(2 ** 2959, 2)
```

```{code-cell}
:tags: ["raises-exception"]
celostevilski_logaritem_rek(2 ** 2960, 2)
```

Pri zankah teh težav ni:

```{code-cell}
celostevilski_logaritem(2 ** 2959, 2)
```

```{code-cell}
celostevilski_logaritem(2 ** 2960, 2)
```

```{code-cell}
celostevilski_logaritem(2 ** 10000, 2)
```

Se pa lahko pri zanki `while` zgodi, da se njeno izvajanje nikoli ne zaključi. Na primer, če bi poklicali `celostevilski_logaritem(12345, 1)`,
bi bil ostanek pri deljenju z 1 v pogoju vedno enak 0 in zanka bi tekla v neskončnost. Ko se naveličamo čakanja, lahko pritisnemo `Ctrl-C` in izvajanje prekinemo.

## Zanka `for`

Zanko `while` torej uporabimo takrat, kadar želimo ukaze ponavljati, dokler velja nek pogoj. Včasih pa že vnaprej vemo, kolikokrat bomo te ukaze ponovili. Na primer, funkcijo za izračun fakultete bi lahko pisali kot:

```{code-cell}
def fakulteta(n):
    """Vrne fakulteto naravnega števila n."""
    produkt = 1
    i = 1
    while i <= n:
        produkt *= i
        i += 1
    return produkt
```

vendar vemo, da se bo zanka izvedla natanko enkrat za vsako število od 1 do `n`. Poleg tega se nam hitro zgodi, da vrstico `i += 1` po nesreči pozabimo ali napišemo kot `i + 1` ali kot `i = 1`, zaradi česar se zanka izvaja v neskončnost. Za primere, ko vemo, kolikokrat izvedemo določeno kodo, raje uporabimo zanko `for`, ki jo pišemo kot:

```{code-block}
for spremenljivka in vrednosti:
    # stavki, ki jih izvedemo
    # po enkrat za vsako izmed
    # podanih vrednost spremenljivke
```

izvede pa se enako, kot če bi napisali
```{code-block}
# v spremenljivko shrani prvo vrednost
# izvedi vse stavke v telesu zanke
# v spremenljivko shrani drugo vrednost
# izvedi vse stavke v telesu zanke
# ...
# v spremenljivko shrani zadnjo vrednost
# izvedi vse stavke v telesu zanke
```

Na primer, čez vse črke danega niza se sprehodimo kot:

```{code-cell}
for znak in 'to je en niz':
    print(znak)
```

samoglasnike pa lahko preštejemo kot:

```{code-cell}
def stevilo_samoglasnikov(niz):
    stevilo = 0
    for znak in niz:
        if znak.lower() in 'aeiou':
            stevilo += 1
    return stevilo
```

```{code-cell}
stevilo_samoglasnikov('Uvod v programiranje')
```

Če se želimo sprehoditi po številih, uporabimo funkcijo `range`. Ta zaporedoma vrača vsa števila v danem razponu:

```{code-cell}
for x in range(5, 10):
    print(x ** 2)
```

Vidimo, da tako kot rezine tudi `range` ne doseže zgornje meje. Če funkciji `range` podamo en argument, bo začela šteti z 0, če pa ji podamo še tretji argument, ga bo uporabila za velikost koraka (kot pri rezinah).

```{code-cell}
for x in range(5):
    print(x)
```

```{code-cell}
for x in range(5, 10, 2):
    print(x)
```

S pomočjo funkcije `range` bi fakulteto torej napisali kot:

```{code-cell}
def fakulteta(n):
    """Vrne fakulteto naravnega števila n."""
    produkt = 1 
    for i in range(1, n + 1):
        produkt *= i
    return produkt
```

```{code-cell}
fakulteta(20)
```

## Stavki `break`, `continue` in `pass`

V zankah lahko uporabimo tudi posebne ukaze, ki spreminjajo običajen potek programa. Stavek `break` prekine trenutno zanko. Na primer:

```{code-cell}
for n in range(1, 5):
    print(n)
    if n == 2 or n == 3:
        break
    print('x')
```

izmenično izpisuje števila od 1 do 4 ter znak `x`. V trenutku, ko pride do števila 2, ki zadošča pogoju `n == 2 or n == 3`, izvajanje zanke v celoti prekine in preneha z izpisovanjem.

Primer je napisan za zanko `for`, vendar enako deluje tudi za zanko `while`.

Stavek `continue` zanke ne ustavi, temveč le preskoči preostanek trenutnega obhoda zanke in gre nazaj na začetek z naslednjo vrednostjo. Na primer:

```{code-cell}
for n in range(1, 5):
    print(n)
    if n == 2 or n == 3:
        continue
    print('x')
```

pri številih 2 in 3, ki zadoščata pogoju, preskoči izpis znaka `x`, ki bi moral slediti.

Tudi stavek `continue` deluje tako za zanko `for` kot za zanko `while`.

Stavek `pass` pa ne stori ničesar. Na primer:

```{code-cell}
for n in range(1, 5):
    print(n)
    if n == 2 or n == 3:
        pass
    print('x')
```

pri številih 2 in 3, ki zadoščata pogoju, vstopi v pogojni stavek, vendar tam ne stori ničesar, zato je izpis enak, kakor bi bil za program brez pogojnega stavka.

Stavek `pass` lahko uporabljamo kjerkoli v Pythonu, ne le v zankah. Najpogosteje ga uporabimo takrat, kadar Python zahteva, da napišemo vsaj en ukaz, vendar ne želimo storiti ničesar. Recimo, da imamo program:

```{code-block}
for x in range(100):
    if x % 2 == 0:
        print(x, 'je sod')
    else:
        print(x, 'je lih')
```

in za trenutek želimo izklopiti izpisovanje sodih števil. Če bi napisali le

```{code-block}
for x in range(100):
    if x % 2 == 0:
        # print(x, 'je sod')
    else:
        print(x, 'je lih')
```

bi se Python pritožil, da je prva veja pogojnega stavka prazna, saj komentarje ignorira. Seveda bi lahko celoten program preuredili v

```{code-block}
for x in range(100):
    if x % 2 != 0:
        print(x, 'je lih')
```

vendar tega ne želimo (sploh pri večjih programih). S pomočjo stavka `pass` pa lahko napišemo

```{code-block}
for x in range(100):
    if x % 2 == 0:
        # print(x, 'je sod')
        pass
    else:
        print(x, 'je lih')
```

Tudi če se odločimo, da bi zopet vklopili izpisovanje, lahko stavek `pass` pustimo v kodi, ker ne stori ničesar.

## Metoda Monte-Carlo

TODO