---
jupytext:
  cell_metadata_filter: '-all'
  formats: 'md:myst'
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.1
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Razredi

V Pythonu sorodne vrednosti združujemo v _razredih_. Posameznim pripadnikom razredov pravimo _objekti_. Vsi objekti istega razreda uporabljajo isto definicijo metod, vsak izmed njih pa ima svoje vrednosti, ki jim pravimo _atributi_. Na primer, seznami pripadajo razredu `list`. Vsak seznam ima svoje elemente, vsi pa podpirajo iste metode kot so `append`, `pop` ali `sort`, ki se na vsakem seznamu obnašajo na isti način. Nizi pripadajo razredu `str`. Vsak niz ima svoje znake, vsi pa imajo skupno definicije metod kot so `split`, `upper` in podobno.

## Definicije lastnih razredov

Če želimo, lahko definiramo tudi svoj razred. To naredimo z ukazom `class`, ki mu sledi ime razreda (pisano z veliko začetnico) ter zamaknjene definicije metod. Na primer, definirajmo si razred, ki bo predstavljal aritmetična zaporedja $a, a + d, a + 2d, a + 3d, \ldots$. Za začetek definirajmo nobene metode, zato v definicijo napišimo le `pass`.

```{code-cell}
class AritmeticnoZaporedje:
    pass
```

Nove objekte danega razreda dobimo tako, da napišemo ime razreda ter oklepaje:

```{code-cell}
zap = AritmeticnoZaporedje()
zap
```

Dobili smo prazen objekt razreda `AritmeticnoZaporedje`, vendar z njim težko naredimo kaj pametnega. Do atributov objektov dostopamo prek `ime_objekta.ime_atributa`, vendar trenutno zaporedjem nismo nastavili še nobenega atributa:

```{code-cell}
:tags: [raises-exception]

zap.zacetni_clen
```

Na podoben način lahko atribute tudi nastavljamo:

```{code-cell}
zap.zacetni_clen = 2
zap.razlika = 5
```

```{code-cell}
zap.zacetni_clen + 8 * zap.razlika
```

Definirajmo si tri metode: prva bo nastavila atributa, v katerih bosta shranjena začetni člen in razlika, drugi dve pa bosta izračunala člen na danem mestu ter vsoto do vključno tega člena.

```{code-cell}
class AritmeticnoZaporedje:
    def nastavi_atribute(self, zacetni_clen, razlika):
        self.zacetni_clen = zacetni_clen
        self.razlika = razlika

    def clen(self, i):
        return self.zacetni_clen + i * self.razlika

    def vsota(self, i):
        return (i + 1) * self.zacetni_clen + i * (i + 1) // 2 * self.razlika
```

Metode definiramo na enak način kot funkcije, le da na prvem mestu sprejmejo še dodatni argument, ki ga ponavadi imenujemo `self`, prek njega pa dostopamo do objekta, na katerem smo poklicali metodo.

```{code-cell}
zap = AritmeticnoZaporedje()
zap.nastavi_atribute(2, 5)
zap.clen(0)
```

```{code-cell}
zap.vsota(5)
```

Ker objekt brez nastavljenih atributov ni preveč koristen, si jih bomo želeli nastaviti na začetku, ko objekt ustvarimo. To storimo tako, da definiramo posebno _inicializacijsko_ metodo z imenom `__init__`, ki jo bo Python poklical takoj za tem, ko ustvari nov prazen objekt. Metodi `__init__` lahko podamo tudi argumente, ki jih podamo ob konstrukciji objekta. Zgornjo definicijo razreda bi tako bolje napisali kot:

```{code-cell}
class AritmeticnoZaporedje:
    def __init__(self, zacetni_clen, razlika):
        self.zacetni_clen = zacetni_clen
        self.razlika = razlika

    def clen(self, i):
        return self.zacetni_clen + i * self.razlika

    def vsota(self, i):
        return (i + 1) * self.zacetni_clen + i * (i + 1) // 2 * self.razlika
```

```{code-cell}
zap = AritmeticnoZaporedje(2, 5)
zap.clen(8)
```

Seveda lahko ustvarimo tudi več objektov:

```{code-cell}
liha_stevila = AritmeticnoZaporedje(1, 2)
liha_stevila.vsota(99)
```

## Posebne metode

Poleg metode `__init__` smo dogovorjeni še za nekaj posebnih metod, ki se pokličejo ob danih trenutkih. Na primer, trenuten izpis v konzoli je precej nekoristen.

```{code-cell}
zap
```

