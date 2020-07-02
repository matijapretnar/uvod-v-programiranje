---
jupytext:
  cell_metadata_filter: '-all'
  formats: 'md:myst'
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

# Uvod v Python

## Aritmetični izrazi

Videli smo, da lahko v Pythonu seštevamo, seveda pa so nam voljo tudi ostale osnovne računske operacije: `-` za odštevanje, `*` za množenje in `**` za potenciranje. Za deljenje Python pozna dve operaciji: običajno deljenje `/` in pa celoštevilsko deljenje `//`, ki zavrže morebitni ostanek. Če želimo izračunati samo ostanek, uporabimo `%`. Prioriteta operatorjev je določena tako kot običajno: najtesneje veže potenciranje, nato množenje in deljenji, nazadnje pa seštevanje in odštevanje. Če želimo vrstni red spremeniti, uporabimo običajne oklepaje. Še to: da je koda bolj berljiva, damo na vsaki strani operatorja po en presledek.

```{code-cell}
(1 + 5) ** (9 - 2)
```

```{code-cell}
123 / 10
```

```{code-cell}
123 // 10
```

```{code-cell}
123 % 10
```

```{code-cell}
123 ** (45 + 67)
```

Vidimo, da velika števila Pythonu ne povzročajo velikih težav.

```{attention}
Razmislite, kako bi izračunali predzadnjih sto števk števila $2^{12345}$?
```

## Spremenljivke

Izračunane vrednosti si lahko shranimo tudi v spremenljivke, ki jih potem uporabljamo v kasnejših izračunih. Za to uporabimo _prireditveni stavek_ oblike

```
ime_spremenljivke = vrednost_ki_jo_zelimo_shraniti
```

na primer:

```{code-cell}
a = 3 + 3
```

Za razliko od aritmetičnih izrazov prireditveni stavek ne vrne nobene vrednosti, zato se izhodna celica ne prikaže. Vseeno pa lahko vidimo, da je Python vrednost izračunal in jo shranil, saj sledeči izraz upošteva, da je `a` enak 6:

```{code-cell}
7 * a
```

V celici lahko zaporedoma izvedemo tudi več ukazov:

```{code-cell}
b = a + 8
c = 3 * b
a + b + c
5 * c
```

Vidimo, da se je v izhodni celici prikazala le vrednost zadnjega izraza.

```{code-cell}
a, b = 10, 15
a + b
```

Vrednost spremenljivke lahko tudi povozimo z novo vrednostjo, vendar to na preostale spremenljivke ne vpliva, saj se vedno shrani tista vrednost, ki smo jo podali v prireditvenem stavku.

```{code-cell}
a = 10 
b = a + 3
b
```

Na primer, če vrednost `a` povozimo, se vrednost `b` ne spremeni, saj je prireditveni stavek `b = a + 3` najprej izračunal vrednost desne strani, torej `13`, in v `b` shranil število samo.

```{code-cell}
a = 25
b
```

