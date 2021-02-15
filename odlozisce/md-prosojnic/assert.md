Pri tem si lahko pomagamo s stavkom `assert`, ki ob izvajanju preveri, da nek pogoj velja. Če ne velja, sproži izjemo.

## Stavek `assert`

Tudi funkcija `splosni_fibonacci` še ni popolna. Kaj se zgodi, če pokličemo `splosni_fibonacci(-2, 0, 1)`? Ker -2 ni enako ne 0 ne 1, bomo izvedli tretjo vejo pogojnega stavka in izračunali `splosni_fibonacci(-3, 0, 1)`, iz tega pa podobno `splosni_fibonacci(-4, 0, 1)` in tako naprej, vse do trenutka, ko se bo Python pritožil:

```
>>> splosni_fibonacci(-2, 0, 1) Traceback (most recent call last):
... File "...", line 8, in splosni_fibonacci File "...", line 8,
in splosni_fibonacci File "...", line 8, in splosni_fibonacci File
"...", line 8, in splosni_fibonacci File "...", line 8, in
splosni_fibonacci File "...", line 8, in splosni_fibonacci File
"...", line 3, in splosni_fibonacci RecursionError: maximum
recursion depth exceeded in comparison
```

Pravi nam, da je naša rekurzija šla pregloboko. O tem bomo še bolj natančno govorili, zaenkrat pa naj nam tako opozorilo pove, da smo program napisali tako, da se ne bo ustavil. Da podobne situacije preprečimo, lahko uporabimo stavek `assert`, v katerem napišemo pogoj, ki mu mora program zadoščati. Če mu ne, Python javi napako.

```
def splosni_fibonacci(n, a, b):

:   '''Vrne n-ti člen Fibonaccijevega zaporedja, ki se začne z a in
    b.''' assert n >= 0 if n == 0: return a elif n == 1: return b
    else: return splosni_fibonacci(n - 1, b, a + b)
```

```
>>> splosni_fibonacci(-2, 0, 1) Traceback (most recent call last):
... AssertionError
```

Še vedno dobimo napako, vendar je ta bolj obvladljiva, pa še takoj se pojavi. Stavke `assert` uporabljamo, kadar v nadaljevanju programa pričakujemo, da je nekim pogojem zadoščeno. Namesto `assert pogoj` bi seveda lahko pisali tudi nekaj v stilu:

```
if not pogoj:
    # ustavi program
    # javi napako
```

ampak ker je to pogosto koristno, so v ta namen uvedli `assert`.
