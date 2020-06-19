# Zanke

Rekurzivni klici nam omogočajo, da se pri izvajanju poljubno mnogokrat vrnemo na poljubne konce programa. V veliki večini primerov pa nam je dovolj že to, da ponovimo določen del programa. Temu so namenjene zanke.

## Zanka `while`

Z zanko `while` določene ukaze izvajamo toliko časa, dokler velja dani pogoj.

Na primer, program

```python
n = 12
while n < 1000:
    n = n * 2
    print(n)
```

bo `n` nastavil na 12, nato pa ga toliko časa podvojeval, dokler njegova vrednost ne bo dosegla 1000\. Program bo tako izpisal:

```python
24
48
96
192
384
768
1536
```

V programih bomo pogostokrat novo vrednost spremenljivke izračunali tako, da bomo spremenili staro (zato tudi govorimo o spremenljivkah). Na primer, ko bomo šteli vsa praštevila med 1 in 1000000, bomo imeli spremenljivko, ki bo imela na začetku vrednost 0, nato pa jo bomo ob vsakem praštevilu povečali za 1\. V ta namen lahko namesto `n = n * 2` pišemo kar operator `n *= 2`, saj je `*=` operacija, ki spremenljivko na levi pomnoži z vrednostjo na desni. Tudi za ostale operacije obstajajo podobne bližnjice, na primer `-=`, `*=`, `//=` in tako naprej.

```python
n = 12
while n < 1000:
*   n *= 2
    print(n)
```

```
>>> x = 3
>>> x += 2
>>> x *= 4
>>> x
20
```

Za primer izračunajmo stopnjo največje potence števila 2, ki še deli število 1580160\. To storimo tako, da število zaporedoma celoštevilsko delimo z 2 in ob vsakem deljenju števec stopnje povečamo za 1\. Ukaze ponavljamo toliko časa, dokler je ostanek pri deljenju z 2 enak 0:

```
n = 1580160 stopnja = 0 while n % 2 == 0: n //= 2 stopnja += 1
```

Ko se izvajanje zaključi, lahko preverimo, da velja

```
>>> stopnja 7
```

Zgornji program lahko pretvorimo v splošnejšo funkcijo:

```
def stopnja_najvecje_potence(n, k):

:   '''Vrne stopnjo največje potence števila k, ki še deli n.'''
    stopnja = 0 while n % k == 0: n //= k stopnja += 1 return stopnja
```

```
>>> stopnja_najvecje_potence(81, 3) 4
>>>
stopnja_najvecje_potence(1580160, 2) 7
```

Isto funkcijo bi lahko napisali tudi z rekurzijo:

```
def stopnja_najvecje_potence_rek(n, k):

:   '''Vrne stopnjo največje potence števila k, ki še deli n.'''
    if n % k == 0: return 1 + stopnja_najvecje_potence_rek(n // k, k)
    else: return 0
```

```
>>> stopnja_najvecje_potence_rek(1580160, 2) 7
>>>
stopnja_najvecje_potence_rek(81, 3) 4
```

V praksi pa za tiste programe, pri katerih neko stvar ponavljamo toliko časa, dokler velja določen pogoj, raje uporabimo zanko `while`, saj je učinkovitejša (vsaj v Pythonu, v drugih jezikih je rekurzija ravno tako učinkovita). Tako bi z zanko `while` lahko napisali tudi Evklidov algoritem:

```
def gcd(m, n):

:   '''Vrne največji skupni delitelj števil m in n.''' while n !=
    0: m, n = n, m % n return m
```

Kot smo videli, se Python pritoži, če gremo pri rekurziji pregloboko. Običajno se to zgodi takrat, kadar smo rekurzijo napisali tako, da se ne ustavi. Vendar računalnik tega ne more vedeti, zato se Python ustavi takrat, ko naredimo približno 1000 rekurzivnih klicev:

```
>>> stopnja_najvecje_potence_rek(2 ** 985, 2) 985
>>>
stopnja_najvecje_potence_rek(2 ** 986, 2) Traceback (most recent
call last): ... File "...", line 4, in
stopnja_najvecje_potence_rek File "...", line 4, in
stopnja_najvecje_potence_rek File "...", line 4, in
stopnja_najvecje_potence_rek File "...", line 4, in
stopnja_najvecje_potence_rek File "...", line 4, in
stopnja_najvecje_potence_rek File "...", line 3, in
stopnja_najvecje_potence_rek RecursionError: maximum recursion depth
exceeded in comparison
```