Izpis lahko popravimo z definicijo metode `__repr__`, ki vrne predstavitev objekta z nizem, Python pa jo pokliče, ko želi izpisati rezultat na konzolo. Podobna ji je metoda `__str__`, ki se pokliče takrat, ko objekt izpišemo. Namen prve je, da vrne izpis, koristen za nadaljnje delo v Pythonu, namen druge pa človeku prijazen izpis.

```{code-cell}
class AritmeticnoZaporedje:
    def __init__(self, zacetni_clen, razlika):
        self.zacetni_clen = zacetni_clen
        self.razlika = razlika

    def __repr__(self):
        return f"AritmeticnoZaporedje({self.zacetni_clen}, {self.razlika})"

    def __str__(self):
        return f"{self.clen(0)}, {self.clen(1)}, {self.clen(2)}, ..."

    def clen(self, i):
        return self.zacetni_clen + i * self.razlika

    def vsota(self, i):
        return (i + 1) * self.zacetni_clen + i * (i + 1) // 2 * self.razlika
```

```{code-cell}
zap = AritmeticnoZaporedje(2, 5)
zap
```

```{code-cell}
print(zap)
```

Takih metod je še precej:

- ko napišemo `x + y`, se na objektu `x` pokliče `x.__add__(y)`, podobno je z ostalimi aritmetičnimi operacijami `__sub__`, `__mul__`, ...
- ko napišemo `x == y`, se na objektu `x` pokliče `x.__eq__(y)`,
- ko napišemo `x in y`, se na objektu `y` pokliče `y.__contains__(x)`,
- ko napišemo `x[i]`, se na objektu `x` pokliče b`x.__getitem__(i)` in tako naprej.