Za primer daljšega programa si oglejmo [Fermijevo oceno](https://sl.wikipedia.org/wiki/Fermijev_problem) števila učiteljev matematike v slovenskih osnovnih šolah:

```{code-cell}
stevilo_slovencev = 2000000
pricakovana_zivljenska_doba = 75
velikost_generacije = stevilo_slovencev / pricakovana_zivljenska_doba
stevilo_osnovnosolcev = 9 * velikost_generacije
stevilo_razredov = stevilo_osnovnosolcev / 25
stevilo_ur_matematike_na_teden = 4.5 * stevilo_razredov
stevilo_uciteljev_matematike = stevilo_ur_matematike_na_teden / 20
stevilo_uciteljev_matematike
```

V Sloveniji bi tako moralo biti približno 2000 učiteljev matematike. Opazimo, da lahko imena spremenljivk vsebujejo več kot eno črko, česar smo navajeni v matematiki. V programiranju je zelo pomembno, da so imena čimbolj opisna, saj tako hitreje razumemo, kaj počne program.

## Funkcije

Pod imeni pa se ne skrivajo samo števila temveč tudi funkcije. Na primer, Python poleg aritmetičnih operacij ponuja osnovne funkcije, kot na primer `max` in `min` za izračun maksimuma in minimuma. Pokličemo jih tako, da za imenom funkcije v oklepajih naštejemo argumente, ločene z vejicami:

```{code-cell}
max(3, 6)
```

```{code-cell}
min(12, -5)
```

```{code-cell}
max(min(10, 20), 30 // 2)
```

Matematične funkcije so na voljo v ločeni knjižnici `math`. Do njih lahko dostopamo na dva osnovna načina:

Knjižnico uvozimo s stavkom `import math`, nato pa do funkcij in konstant dostopamo tako, da dodamo `math.` pred vsako ime:

```{code-cell}
import math
math.sqrt(2) / 2
```

```
math.sin(math.pi / 4)
```

Drugi način pa je, da iz knjižnice s stavkom `from math import ...` uvozimo posamezne vrednosti, nato pa do njih dostopamo direktno:

```{code-cell}
from math import sqrt, sin, pi
```

```{code-cell}
sqrt(2) / 2
```

```{code-cell}
sin(pi)
```

```{attention}
V zadnjem ukazu nismo dobili pričakovanega odgovora 0\. Računalnik namreč ne dela s čisto pravimi realnimi števili, temveč z njihovimi približki, ki jim pravimo *števila s plavajočo vejico*. Za ta števila običajno najprej zapišemo decimalke (ki jim pravimo *mantisa*), nato pa še eksponent. Število, ki smo ga dobili, je tako enako približno $1{,}22 \cdot 10^{-16}$, saj `e-16` pomeni $10^{-16}$. Na primer `3.2445e2` pa označuje število $324{,}45 = 3{,}2445 \cdot 10^2$).
```

Obstaja tudi tretji način, ko iz knjižnice s stavkom `from math import *` uvozimo vse naštete vrednosti, vendar je odsvetovan, ker potem nikoli ne vemo, kaj vse smo uvozili.

## Preprečevanje napak

V programih lahko naredimo tri glavne vrste napak

### Sintaktične napake

Pri teh napakah program napišemo drugače, kot določajo pravila. Na primer, če argumente funkcije ločimo s podpičjem namesto z vejico, ali pa če narobe pišemo oklepaje:

```{code-cell}
:tags: ["raises-exception"]
max(2; 4)
```

```{code-cell}
:tags: ["raises-exception"]
max(2, 4))
```

Na take napake nas Python opozori, še preden začne z izvajanjem programa, zato jih ne moremo zgrešiti.

### Napake ob izvajanju

Pri teh napakah program napišemo sintaktično pravilno, vendar ga Python ne zna ali ne more izvesti:

```{code-cell}
:tags: ["raises-exception"]
1 / 0
```

```{code-cell}
:tags: ["raises-exception"]
mix(2, 4)
```

Opozorila o napakah si bomo še ogledali bolj podrobno, zaenkrat pa si zapomnimo le, da je ključna informacija o napaki v zadnji vrstici opozorila. V prvem primeru je bila napaka deljenje z 0, v drugem pa to, da ime `mix` ni definirano.

Na precej takih napak (npr. na to, da uporabimo nedefinirano ime) nas bo opozoril že urejevalnik, lahko pa se zgodi, da se bodo pojavile šele ob izvajanju. Pri Uvodu v programiranje to običajno ne bo težava, v praksi pa zna biti precej nerodno, sploh kadar gre za kritično pomemben program (npr. za nadzor jedrskega reaktorja) ali pa kadar s tem izgubimo veliko dela (recimo, da se računalnik po 10-urnem izračunu ustavi, preden izpiše rezultat). Lahko se tudi zgodi, da do napak pride šele ob kakšnih robnih pogojih, zato jih lahko precej časa sploh ne opazimo. Vseeno pa je njihova prednost vsaj ta, da jih opazimo, kadar se zgodijo (kot bomo videli, jih lahko včasih tudi naknadno rešimo).

### Vsebinske napake

Pri vsebinskih napakah je vse videti v redu, vendar je koncu dobimo napačen odgovor, ker smo podali napačna navodila. Recimo, da želimo izračunati razdaljo med točkama (2, 3) in (5, 7):

```{code-block}
((2 - 5) ** 2 + (3 - 7) ** 2) ** 1/2
```

Program smo napisali brez sintaktičnih napak in izvajanje je uspešno vrnilo rezultat, ki pa je žal napačen, ker nismo potencirali na 1/2, temveč potencirali na 1 in delili z 2, saj ima potenciranje prednost pred deljenjem. Take napake so še posebej zlobne, ker jih lahko precej dolgo časa ne opazimo. Znan primer te napake je [Mars Climate Orbiter](https://en.wikipedia.org/wiki/Mars_Climate_Orbiter), ki je po devetih mesecih potovanja proti Marsu prehitro vstopil v atmosfero in razpadel. Vzrok je bil v tem, da je del kode delal s SI merskimi enotami, del kode pa z imperialnimi. Škode je bilo za 300 milijonov dolarjev.

Na vsebinske napake nas računalnik ne more opozoriti, saj nam ne zna brati misli. Izognemo se jim lahko tako, da programe pišemo strukturirano iz manjših delov, ki jih sproti preverjamo. Ključno pa je, da jih pišemo berljivo:

- Na vsaki strani dvomestne operacije (`=`, `+`, `**`, ...) pišemo presledek (tako bi hitreje prepoznali, da `** 1/2` v resnici pomeni `** 1 / 2`).
- Za ločili (na primer `,`) pišemo presledek, pred njimi pa ne.
- Spremenljivkam dajemo opisna imena, ki jih pišemo z malimi črkami. Posamezne besede ločimo z znakom `_`.

Na primer, računalnik bi razumel tudi sledeči izračun števila učiteljev matematike:

```{code-cell}
s,z=2000000,75
g=s/z
o=9*g
r=o/25
m=4.5*r
u=m/20
u
```

ali celo:

```{code-cell}
s,z=2000000,75;g=s/z;o=9*g;r=o/25;m=4.5*r;u=m/20;u
```

a pri takem pisanju se nam bo hitro pojavila napaka.

## Definicije funkcij

Kako bi izračunali ploščino trikotnika s stranicami dolžin 4, 13 in 15? Pomagamo si lahko s Heronovo formulo

$$\sqrt{s (s - a) (s - b) (s - c)}$$

kjer je $s = (a + b + c) / 2$. Tako bi lahko napisali:

```{code-cell}
a, b, c = 4, 13, 15
s = (a + b + c) / 2
ploscina = math.sqrt(s * (s - a) * (s - b) * (s - c))
ploscina
```

Kako pa bi izračunali površino tetraedra pa bi izračunali površino tetraedra, ki ima za lica štiri trikotnike? Načeloma bi lahko pisali:

```{code-cell}
a, b, c, d, e, f = 896, 1073, 1073, 990, 1073, 1073
s_abc = (a + b + c) / 2
p_abc = math.sqrt(s_abc * (s_abc - a) * (s_abc - b) * (s_abc - c))
s_aef = (a + e + f) / 2
p_aef = math.sqrt(s_aef * (s_aef - a) * (s_aef - e) * (s_aef - f))
s_cde = (c + d + e) / 2
p_cde = math.sqrt(s_cde * (s_cde - c) * (s_cde - d) * (s_cde - f))
s_bdf = (b + d + f) / 2
p_bdf = math.sqrt(s_bdf * (s_bdf - b) * (s_bdf - d) * (s_bdf - f))
povrsina = p_abc + p_aef + p_bdf + p_cde
povrsina
```

Kot vidimo, to ni najbolj pregledno. V taki kodi z veliko verjetnostjo naredimo kakšno napako. Bolje je, da uporabimo funkcije. Že prej smo uporabili nekaj vgrajenih funkcij, Python pa nam omogoča, da si funkcije definiramo tudi sami. Na primer, definicija funkcije za izračun ploščine trikotnika je sledeča:

```{code-cell}
def ploscina_trikotnika(a, b, c):
    """Vrne ploščino trikotnika z danimi stranicami."""
    s = (a + b + c) / 2
    ploscina = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return ploscina
```

Oglejmo si njene sestavne dele. Vsaka definicija funkcije se začne s ključno besedo `def`, ki ji sledi ime funkcije, v našem primeru `ploscina_trikotnika`, tej pa v oklepajih našteti argumenti, ki jih funkcija sprejme. Funkcije lahko sprejmejo različno število argumentov. Naša sprejme tri argumente, ki jih bomo shranili v spremenljivke `a`, `b` in `c`. Za dvopičjem sledi glavni del: _telo funkcije_, torej ukazi, ki naj se izvedejo, ko funkcijo pokličemo. Telo moramo zamakniti za štiri presledke, da se jasno vidi, kaj vse obsega.

V prvo vrstico telesa lahko zapišemo neobvezni _dokumentacijski niz_ oziroma _docstring_, v katerem na kratko opišemo, kaj funkcija počne. Dokumentacijski niz ni obvezen, je pa koristen, saj uporabniku prek ustrezne podpore v urejevalniku ali funkcije `help` pove, kaj funkcija počne. Drugo in tretjo vrstico telesa smo že videli, v zadnji pa z ukazom `return` povemo, katero vrednost naj vrne funkcija. Tako definirano funkcijo potem kličemo na enak način kot vgrajene funkcije.

```{code-cell}
ploscina_trikotnika(4, 13, 15)
```

S pomočjo funkcije `ploscina_trikotnika` lahko tudi na veliko bolj pregleden način zapišemo funkcijo za izračun površine tetraedra:

```{code-cell}
def povrsina_tetraedra(a, b, c, d, e, f):
    p_abc = ploscina_trikotnika(a, b, c)
    p_aef = ploscina_trikotnika(a, e, f)
    p_bdf = ploscina_trikotnika(b, d, f)
    p_cde = ploscina_trikotnika(c, d, e)
    return p_abc + p_aef + p_bdf + p_cde

povrsina_tetraedra(896, 1073, 1073, 990, 1073, 1073)
```

Tako kot drugje v Pythonu, se tudi stavki v telesu funkcije izvajajo od prvega proti zadnjemu. Ko dosežemo stavek `return`, funkcija vrne vrednost danega izraza ter zaključi z izvajanjem. Tako tudi funkcija

```{code-cell}
def f(x):
    return x ** 2
    return 1000
```

vrne kvadrat števila `x` in ne števila 1000, saj se izvajanje ustavi ob prvem stavku `return`, zato do drugega sploh ne pride.

```{code-cell}
f(10)
```

Če stavka `return` ne napišemo, funkcija vrne posebno vrednost `None`, ki označuje manjkajočo vrednost. Pozorno se ji bomo posvetili kasneje, zaenkrat pa jo omenimo le zato, da bomo znali razumeti spodnjo (precej pogosto) napako:

```{code-cell}
:tags: ["raises-exception"]
def g(x):
    x ** 2

2 * g(10)
```

Pričakovali bi, da bo rezultat klica `2 * g(10)` enak 200\. Toda ker smo v funkciji `g` pozabili na `return`, je funkcija vrnila vrednost `None`. To lahko razberemo iz opozorila, v katerem približno piše, da operacije `*` ne moremo uporabiti na celem številu in vrednosti `None`. Vsakič, ko dobite opozorilo `TypeError`, v katerem se pojavlja `NoneType`, posumite na to, da nekje manjka stavek `return`.

Argumenti funkcije in spremenljivke, ki jih definiramo v telesu funkcije, se izven funkcije ne vidijo. Pravimo, da so _lokalne_. Namen tega je, da funkcije ne motijo ena druge s spremenljivkami, ki jih uporabljajo. Na primer, če definiramo

```{code-cell}
def f(x):
    y = 3 * x
    return y
```

tedaj tudi po klicu funkcije `f` ne `x` ne `y` ne bosta definirana:

```
f(4)
```

```{code-cell}
:tags: ["raises-exception"]
x
```

```{code-cell}
:tags: ["raises-exception"]
y
```

Če pa je `y` na primer že definiran drugje, pa ga klic funkcije `f` ne zmoti:

```{code-cell}
y = 10
f(4)
```

```{code-cell}
y
```

Včasih imamo za nekatere argumente funkcij v mislih že prav določeno vrednost. Na primer, za izračun logaritma potrebujemo dve števili: osnovo in argument (tudi logaritmand). Toda velikokrat za osnovo vzamemo $10$, zato namesto $\log_{10} x$ pišemo kar $\log x$. V Pythonu lahko neobvezne argumente določimo tako, da jim podamo privzeto vrednost:

```{code-cell}
def koren(x, n=2):
    return x ** (1 / n)
```

Pozor, okoli enačajev pri neobveznih argumentih **ne pišemo presledkov**. Na podoben način take funkcije tudi kličemo:

```{code-cell}
koren(64, n=3)
```

V primeru, da drugega argumenta ne podamo, bi Python uporabil privzeto vrednost:

```{code-cell}
koren(64)
```

## Logične vrednosti

Poleg števil Python pozna tudi logični vrednosti `True` in `False`, ki označujeta resnico in neresnico. Logične vrednosti ponavadi dobimo kot rezultat primerjav, kot so enakost `==`, neenakost `!=` ali urejenostne relacije `<`, `>`, `<=`, `>=`, ter prek logičnih operacij `and`, `or` in `not`.

```{code-cell}
1 + 1 == 3
```

```{code-cell}
3 != 2
```

```{code-cell}
True and False
```

```{code-cell}
not (5 == 10)
```

```{code-cell}
3 < 5 or 10 > 20
```

Logične vrednosti uporabimo v _pogojnih stavkih_ (oziroma _stavkih_ `if`) oblike

```
if pogoj:
    # stavki, ki jih izvedemo,
    # ko pogoj drži
else:
    # stavki, ki jih izvedemo,
    # ko pogoj ne drži
```

Ključnima besedama `if`/`else` in pripadajočim stavkom pravimo tudi _veji pogojnega stavka_. Stavke v obeh vejah moramo zamakniti za štiri presledke tako kot v funkcijah.

Na primer, če izvedemo program

```{code-cell}
x = 5
if x < 10:
    y = 2 * x
else:
    y = 3 * x - 1
x = y + 7
```

se bo izvedla veja `if`, zato bo `x` na koncu enak 17, `y` pa 10\. V primeru, da bi bila začetna vrednost `x = 12`, pa bi se izvedla veja `else` in vrednost `x` bi na koncu bila 42, vrednost `y` pa 35.

Pogojne stavke lahko pišemo tudi v funkcijah. Na primer, funkcijo, ki računa absolutno vrednost, lahko s pomočjo pogojnega stavka napišemo kot:

```{code-cell}
def absolutna_vrednost(x):
    if x >= 0:
        return x
    else:
        return -x
```

```{code-cell}
absolutna_vrednost(-5)
```

```{code-cell}
absolutna_vrednost(3)
```

Če bi želeli vrniti predznak števila, pa moramo ločiti tri primere: negativno število, nič in pozitivno število. To lahko storimo kot:

```{code-cell}
def predznak(x):
    if x < 0:
        return -1
    else:
        if x == 0:
            return 0
        else:
            return 1
```

Zgornji pogojni stavek je malo nerodno zapisan. Ker se nam bo dostikrat zgodilo, da se ne bomo odločali le med dvema primeroma, temveč med večimi, nam Python omogoča splošnejše pogojne stavke oblike:

```
if pogoj1:
    # stavki, ki jih izvedemo,
    # ko pogoj1 drži
elif pogoj2:
    # stavki, ki jih izvedemo,
    # ko pogoj1 ne drži, ampak drži pogoj2
elif pogoj3:
    # stavki, ki jih izvedemo,
    # ko tudi pogoj2 ne drži, ampak drži pogoj3
else:
    # stavki, ki jih izvedemo,
    # ko noben od pogojev ne drži
```

Beseda `elif` je okrajšava za `else`-`if`. Funkcijo za izračun predznaka bi lepše zapisali kot

```
def predznak(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1
```

## Izrazi & stavki

V Pythonovih programih ločimo med _izrazi_ in _stavki_. Izrazi so vse, kar sestavimo iz funkcij in operacij ter uporabljamo kot argumente funkcij, desne strani prireditvenih izrazov ali pogoje v pogojnih stavkih. Stavki pa so osnovni gradniki Pythonovih programov in jih pišemo enega pod drugim. Zaenkrat smo videli tri vrste stavkov: prva so bili prireditveni stavki, drugi pogojni stavki (ki so potem spet sestavljeni iz gnezdenih stavkov), tretja in najmanj opazna pa so bili izrazi. Običajne izraze lahko prav tako pišemo v programe, vendar ne bodo imeli posebnega učinka. Če napišemo

```
x = 10
10 + 10
y = 20
```

se bo vsota `10 + 10` res izračunala, vendar se ne bo nikamor shranila in Python bo na njo hitro pozabil. Kmalu pa bomo srečali tudi izraze, ki bodo imeli vpliv na nadaljnje izvajanje programov.

Python poleg pogojnih stavkov podpira tudi pogojne izraze, s katerimi nekatere stvari napišemo malo elegantneje. Na primer, zgornjo določitev osnovnih točk bi lahko pisali kot:

```
def absolutna_vrednost(x):
    return x if x >= 0 else -x
```

V pogojnih izrazih moramo vedno napisati obe možnosti, prav tako pa ne moremo uporabiti `elif`-a. Načeloma lahko pogojne izraze verižimo kot:

```
def predznak(x):
    return -1 if x < 0 else 0 if x == 0 else 1
```

samo to je preveč natlačeno, da bi bilo berljivo. Pogojni stavki so torej precej omejeni, ampak vseeno jih omenjamo, ker znajo včasih kakšno stvar narediti preglednejšo.

## Rekurzivne definicije

Videli smo, da probleme rešujemo s prevajanjem na manjše, dokler ne pridemo do čisto osnovnih. Na primer, površino tetraedra izračunamo iz ploščin trikotnikov, te pa lahko prevedemo na vgrajene aritmetične operacije.

Dostikrat pa bodo manjši problemi iste oblike kot prvotni problem. Poglejmo, kako bi izračunali $n! = n \cdot (n - 1) \dots 3 \cdot 2 \cdot 1$. Kot vidimo velja $n! = n \cdot (n - 1)!$, zato bomo $n!$ izračunali tako, da bomo $n$ pomnožili z $(n - 1)!$. Toda od kod bomo dobili tega? Preprosto, $n - 1$ bomo pomnožili z $(n - 2)!$. Od kod pa tega? Ja iz $(n - 3)!$. In tako naprej vse do $2!$, ki ga bomo dobili iz $1!$, tega pa iz $0!$, ki je po definiciji enak $1$. Torej lahko funkcijo, ki računa fakulteto, napišemo tako, da najprej pogleda svoj argument `n`. Če je enak 1, vrne 1, sicer pa `n` pomnožimo z rezultatom klica `fakulteta(n - 1)`:

```{code-cell}
def fakulteta(n):
    if n <= 1:
        return 1
    else:
        return n * fakulteta(n - 1)
```

ali s pogojnim izrazom kot:

```{code-cell}
def fakulteta(n):
    return 1 if n == 0 else n * fakulteta(n - 1)
```

```{code-cell}
fakulteta(1)
```

```{code-cell}
fakulteta(5)
```

```{code-cell}
fakulteta(10)
```

Funkcijam, ki so definirane s pomočjo same sebe pravimo, da so **rekurzivne**. Izkaže se, da lahko s pomočjo rekurzije napišemo **čisto vse** izračunljive funkcije na celih številih: ugotovimo lahko, katera števila so praštevila, katera so si prijateljska, katera so popolna, ...

Še en primer rekurzivne definicije so Fibonaccijeva števila. Velja $F_0 = 0$, $F_1 = 1$, za vse $n \ge 2$ pa velja in $F_{n} = F_{n - 1} + F_{n - 2}$. Funkcijo tedaj napišemo podobno na podoben način kot zgornjo: če je `n` enak 0, vrnemo 0, sicer pogledamo, ali je enak 1\. V tem primeru vrnemo 1\. Če pa tudi 1 ni enak, mora biti večji ali enak 2, zato se pokličemo rekurzivno.

```{code-cell}
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

```{code-cell}
fibonacci(3)
```

```{code-cell}
fibonacci(4)
```

```{code-cell}
fibonacci(5)
```

```{code-cell}
fibonacci(20)
```

Kaj se zgodi, če poskušate izračunati `fibonacci(35)`? Po nekaj časa res dobite pravilen odgovor 9227465, vendar to kaže, da nekaj ni v redu. Težava je, da se pri `fibonacci(35)` funkcija pokliče dvakrat: enkrat na 34 in enkrat na 33\. Tudi vsak od teh dveh klicov povzroči dva nadaljnja klica in tako naprej, vse dokler ne pridemo do 0 ali 1\. Bolje bi bilo, če bi jo zastavili malo drugače.

Poleg Fibonaccijevega zaporedja, ki se začne s številoma 0 in 1, obstaja tudi splošno Fibonaccijevo zaporedje, ki se začne s poljubnima členoma $a$ in $b$:

$$a, b, a + b, b + (a + b) = a + 2 b, (a + b) + (a + 2 b) = 2 a + 3 b, \ldots$$

Vidimo, da je $n$. člen tega zaporedja ravno $n - 1$. člen zaporedja, ki se začne s členoma $b$ in $a + b$. Tedaj lahko definiramo:

```{code-cell}
def splosni_fibonacci(n, a=0, b=1):
    """Vrne n-ti člen zaporedja a, b, a + b, a + 2 b, …"""
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return splosni_fibonacci(n - 1, b, a + b)
```

Kot lahko sami preizkusimo, ta funkcija deluje veliko hitreje od prejšnje:

```{code-cell}
splosni_fibonacci(35, 0, 1)
```

```{code-cell}
splosni_fibonacci(35, 0, 10)
```

Pomembno ni torej samo to, da naš program pravilno izračuna iskani rezultat, temveč tudi to, kako učinkovito ga izračuna.

Ker smo argumentoma `a` in `b` v definiciji podali privzeti vrednosti, nam jih pri klicu ni treba podati:

```{code-cell}
splosni_fibonacci(35)
```