Pri zankah teh težav ni:

```
>>> stopnja_najvecje_potence(2 ** 985, 2) 985
>>>
stopnja_najvecje_potence(2 ** 986, 2) 986
>>>
stopnja_najvecje_potence(2 ** 10000, 2) 10000
```

Seveda tudi pri zanki `while` obstaja nevarnost, da se njeno izvajanje nikoli ne zaključi. Na primer, če bi poklicali

```
>>> stopnja_najvecje_potence(12345, 1)
```

bi bil ostanek pri deljenju z 1 v pogoju vedno enak 0, zato bi zanka tekla v neskončnost. Ko se naveličamo čakanja, lahko pritisnemo `Ctrl-C` in izvajanje prekinemo.

Koliko je najmanjši $n$, da velja

$$\frac{1}{1} + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n} > 15$$

## A: knjižnica `turtle`

## B: iskanje ničle funkcije

Poglejmo si enostaven algoritem, s katerim lahko izračunamo kvadratni koren pozitivnega števila. Recimo, da že vemo, da se koren števila $n$ nahaja na intervalu $[a, b]$ (npr. vemo, da se zagotovo nahaja na intervalu $[0, n]$). Naj bo $c = (a + b) / 2$ sredina intervala. Tedaj ločimo tri primere:

- Če imamo srečo, je $c^2 = n$, zato smo našli koren in postopek lahko končamo.
- Če je $c^2 > n$, je tudi $c > \sqrt{n}$, zato lahko na podoben način nadaljujemo z iskanjem korena na intervalu $[a, c]$.
- V nasprotnem primeru pa mora biti $c^2 < n$ in $c < \sqrt{n}$, zato lahko z iskanjem nadaljujemo na intervalu $[c, b]$.

Ker interval vedno razdelimo na pol, postopku pravimo _bisekcija_. Ker lahko realna števila poljubno delimo, se zgornji postopek ne bo nikoli ustavil (razen, če imamo srečo in naletimo točno na koren). Toda ker nas zanima le približek korena, lahko postopek ustavimo takrat, ko se krajišči intervala razlikujeta za dovolj majhno vrednost $\varepsilon$. Načeloma v algoritmu prvo možnost (ko je $c^2 = n$) kar izpustimo, saj je preveč redka, pa tudi brez nje algoritem najde pravo rešitev.

V Pythonu bi algoritem zapisali kot:

```
def kvadratni_koren(n, eps):

:   '''Z metodo bisekcije poišče koren števila n.''' a, b = 0, n
    while b - a > eps: c = (a + b) / 2 if c * c > n: b = c else: a =
    c return c
```

```
>>> kvadratni_koren(10, 1e-5) 3.1622791290283203
>>>
kvadratni_koren(10, 1e-10) 3.1622776602307567
>>>
kvadratni_koren(10, 1e-15) 3.162277660168379
```

Na podoben način lahko približno izračunamo ničlo zvezne realne funkcije $f$ na intervalu $[a, b]$, če vemo, da sta vrednosti $f(a)$ in $f(b)$ različno predznačeni. Če je $c = (a + b) / 2$ zopet sredina intervala, ločimo tri primere:

- Če imamo srečo, je $f(c) = 0$, zato smo našli ničlo in postopek lahko končamo. Sicer je $f(c)$ neničelno število, zatorej ima nek predznak.
- Če je predznak $f(c)$ različen od predznaka $f(a)$ lahko na podoben način nadaljujemo z iskanjem ničle na intervalu $[a, c]$.
- V nasprotnem primeru pa mora biti predznak $f(c)$ različen od predznaka $f(b)$ (ker imata $f(a)$ in $f(b)$ različen predznak), zato lahko z iskanjem nadaljujemo na intervalu $[c, b]$.

Podobno kot prej bi algoritem zapisali kot:

```
def bisekcija(f, a, b, eps):

:   '''Z metodo bisekcije izračuna ničlo f na intervalu [a,
    b].''' while b - a > eps: c = (a + b) / 2 if f(a) * f(c) < 0:
    b = c else: a = c return c
```