Seznam vseh posebnih metod najdete v [uradni dokumentaciji](https://docs.python.org/3/reference/datamodel.html#special-method-names).

```{code-cell}
class AritmeticnoZaporedje:
    def __init__(self, zacetni_clen, razlika):
        self.zacetni_clen = zacetni_clen
        self.razlika = razlika

    def __repr__(self):
        return f"AritmeticnoZaporedje({self.zacetni_clen}, {self.razlika})"

    def __str__(self):
        return f"{self.clen(0)}, {self.clen(1)}, {self.clen(2)}, ..."

    def __getitem__(self, i):
        return self.zacetni_clen + i * self.razlika

    def __contains__(self, x):
        return (x - self.zacetni_clen) % self.razlika == 0

    def __add__(self, other):
        zacetni_clen_vsote = self.zacetni_clen + other.zacetni_clen
        razlika_vsote = self.razlika + other.razlika
        return AritmeticnoZaporedje(zacetni_clen_vsote, razlika_vsote)

    def __eq__(self, other):
        return self.zacetni_clen == other.zacetni_clen and self.razlka == other.razlika

    def vsota(self, i):
        return (i + 1) * self.zacetni_clen + i * (i + 1) // 2 * self.razlika
```

```{code-cell}
zap1 = AritmeticnoZaporedje(2, 5)
zap2 = AritmeticnoZaporedje(7, 3)
zap1 + zap2
```

```{code-cell}
zap1[8]
```

```{code-cell}
42 in zap2
```

```{code-cell}
zap1 + zap2 == AritmeticnoZaporedje(1, 8)
```

## Iteracija

### Iteratorji

V Pythonu se dostikrat sprehajamo čez znake v nizu, elemente seznama, števila v `range`, ... Vse dosežemo prek tako imenovanih _iteratorjev_. To so objekti, ki imajo posebno vgrajeno metodo `__next__`, ki ob vsakem klicu vrne naslednjo vrednost. Ko vrednosti zmanjka, metoda to sporoči tako, da sproži izjemo `StopIteration`. Za primer napišimo iterator, ki zaporedoma vrača znake niza:

```{code-cell}
class IteratorCezNiz:
    def __init__(self, niz):
        self.niz = niz
        self.indeks = 0

    def __next__(self):
        if self.indeks < len(self.niz):
            znak = self.niz[self.indeks]
            self.indeks += 1
            return znak
        else:
            raise StopIteration
```

```{code-cell}
it = IteratorCezNiz('abc')
```

Metodo `__next__` bi lahko poklicali direktno, kot `it.__next__()`, vendar jo je lepše poklicati prek vgrajene funkcije `next` (ki ne naredi drugega, kot da na svojem argumentu pokliče `__next__`).

```{code-cell}
next(it)
```

```{code-cell}
next(it)
```

```{code-cell}
next(it)
```

```{code-cell}
:tags: [raises-exception]
next(it)
```

Če želimo, se lahko iteratorji tudi nikoli ne končajo, s čimer lahko predstavimo neskončne sezname, na primer vsa Fibonaccijeva števila.

```{code-cell}
class IteratorFibonaccijevih:
    def __init__(self):
        self.a, self.b = 0, 1

    def __next__(self):
        prejsnji_a = self.a
        self.a, self.b = self.b, self.a + self.b
        return prejsnji_a
```

```{code-cell}
fib = IteratorFibonaccijevih()
[next(fib) for _ in range(10)]
```

### Generatorji

V Pythonu obstaja zelo enostaven način, na katerega pišemo iteratorje, in to so _generatorji_. Recimo, da bi želeli le izpisati vse znake v nizu. Tedaj bi lahko napisali funkcijo:

```{code-cell}
def znaki_niza(niz):
    i = 0
    while i < len(niz):
        print(niz[i])
        i += 1
```

Pri funkciji nalašč nismo uporabili zanke `for`, saj bi bilo to goljufanje.

```{code-cell}
znaki_niza("abc")
```

To je res izpisalo vse znake, vendar si z njimi ne moremo pomagati, saj so šli naravnost na konzolo. Če bi jih želeli vrniti, bi lahko napisali sledečo funkcijo, vendar bi ta ob prvem `return` prenehala z izvajanjem:

```{code-cell}
def znaki_niza(niz):
    i = 0
    while i < len(niz):
        return niz[i]
        i += 1
```

```{code-cell}
znaki_niza("abc")
```

Tu v igro pridejo _generatorji_. Dobimo jih tako, da namesto `return` napišemo `yield`. Ko bo izvajanje klica prišlo do ukaza `yield`, se ne bo končalo, temveč le zaustavilo, ter se od tam nadaljevalo ob naslednjem klicu `next`.

```{code-cell}
def znaki_niza(niz):
    i = 0
    while i < len(niz):
        yield niz[i]
        i += 1
```

```{code-cell}
gen = znaki_niza("abc")
```

```{code-cell}
gen
```

```{code-cell}
next(gen)
```

```{code-cell}
next(gen)
```

```{code-cell}
next(gen)
```

```{code-cell}
:tags: [raises-exception]
next(gen)
```

Tudi generator Fibonaccijevih števil lahko dobimo na podoben način:

```{code-cell}
def fibonaccijeva_stevila(a=0, b=1):
    while True:
        yield a
        a, b = b, a + b
```

```{code-cell}
f = fibonaccijeva_stevila()
[next(f) for _ in range(10)]
```

```{code-cell}
f = fibonaccijeva_stevila(0, 10)
[next(f) for _ in range(10)]
```

Pri poimenovanju je treba biti natančen: `fibonaccijeva_stevila` niso generator, temveč funkcija, ki ob vsakem klicu vrne generator, ki je posebna vrsta iteratorja.

```{code-cell}
fibonaccijeva_stevila
```

```{code-cell}
fibonaccijeva_stevila()
```

### Iterabilni objekti

Objekti, po katerih se sprehajamo z zanko `for`, niso iteratorji. Na primer, nizi so sestavljeni natanko iz svojih znakov, zato si ne morejo "zapomniti", katere znake so že vrnili in katerih ne. Ampak, kot smo videli, iz njih lahko naredimo smiselne iteratorje. Takim objektom pravimo _iterabilni_. Natančneje zanka `for x in obj: ...` deluje na sledeči način:

1. pokliči `iter(obj)`, da iz iterabilnega objekta `obj` dobiš iterator `it`
2. pokliči `next(it)`, da dobiš naslednjo vrednost
3. vrednost shrani v spremenljivko `x`
4. izvedi ukaze `...`
5. ponavljaj korake od 2 do 4, dokler korak 2 ne sproži izjeme `StopIteration`
6. ko dobiš izjemo, končaj

Če želimo na objektih svojega razreda podpreti zanko `for`, moramo definirati metodo `__iter__`, ki bo vrnila iskani iterator. Na primer, iterator po aritmetičnih zaporedjih bi lahko napisali kot:

```{code-cell}
class AritmeticnoZaporedje:
    def __init__(self, zacetni_clen, razlika):
        self.zacetni_clen = zacetni_clen
        self.razlika = razlika

    def __iter__(self):
        x = self.zacetni_clen
        while True:
            yield x
            x += self.razlika
```

```{code-cell}
zap = AritmeticnoZaporedje(2, 5)
```

```{code-cell}
for x in zap:
    print(x)
    if x > 100:
        break
```
