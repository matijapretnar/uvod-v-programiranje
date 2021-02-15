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