```
>>> import math
>>> bisekcija(math.sin, 2, 4, 0.01) 3.1484375
>>> bisekcija(math.sin, 2, 4, 0.00001) 3.1415939331054688
>>>
bisekcija(math.sin, 2, 4, 10 ** -10) 3.141592653642874
>>>
bisekcija(math.sin, 2, 4, 1e-10) 3.141592653642874
```

Zgoraj lahko opazimo, da nam Python dopušča, da za argumente funkcij ne podajamo le števil, temveč tudi druge funkcije. Pravimo, da podpira _funkcije višjega reda_. Če želimo, lahko za argumente podamo tudi funkcije, ki smo jih definirali sami:

```
def moj_f(x):

:   return x ** 2 - 2
```

```
>>> bisekcija(moj_f, 1, 2, 0.000001) 1.4142141342163086
```

Če se nam neke funkcije, ki bi jo uporabili samo v enem primeru (kot je ta zgoraj), ne da poimenovati, lahko uporabimo _anonimne_ oziroma _lambda_ funkcije, v katerih za telo napišemo enostaven izraz. Zgornji primer bi z njimi pisali kot:

```
>>> bisekcija(lambda x: x ** 2 - 2, 1, 2, 0.000001)
1.4142141342163086
```

Funkcij z zapletenejšim telesom in tistih, v katerih uporabljemo več stavkov, ne pišemo z lambdami. Tako ali tako je bolje, da zapletenejšim funkcijam damo ime, da se vidi, kaj počnejo.

## Neobvezni argumenti z `None`

## Zanka `for` na nizih

Zanko `while` torej uporabimo takrat, kadar želimo ukaze ponavljati, dokler velja nek pogoj. Včasih pa že vnaprej vemo, kolikokrat bomo te ukaze ponovili. Na primer, funkcijo za izračun fakultete bi lahko pisali kot:

```
def fakulteta(n):

:   '''Vrne fakulteto naravnega števila n.''' produkt = 1 i = 1
    while i <= n: produkt *= i i += 1 return produkt
```

vendar vemo, da se bo zanka izvedla natanko enkrat za vsako število od 1 do $n$. Poleg tega se nam hitro zgodi, da vrstico `i += 1` po nesreči pozabimo ali napišemo kot `i + 1` ali kot `i = 1`, zaradi česar se zanka izvaja v neskončnost. Za primere, ko vemo, kolikokrat izvedemo določeno kodo, raje uporabimo zanko `for`.

```
for spremenljivka in podane_vrednosti:
    # stavki, ki se izvedejo
    # po enkrat za vsako izmed
    # podanih vrednost spremenljivke
```

Z zanko `for` se lahko vozimo **po nizih**

```python
for x in 'abc':
    print(x)
```

```python
a
b
c
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

Kot vidimo zgoraj, lahko vejo `else` tudi izpustimo (tako v običajnem kot v razširjenem pogojnem stavku). V tem primeru se ob neizpolnjevanju pogoja ne zgodi nič.

## Zanka for na `range`, `enumerate` in `zip`

Na primer, fakulteto števila 10 bi lahko izračunali kot:

```
fakulteta10 = 1 for i in range(1, 11): fakulteta10 *= i
```

```
>>> fakulteta10 3628800
```

V zanki `for` smo uporabili funkcijo `range`, ki vrne vsa cela števila v razponu od vključno prvega do tistega pred drugim (tako kot pri rezinah). V naši zanki `for` se spremenljivka `i` torej sprehodi po vseh vrednostih od `1` do `10`. Koda se obnaša tako, kot če bi pisali:

```
fakulteta10 = 1 i = 1 fakulteta10 *= i i = 2 fakulteta10*= i i = 3
fakulteta10 *= i i = 4 fakulteta10*= i i = 5 fakulteta10 *= i i = 6
fakulteta10*= i i = 7 fakulteta10 *= i i = 8 fakulteta10*= i i = 9
fakulteta10 *= i i = 10 fakulteta10*= i
```

Funkcijo `fakulteta` pa bi napisali kot:

```
def fakulteta(n):

:   '''Vrne fakulteto naravnega števila n.''' produkt = 1 for i in
    range(1, n + 1): produkt *= i return produkt
```

Z zanko `for` se lahko vozimo **po razponih**

```python
for x in range(5):
    print(x)
```

```python
0
1
2
3
4
```

Z zanko `for` se lahko vozimo **po razponih**

```python
for x in range(5, 10):
    print(x)
```

```python
5
6
7
8
9
```

Z zanko `for` se lahko vozimo **po razponih**

```python
for x in range(5, 10, 2):
    print(x)
```

```python
5
7
9
```

Dostikrat želimo hkrati dostopati do elementov seznama in njihovih indeksov.

Predstavimo polinome s seznamom koeficientov, urejenim od prostega proti vodilnemu členu. Polinom $3 - x^2$ bi tako predstavili s seznamom `[3, 0, -1]`. Pri izračunu vrednosti polinoma želimo hkrati dostopati tako do koeficientov kot do njihovih indeksov, ki ustrezajo potenci. To lahko storimo na več načinov. Lahko se vozimo po indeksih in prek njih dostopamo do koeficientov:

```
def vrednost_polinoma(koeficienti, tocka):

:   '''Vrne vrednost polinoma z danimi koeficienti v dani
    točki.''' vsota = 0 for i in range(len(koeficienti)): koeficient
    = koeficienti[i] vsota += koeficient * tocka ** i return vsota
```

```
>>> vrednost_polinoma([3, 0, 1], 1) 4
>>>
vrednost_polinoma([3, 0, 1], 2) 7
```

Lahko se vozimo po koeficientih in hkrati povečujemo števec indeksa:

```
def vrednost_polinoma(koeficienti, tocka):

:   '''Vrne vrednost polinoma z danimi koeficienti v dani
    točki.''' vsota = 0 i = 0 for koeficient in koeficienti: vsota +=
    koeficient * tocka ** i i += 1 return vsota
```

Najbolj enostavno pa je, da uporabimo funkcijo `enumerate`, ki vrne zaporedje parov, v katerih so druge komponente vrednosti danega seznama, prve komponente pa njihovi indeksi:

> ```
> >> list(enumerate([20, 200, 2000])) [(0, 20), (1, 200), (2,
> 2000)]
> >> list(enumerate('beseda')) [(0, 'b'), (1, 'e'),
> (2, 's'), (3, 'e'), (4, 'd'), (5, 'a')]
> ```

S pomočjo funkcije `enumerate` lahko vrednost polinoma izračunamo kot:

```
def vrednost_polinoma(koeficienti, tocka):

:   '''Vrne vrednost polinoma z danimi koeficienti v dani
    točki.''' vsota = 0 for i, koeficient in enumerate(koeficienti):
    vsota += koeficient * tocka ** i return vsota
```

Kot vidimo, lahko tudi v zanki `for` uporabimo razstavljanje naborov, in pare, ki nam jih podaja `enumerate`, takoj shranimo v dve spremenljivki.

Paziti moramo, da indeksa ne računamo s pomočjo metode `.index`, saj je ta način prvič neučinkovit, drugič pa ne bi vedno delovala pravilno, saj `.index` vrne indeks prve pojavitve iskane vrednosti:

```
def napacna_vrednost_polinoma(koeficienti, tocka):

:   '''Vrne vrednost polinoma z danimi koeficienti v dani točki.''' vsota = 0 for koeficient in koeficienti: i = koeficienti.index(koeficient) vsota += koeficient * tocka ** i return vsota
```

```
>>> vrednost_polinoma([0, 2, 0, 2], 3) 60
>>> napacna_vrednost_polinoma([0, 2, 0, 2], 3) 12
```

Ker je v spodnjem klicu funkcije metoda `.index` za indeks prve pojavitve vrednosti 2 obakrat vrnila 1, je funkcija vrnila $2 \cdot 3^1 + 2 \cdot 3^1 = 6$ namesto $2 \cdot 3^1 + 2 \cdot 3^3 = 60$.

```
Podobno kot `enumerate` deluje funkcija `zip`, ki sprejme več seznamov,
vrne pa zaporedje naborov istoležnih elementov:
```

> > > list(zip([10, 20, 30], [4, 5, 6])) [(10, 4), (20, 5), (30, 6)] list(zip([10, 20, 30], [4, 5, 6], 'abc')) [(10, 4, 'a'), (20, 5, 'b'), (30, 6, 'c')] ```

Funkciji se reče `zip`, ker združuje elemente različnih seznamov tako, kot zadrga. Vrnjeno zaporedje ima toliko elementov, kot najkrajši argument funkcije:

>

> > > list(zip([10, 20, 30], [4, 5, 6], 'ab')) [(10, 4, 'a'), (20, 5, 'b')]

S pomočjo funkcije `zip` lahko enostavno izračunamo skalarni produkt:

```
def skalarni_produkt(vektor1, vektor2):

:   '''Vrne skalarni produkt dveh vektorjev iste dimenzije.'''
    assert len(vektor1) == len(vektor2) vsota = 0 for x1, x2 in
    zip(vektor1, vektor2): vsota += x1 * x2 return vsota
```

```
>>> skalarni_produkt([1, -2, 5], [-2, 5, 2]) -2
```

Z zanko `for` se lahko vozimo po `enumerate`:

```
for x in enumerate('abc'):
    print(x)
```

```
(0, 'a')
(1, 'b')
(2, 'c')
```

```
for i, x in enumerate('abc'):
    print(i, x)
```

```
0 a
1 b
2 c
```

Pare običajno **razstavimo v zanki**

```
for par in enumerate('abc'):
    print(par[0], '->', par[1])
```

```
for i, znak in enumerate('abc'):
    print(i, '->', znak)
```

```
0 -> a
1 -> b
2 -> c
```

Z zanko `for` se lahko vozimo po `zip`:

```
for x in zip('xyz', [10, 20, 30, 40]):
    print(x)
```

```
('x', 10)
('y', 20)
('z', 30)
```

```
for x, y in zip('xyz', [10, 20, 30, 40]):
    print(x, y)
```

```
x 10
y 20
z 30
```

```
for par in zip('abc', [10, 20, 30, 40]):
    print(par[0], '->', par[1])
```

```
for x, y in zip('abc', [10, 20, 30, 40]):
    print(x, '->', y)
```

```
a -> 10
b -> 20
c -> 30
```

## Stavki `break`, `continue`, `pass`

V zankah lahko uporabimo tudi posebne ukaze, ki spreminjajo običajen potek programa. Stavek `break` prekine trenutno zanko. Na primer:

```python
for n in range(1, 5):
    print(n)
    if n == 2 or n == 3:
        break
    print('x')
```

izmenično izpisuje števila od 1 do 4 ter znak `x`. V trenutku, ko pride do števila 2, ki zadošča pogoju `n == 2 or n == 3`, izvajanje zanke v celoti prekine, zato izpiše le

```python
1
x
2
```

Primer je napisan za zanko `for`, vendar enako deluje tudi za zanko `while`.

Stavek `continue` zanke ne ustavi, temveč le preskoči preostanek trenutnega obhoda zanke in gre nazaj na začetek z naslednjo vrednostjo. Na primer:

```
for n in range(1, 5):
    print(n)
    if n == 2 or n == 3:
        continue
    print('x')
```

pri številih 2 in 3, ki zadoščata pogoju, preskoči izpis znaka `x`, ki bi moral slediti. Celoten izpis je tako:

```
1
x
2
3
4
x
```

Tudi stavek `continue` deluje tako za zanko `for` kot za zanko `while`.

Stavek `pass` pa ne stori ničesar. Na primer:

```
for n in range(1, 5):
    print(n)
    if n == 2 or n == 3:
        pass
    print('x')
```

pri številih 2 in 3, ki zadoščata pogoju, vstopi v pogojni stavek, vendar tam ne stori ničesar. Tako je izpis enak, kakor bi bil za program brez pogojnega stavka:

```
1
x
2
x
3
x
4
x
```

Stavek `pass` lahko uporabljamo kjerkoli v Pythonu, ne le v zankah. Najpogosteje ga uporabimo takrat, kadar Python zahteva, da napišemo vsaj en ukaz, vendar ne želimo storiti ničesar. Recimo, da imamo program:

```
for x in range(100):
    if x % 2 == 0:
        print(x, 'je sod')
    else:
        print(x, 'je lih')
```

in za trenutek želimo izklopiti izpisovanje sodih števil. Če bi napisali le

```
for x in range(100):
    if x % 2 == 0:
        # print(x, 'je sod')
    else:
        print(x, 'je lih')
```

bi se Python pritožil, da je prva veja pogojnega stavka prazna, saj komentarje ignorira. Seveda bi lahko celoten program preuredili v

```
for x in range(100):
    if x % 2 != 0:
        print(x, 'je lih')
```

vendar tega ne želimo (sploh pri večjih programih). S pomočjo stavka `pass` pa lahko napišemo

```
for x in range(100):
    if x % 2 == 0:
        # print(x, 'je sod')
        pass
    else:
        print(x, 'je lih')
```

Tudi če se odločimo, da bi zopet vklopili izpisovanje, lahko stavek `pass` pustimo v kodi, ker ne stori ničesar.

## Monte-Carlo simulacije

`random.random()` vrne naključno realno število na intervalu `[0, 1]`

```python
for _ in range(10):
    print(random.random())
```

```python
0.269454709396
0.150338688416
0.86826547468
0.645895807098
0.772181460437
0.522534622302
0.472586885944
0.0620787396277
0.913226625841
0.248149046053
```

`random.uniform(a, b)` vrne naključno realno število na intervalu `[a, b]`

```python
for _ in range(10):
    print(random.uniform(10, 15))
```

```python
12.8787811514
12.6687121738
12.1844239968
11.1800356184
13.2297206416
10.4020532268
14.9780516491
13.1393786622
14.3589751972
12.4133107171
```

`random.randint(a, b)` vrne naključno naravno število na intervalu `[a, b]`

```python
for _ in range(10):
    print(random.randint(10, 15))
```

```python
10
15
14
12
12
12
13
11
11
10
```

`random.randrange(a, b)` vrne naključno naravno število na intervalu `[a, b)`

```python
for _ in range(10):
    print(random.randrange(10, 15))
```

```python
14
11
11
14
14
11
14
13
10
14
```

`random.choice(elementi)` vrne naključno izbran element

```python
for _ in range(10):
    print(random.choice([1, 10, 50]))
```

```python
1
50
1
50
50
1
10
10
1
1
```

`random.choice(elementi)` vrne naključno izbran element

```python
for _ in range(10):
    print(random.choice('abc'))
```

```python
b
c
b
b
c
a
a
c
b
b
```

`random.sample(elementi, k)` vrne `k` naključno izbranih elementov

```python
for _ in range(10):
    print(random.sample('abcdefg', 3))
```

```python
['f', 'd', 'g']
['g', 'a', 'd']
['f', 'g', 'e']
['b', 'f', 'a']
['g', 'c', 'd']
['g', 'c', 'a']
['b', 'f', 'c']
['b', 'f', 'a']
['g', 'f', 'e']
['d', 'g', 'e']
```

`random.shuffle` naključno premeša seznam

```python
>>> seznam = [10, 20, 30, 40, 50]
>>> random.shuffle(seznam)
>>> seznam
[30, 20, 40, 10, 50]
```

## Met poštenega kovanca

```python
for _ in range(10):
    print(posteni_kovanec())
```

```python
cifra
grb
grb
cifra
cifra
cifra
grb
grb
grb
cifra
```

## Met nepoštenega kovanca

```python
for _ in range(10):
    print(neposteni_kovanec(0.2))
```

```python
cifra
cifra
grb
cifra
cifra
cifra
cifra
grb
cifra
cifra
```

Met nepoštene kocke

## Kako generiramo naključne vrednosti?

background-image: url(slike/generator.jpg)

Cenejši način je uporaba psevdonaključnih števil

```
1234

<sup>2</sup>

 = 01**5227**56
5227

<sup>2</sup>

 = 27**3215**29
3215

<sup>2</sup>

 = 10**3362**25
3362

<sup>2</sup>

 = 11**3030**44
3030

<sup>2</sup>

 = 09**1809**00
```

Začetnemu številu pravimo seme

Seme lahko nastavimo z `random.seed`

```python
>>> random.seed(3)
>>> random.random()
0.23796462709189137
>>> random.random()
0.5442292252959519
>>> random.seed(3)
>>> random.random()
0.23796462709189137
>>> random.random()
0.5442292252959519
```

## Generator psevdonaključnih števil

## Linearni kongruenčni generator

background-image: url(slike/generator.jpg)

Izračun števila (\pi)

V 28 metih kovanca je padlo 20 cifer. Je kovanec pošten?

Kako bi se lahko izognili razmišljanju?
