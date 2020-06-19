# Uvod v Python

## Zgodovina Pythona

.center[![](https://upload.wikimedia.org/wikipedia/commons/f/f8/Python_logo_and_wordmark.svg)]

- 1991: Guido van Rossum (~~BDFL~~) objavi Python 0.9
- 2000: Python 2.0
- 2008: Python 3.0
- 2010: Python 2.7
- ~~2015: predvideni konec podpore za Python 2.7~~
- 2019: Python 3.8
- 2020: konec podpore za Python 2.7

## Kako uporabljamo Python

S Pythonom se najenostavneje pogovarjamo prek interaktivne konzole, do katere lahko dostopamo na več načinov: neposredno iz ukazne vrstice, z uporabo enostavnega okolja IDLE, ki je priloženo vsaki namestitvi Pythona, ali pa prek kakšnega od naprednejših razvijalskih okolij, na primer PyCharm. Za navodila, kako to storimo, si oglejte video [Namestitev Pythona pod Windowsi](https://vimeo.com/156327496).

V vseh primerih nas pozdravi približno tak izpis:

```
Python 3.7.3 (default, Nov 15 2019, 04:04:52) 
[Clang 11.0.0 (clang-1100.0.33.16)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Na začetku natančno piše, katero različico Pythona uporabljamo, temu pa sledi nekaj kazalcev na osnovne informacije. Mi se bomo osredotočili na zadnjo vrstico, v kateri nam poziv `>>>` kaže, da je Python pripravljen na naš vnos.

```
Pozorni bodite, da v prvi vrstici piše `Python 3.x.x` (zadnji dve številki nista tako ključni). Če tam piše `Python 2.x.x`, uporabljate Python 2, starejšo, a še vedno precej razširjeno starejšo različico Pythona. Ob prehodu na Python 3 leta 2008 so razvijalci jezika naredili nekaj večjih sprememb, ki so jezik prečistile, vendar so zaradi njih nekateri programi, napisani v Pythonu 2, prenehali delovati. Razvijalci Pythona so upali, da bodo avtorji starih programov prešli na Python 3, vendar se to ni zgodilo dovolj hitro, tako da sta danes še vedno v uporabi obe različici. V tem učbeniku se bomo ukvarjali izključno s Pythonom 3.
```

Za začetek izračunajmo, koliko je 1 + 1\. Vnesemo `1 + 1` ter pritisnimo znak za novo vrstico. Ob tem Python prebere naš vnos, ga izračuna in izpiše rezultat.

```
1 + 1
```

REPL, Jupyter, datoteke

## Aritmetični izrazi

Poleg seštevanja so nam na voljo tudi ostale osnovne računske operacije: `-` za odštevanje, `*` za množenje in `**` za potenciranje. Za deljenje Python pozna dve operaciji: običajno deljenje `/` in pa celoštevilsko deljenje `//`, ki zavrže morebitni ostanek. Če želimo izračunati samo ostanek, uporabimo `%`. Prioriteta operatorjev je določena tako kot običajno: najtesneje veže potenciranje, nato množenje in deljenji, nazadnje pa seštevanje in odštevanje. Če želimo vrstni red spremeniti, uporabimo običajne oklepaje. Še to: da je koda bolj berljiva, damo na vsaki strani operatorja po en presledek.

```
(1 + 5) ** (9 - 2)
```

```
123 / 10
```

```
123 // 10
```

```
123 % 10
```

```
123 ** (45 + 67)
```

Vidimo, da velika števila Pythonu ne povzročajo velikih težav.

Kaj je predzadnjih sto števk števila $2^{12345}$?

## Spremenljivke

Izračunane vrednosti si lahko shranimo tudi v spremenljivke, ki jih potem uporabljamo v kasnejših izračunih. Za to uporabimo _prireditveni stavek_ oblike

```
ime_spremenljivke = vrednost_ki_jo_zelimo_shraniti
```

na primer:

```
x = 3 + 3
```

```
7 * x
```

```
y = x + 8
```

```
y
```

Če želimo, lahko hkrati priredimo tudi več vrednosti:

```
x, y = 10, 15
```

```
x + y
```

```
z = y - x
```

```
z
```

Vrednost spremenljivke lahko tudi povozimo z novo vrednostjo, vendar to na preostale spremenljivke ne vpliva, saj se vedno shrani tista vrednost, ki smo jo podali v prireditvenem stavku.

```
x = 10 
y = x + 3
```

```
y
```

```
x = 25
```

```
y
```

Ko smo v `x` shranili novo vrednost, se vrednost `y` ni spremenila, saj je prireditveni stavek `y = x + 3` najprej izračunal vrednost desne strani, torej `13`, in v `y` shranil samo število.

## Shranjevanje programov v datoteke

Interaktivna konzola je uporabna za krajše programe, daljše pa raje shranimo v datoteko. S tem preprečimo, da bi izgubili vse svoje delo, pa tudi lažje popravljamo napake, saj nam ni treba vsega ponovno vnašati. Pythonove programe shranjujemo v običajne tekstovne datoteke, kar pomeni, da jih lahko odpremo s katerim koli urejevalnikom besedila, na primer _Notepad_, _Notepad++_, _Emacs_ ali _Vi_. Pythonovim datotekam običajno damo končnico `.py`. Za natančnejša navodila si oglejte video [Nalaganje programov iz datotek](https://vimeo.com/156465707).

Za primer daljšega programa si oglejmo [Fermijevo oceno](https://sl.wikipedia.org/wiki/Fermijev_problem) števila učiteljev matematike v slovenskih osnovnih šolah. Sledeče stavke vpišite v datoteko `fermi.py`:

```
stevilo_slovencev = 2000000
pricakovana_zivljenska_doba = 75
velikost_generacije = stevilo_slovencev / pricakovana_zivljenska_doba
stevilo_osnovnosolcev = 9 * velikost_generacije
stevilo_razredov = stevilo_osnovnosolcev / 25
stevilo_ur_matematike_na_teden = 4.5 * stevilo_razredov
stevilo_uciteljev_matematike = stevilo_ur_matematike_na_teden / 20
```

Ko datoteko naložimo, lahko vidimo, da bi moralo v Sloveniji biti približno 2000 učiteljev matematike:

```
stevilo_uciteljev_matematike
```

Vidimo, da lahko imena spremenljivk vsebujejo več kot eno črko, česar smo navajeni v matematiki. V programiranju je zelo pomembno, da so imena čimbolj opisna, saj tako hitreje razumemo, kaj počne program. Računalnik bi razumel tudi sledeč program in izračunal enak odgovor, vendar vidimo, da smiselna imena in presledki kodo naredijo veliko bolj berljivo.

```
s,z=2000000,75
g=s/z
o=9*g
r=o/25
m=4.5*r
u=m/20
```

```
u
```

Zato se bomo držali sledečih pravil:

- Na vsaki strani dvomestne operacije (`=`, `+`, `**`, ...) pišemo presledek.
- Za ločili (na primer `,`) pišemo presledek, pred njimi pa ne.
- Spremenljivkam dajemo opisna imena, ki jih pišemo z malimi črkami. Posamezne besede ločimo z znakom `_`.

Koliko je ploščina trikotnika s stranicami dolžin 4, 13 in 15?

Ploščino trikotnika s stranicami $a, b, c$ lahko izračunamo po Heronovi formuli

$$\sqrt{s (s - a) (s - b) (s - c)}$$

kjer je $s = (a + b + c) / 2$. Ploščino trikotnika s stranicami 4, 13 in 15 bi v Pythonu lahko torej izračunali s programom:

```
import math

a, b, c = 4, 13, 15
s = (a + b + c) / 2
ploscina = math.sqrt(s * (s - a) * (s - b) * (s - c))
```

Tedaj je

```
ploscina
```

## Napake

V programih lahko naredimo tri vrste napak

### Sintaktične napake

**Zapis je napačen** in ga Python ne razume (noče razumeti).

### Napake ob izvajanju

Zapis je pravilen, vendar ga Python **ne zna izvesti**.

### Vsebinske napake

Zapis je pravilen, Python ga izvede, vendar ima **napačna navodila**.

vrste napak, odpravljanje starih in preprečevanje novih napak

Pri teh napakah program napišemo drugače, kot določajo pravila. Na primer, če argumente funkcije ločimo s podpičjem namesto z vejico, ali pa če narobe pišemo oklepaje:

```python
max(2; 4)
```

```
...
  max(2; 4)
       ^
SyntaxError: invalid syntax
```

```python
max(2, 4))
```

```
...
  max(2, 4))
           ^
SyntaxError: invalid syntax
```

Na take napake nas Python opozori, še preden začne z izvajanjem programa, zato jih ne moremo zgrešiti.

### Napake ob izvajanju

Pri teh napakah program napišemo sintaktično pravilno, vendar uporabimo neveljavno operacijo:

```python
1 / 0
```

```
Traceback (most recent call last)
...
----> 1 1 / 0

ZeroDivisionError: division by zero
```

```python
mix(2, 4)
```

```
Traceback (most recent call last)
...
----> 1 mix(2, 4)

NameError: name 'mix' is not defined
```

Opozorila o napakah si bomo še ogledali bolj podrobno, zaenkrat pa si zapomnimo le, da je ključna informacija o napaki v zadnji vrstici opozorila. V prvem primeru je bila napaka deljenje z 0, v drugem pa to, da ime `mix` ni definirano.

Take napake se pojavijo šele ob izvajanju programa, in izvajanje tudi prekinejo. To zna biti nerodno, kadar gre za kritično pomemben program (npr. za nadzor jedrskega reaktorja) ali pa kadar s tem izgubimo veliko dela (recimo, da se računalnik po 10-urnem izračunu ustavi, preden izpiše rezultat). Lahko se tudi zgodi, da do napak pride šele ob kakšnih robnih pogojih, zato jih lahko precej časa sploh ne opazimo. Vseeno pa je njihova prednost vsaj ta, da jih opazimo, kadar se zgodijo (kot bomo videli, jih lahko včasih tudi naknadno rešimo).

### Vsebinske napake

Pri vsebinskih napakah program navidez deluje brez težav, vendar izračuna napačen odgovor, ker smo mu dali napačna navodila. Recimo, da želimo izračunati razdaljo med točkama (2, 3) in (5, 7):

```
((2 - 5) ** 2 + (3 - 7) ** 2) ** 1 / 2
```

Program smo napisali brez sintaktičnih napak in izvajanje je uspešno vrnilo rezultat, ki pa je žal napačen, ker nismo potencirali na 1/2, temveč potencirali na 1 in delili z 2, saj ima potenciranje prednost pred deljenjem. Take napake so še posebej zlobne, ker jih lahko precej dolgo časa ne opazimo. Znan primer te napake je [Mars Climate Orbiter](https://en.wikipedia.org/wiki/Mars_Climate_Orbiter), ki je po devetih mesecih potovanja proti Marsu prehitro vstopil v atmosfero in razpadel. Vzrok je bil v tem, da je del kode delal s SI merskimi enotami, del kode pa z imperialnimi. Škode je bilo za 300 milijonov dolarjev.

## Vgrajene funkcije

Na voljo so tudi osnovne funkcije, kot na primer `max` in `min` za izračun maksimuma in minimuma.

```
>>> max(3, 6)
6
>>> min(12, -5)
-5
>>> max(min(10, 20), 30 // 2)
15
```

```
max(3, 6)
```

```
min(12, -5)
```

```
max(min(10, 20), 30 // 2)
```

Matematične funkcije so na voljo v ločeni knjižnici `math`. Do njih lahko dostopamo na dva osnovna načina:

Knjižnico uvozimo s stavkom `import math`, nato pa do funkcij in konstant dostopamo tako, da dodamo `math.` pred vsako ime:

```
import math
```

```
math.sqrt(2) / 2
```

```
math.sin(math.pi / 4)
```

```
math.sin(math.pi)
```

```
V zadnjem ukazu nismo dobili pričakovanega odgovora 0\. Računalnik namreč ne dela s čisto pravimi realnimi števili, temveč z njihovimi približki, ki jim pravimo *števila s plavajočo vejico*. Za ta števila običajno najprej zapišemo decimalke (ki jim pravimo *mantisa*), nato pa še eksponent. Število, ki smo ga dobili, je tako enako približno $1{,}22 \cdot 10^{-16}$, saj `e-16` pomeni $10^{-16}$. Na primer `3.2445e2` pa označuje število $324{,}45 = 3{,}2445 \cdot 10^2$).
```

Iz knjižnice s stavkom `from math import ...` uvozimo posamezne vrednosti, nato pa do njih dostopamo direktno:

```
from math import sqrt, sin, pi
```

```
sqrt(2) / 2
```

```
sin(pi / 4)
```

Obstaja tudi tretji način, ko iz knjižnice s stavkom `from math import *` uvozimo vse naštete vrednosti, vendar je odsvetovan, ker potem nikoli ne vemo, kaj vse smo uvozili.

Včasih imamo za nekatere argumente funkcij v mislih že prav določeno vrednost. Na primer, za izračun logaritma potrebujemo dve števili: osnovo in argument (tudi logaritmand). Toda velikokrat za osnovo vzamemo $10$, zato namesto $\log_{10} x$ pišemo kar $\log x$. Tudi pri Pythonu je podobno.

```
>>> math.log(10)
3
>>> math.log(10, base=10)
1
```

Koliko je $\sin(\pi)$?

## Definicije funkcij

Koliko je površina tetraedra s stranicami dolžin 18, 21, 22, 25, 27 in 31?

Kako pa bi izračunali površino tetraedra, ki ima za lica štiri trikotnike? Načeloma bi lahko pisali:

```
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
```

Kot vidimo, to ni najbolj pregledno. V taki kodi z veliko verjetnostjo naredimo kakšno napako. Bolje je, da uporabimo funkcije. Že prej smo uporabili nekaj vgrajenih funkcij, na primer `min` in `max`. Python pa nam omogoča, da si funkcije definiramo tudi sami.

.small[![](slike/tetraeder.png)]

V Pythonu lahko **definiramo svoje funkcije**

```
def ime_funkcije(argument1, argument2):
    # stavki, s katerimi
    # izračunamo iskani rezultat
    return iskani_rezultat
```

Definicija funkcije, ki izračuna ploščino trikotnika, je sledeča:

```
import math

def ploscina_trikotnika(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))
```

Oglejmo si njene sestavne dele. Vsaka definicija funkcije se začne s ključno besedo `def`, ki ji sledi ime funkcije, v našem primeru `ploscina_trikotnika`, tej pa v oklepajih našteti argumenti, ki jih funkcija sprejme. Funkcije lahko sprejmejo različno število argumentov. Naša sprejme tri argumente, ki jih bomo shranili v spremenljivke `a`, `b` in `c`.

Nato sledi _telo funkcije_, torej ukazi, ki naj se izvedejo, ko funkcijo pokličemo. Vsako vrstico telesa funkcije moramo zamakniti za štiri presledke, da se jasno vidi, kaj vse funkcija obsega. Prvo vrstico telesa smo že videli, v drugi pa z ukazom `return` povemo, katero vrednost naj vrne funkcija. Tako definirano funkcijo potem kličemo na enak način kot vgrajene funkcije.

```
ploscina_trikotnika(4, 13, 15)
```

S pomočjo funkcije `ploscina_trikotnika` lahko tudi na veliko bolj pregleden način zapišemo funkcijo za izračun površine tetraedra:

```
def povrsina_tetraedra(a, b, c, d, e, f):
    p_abc = ploscina_trikotnika(a, b, c)
    p_aef = ploscina_trikotnika(a, e, f)
    p_bdf = ploscina_trikotnika(b, d, f)
    p_cde = ploscina_trikotnika(c, d, e)
    return p_abc + p_aef + p_bdf + p_cde
```

```
povrsina_tetraedra(896, 1073, 1073, 990, 1073, 1073)
```

Pred telesom funkcije dostikrat lahko zapišemo tudi _dokumentacijski niz_ oziroma _docstring_. Ta niz ponavadi zapišemo med trojne narekovaje, v njem pa na kratko opišemo, kaj funkcija počne. Ta vrstica ni obvezna, je pa koristna, saj lahko uporabnik, ki ne ve, kaj funkcija počne, to pogleda s pomočjo funkcije `help`.

```
import math

def ploscina_trikotnika(a, b, c):
    """Vrne ploščino trikotnika z danimi stranicami."""
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))
```

```
help(ploscina_trikotnika)
```

Argumenti funkcij so lahko **neobvezni**

Če se nam ob klicu funkcije ne ljubi navajati vrednosti vseh argumentov, lahko za nekatere od njih v prvi vrstici definicije navedemo privzeto vrednost. Na primer, pri funkciji `kvadratni_koren` ne pričakujemo, da bo uporabnik vedno znova vnašal natančnost, na katero želi izračunati koren. Če želimo, da ima `eps` privzeto vrednost `1e-15`, lahko napišemo:

Tedaj se bo vedno uporabila privzeta vrednost za tiste argumente, ki jih ne podamo izrecno.

```
def fibonacci(n, a=0, b=1):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibonacci(n - 1, b, a + b)
```

Klic deluje tudi, če neobveznih argumentov ne poimenujemo, vendar lahko to vodi do zmede, če je argumentov več, zato se takih klicev izogibamo.

```
>>> fibonacci(10, a=0, b=10)
550
>>> fibonacci(10, 0, 10)
550
>>> fibonacci(10)
55
```

Tako kot drugje v Pythonu, se tudi stavki v telesu funkcije izvajajo od prvega proti zadnjemu. Ko dosežemo stavek `return`, funkcija vrne vrednost danega izraza ter zaključi z izvajanjem. Tako tudi funkcija

```
def f(x):
    return x ** 2
    return 1000
```

vrne kvadrat števila `x` in ne števila 1000, saj se izvajanje ustavi ob prvem stavku `return`, zato do drugega sploh ne pride. Če stavka `return` ne napišemo, funkcija vrne posebno vrednost `None`, ki označuje manjkajočo vrednost. Pozorno se ji bomo posvetili kasneje, zaenkrat pa jo omenimo le zato, da bomo znali razumeti spodnjo (precej pogosto) napako:

```
def g(x):
    x ** 2
```

```python
2 * g(10)
```

```
Traceback (most recent call last):
  ...
TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
```

Pričakovali bi, da bo rezultat klica `2 * g(10)` enak 200\. Toda ker smo v funkciji `g` pozabili na `return`, je funkcija vrnila vrednost `None`. To lahko razberemo iz opozorila, v katerem približno piše, da operacije `*` ne moremo uporabiti na celem številu in vrednosti `None`. Vsakič, ko dobite opozorilo `TypeError`, v katerem se pojavlja `NoneType`, posumite na to, da nekje manjka stavek `return`.

```
def f(x):
    return x ** 2
    return 1000
```

Koliko je `f(10)`?

```
def g(x):
    x ** 2
```

Koliko je `2 * g(10)`?

```
def f(x):
    y = 3 * x
    return y
```

```
>>> y = 5
>>> f(4)
12
```

Argumenti funkcije in spremenljivke, ki jih definiramo v telesu funkcije, se izven funkcije ne vidijo. Pravimo, da so _lokalne_. Namen tega je, da funkcije ne motijo ena druge s spremenljivkami, ki jih uporabljajo. Na primer, če definiramo

```
def f(x):
    y = 3 * x
    return y
```

tedaj tudi po klicu funkcije `f` ne `x` ne `y` ne bosta definirana:

```
f(4)
```

```python
x
```

```
Traceback (most recent call last):
  ...
NameError: name 'x' is not defined
```

```python
y
```

```
Traceback (most recent call last):
  ...
NameError: name 'y' is not defined
```

Če pa je `y` na primer že definiran drugje, pa ga klic funkcije `f` ne zmoti:

```
y = 10
f(4)
```

```
y
```

Definirajmo funkcijo za izračun absolutne vrednosti

## Logične vrednosti

Poleg števil Python pozna tudi logični vrednosti `True` in `False`, ki označujeta resnico in neresnico. Logične vrednosti ponavadi dobimo kot rezultat primerjav, kot so enakost `==`, neenakost `!=` ali urejenostne relacije `<`, `>`, `<=`, `>=`, ter prek logičnih operacij `and`, `or` in `not`.

```
>>> 1 + 1 == 3
False
>>> 3 != 2
True
>>> True and False
False
>>> not (5 == 10)
True
>>> 3 < 5 or 10 > 20
True
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

```
x = 5 if x < 10: y = 2 * x else: y = 3 * x - 1 x = y + 7
```

se bo izvedla veja `if`, zato bo `x` na koncu enak 17, `y` pa 10\. V primeru, da bi bila začetna vrednost `x = 12`, pa bi se izvedla veja `else` in vrednost `x` bi na koncu bila 42, vrednost `y` pa 35.

Pogojne stavke lahko pišemo tudi v funkcijah. Na primer, funkcijo, ki računa absolutno vrednost, lahko s pomočjo pogojnega stavka napišemo kot:

```
def absolutna_vrednost(x):

:   

    if x >= 0:

    :   return x

    else:

    :   return -x
```

```
absolutna_vrednost(-5) 5 
absolutna_vrednost(3) 3
```

Če bi želeli vrniti predznak števila, pa moramo ločiti tri primere: negativno število, nič in pozitivno število. To lahko storimo kot:

```
def predznak(x):

:   

    if x < 0:

    :   return -1

    else:

    :   

        if x == 0:

        :   return 0

        else:

        :   return 1
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

Pogojni stavek ima lahko **več vej**

```
if pogoj1:
    # stavki, ki jih izvedemo,
    # ko pogoj1 drži
elif pogoj2:
    # stavki, ki jih izvedemo,
    # ko pogoj1 ne drži, ampak drži pogoj2
elif pogoj3:
    # stavki, ki jih izvedemo,
    # ko tudi pogoj2 ne drži,
    # ampak drži pogoj3
else:
    # stavki, ki jih izvedemo,
    # ko noben od pogojev ne drži
```

Beseda `elif` je okrajšava za `else`-`if`. Funkcijo za izračun predznaka bi lepše zapisali kot

```
def predznak(x):

:   

    if x < 0:

    :   return -1

    elif x == 0:

    :   return 0

    else:

    :   return 1
```

# Izrazi & stavki

V Pythonovih programih ločimo med _izrazi_ in _stavki_. Izrazi so vse, kar sestavimo iz funkcij in operacij ter uporabljamo kot argumente funkcij, desne strani prireditvenih izrazov ali pogoje v pogojnih stavkih. Stavki pa so osnovni gradniki Pythonovih programov in jih pišemo enega pod drugim. Zaenkrat smo videli tri vrste stavkov: prva so bili prireditveni stavki, drugi pogojni stavki (ki so potem spet sestavljeni iz gnezdenih stavkov), tretja in najmanj opazna pa so bili izrazi. Običajne izraze lahko prav tako pišemo v programe, vendar ne bodo imeli posebnega učinka. Če napišemo

```
x = 10
10 + 10
y = 20
```

se bo vsota `10 + 10` res izračunala, vendar se ne bo nikamor shranila in Python bo na njo hitro pozabil. Kmalu pa bomo srečali tudi izraze, ki bodo imeli vpliv na nadaljnje izvajanje programov.

# Pogojni izraz

Python poleg pogojnih stavkov podpira tudi pogojne izraze, s katerimi nekatere stvari napišemo malo elegantneje. Na primer, zgornjo določitev osnovnih točk bi lahko pisali kot:

```
def absolutna_vrednost(x):
    return x if x >= 0 else -x
```

V pogojnih izrazih moramo vedno napisati obe možnosti, prav tako pa ne moremo uporabiti `elif`-a. Načeloma lahko pogojne izraze verižimo kot: No, načeloma bi jo lahko z

```
def predznak(x):
    return -1 if x < 0 else 0 if x == 0 else 1
```

samo to je preveč natlačeno, da bi bilo berljivo. Pogojni stavki so torej precej omejeni, ampak vseeno jih omenjamo, ker znajo včasih kakšno stvar narediti preglednejšo.

## Rekurzivne definicije

Izkaže se, da lahko s tem, kar smo spoznali v prvem poglavju, napišemo **čisto vse** izračunljive funkcije na celih številih: ugotovimo lahko, katera števila so praštevila, katera so si prijateljska, katera so popolna, ... To nam omogoča rekurzija, s katero dosežemo, da računalnik programa ne izvaja strogo od zgoraj navzdol, temveč se po potrebi tudi vrne in kakšen korak izvede večkrat. Da bomo imeli bolj pestre primere, si pred rekurzijo oglejmo še nize.

V programiranju probleme pogosto rešujemo s prevajanjem na **manjše probleme**

```
def ploscina_trikotnika(a, b, c):
    s = (a + b + c) / 2
    p2 = s * (s - a) * (s - b) * (s - c)
    return math.sqrt(p2)
```

```
def povrsina_tetraedra(a, b, c, d, e, f):
    p_abc = ploscina_trikotnika(a, b, c)
    p_aef = ploscina_trikotnika(a, e, f)
    p_bdf = ploscina_trikotnika(b, d, f)
    p_cde = ploscina_trikotnika(c, d, e)
    return p_abc + p_aef + p_bdf + p_cde
```

Manjši problemi so lahko **iste oblike** kot prvotni problem

```
def fakulteta(n):
    if n <= 1:
        return 1
    else:
        return n * fakulteta(n - 1)
```

Če funkcija kliče sebe, pravimo, da je klic **rekurziven**

Videli smo, da lahko iz funkcij kličemo tudi druge funkcije. Na primer, v funkciji `povrsina_tetraedra` smo poklicali funkcijo `ploscina_trikotnika`, v tej pa vgrajeno funkcijo `math.sqrt`. V resnici pa lahko v funkciji pokličemo tudi funkcijo samo. Takemu klicu pravimo **rekurzivni klic**. Poglejmo, kako bi izračunali $n! = n \cdot (n - 1) \dots 3 \cdot 2 \cdot 1$. Kot vidimo velja $n! = n \cdot (n - 1)!$, zato bomo $n!$ izračunali tako, da bomo $n$ pomnožili z $(n - 1)!$. Toda od kod bomo dobili tega? Preprosto, $n - 1$ bomo pomnožili z $(n - 2)!$. Od kod pa tega? Ja iz $(n - 3)!$. In tako naprej vse do $2!$, ki ga bomo dobili iz $1!$, tega pa iz $0!$, ki je po definiciji enak $1$.

Torej lahko funkcijo, ki računa fakulteto, napišemo tako, da najprej pogleda svoj argument `n`. Če je enak 1, vrne 1, sicer pa izračunamo tako, da `n` pomnožimo z rezultatom klica `fakulteta(n - 1)`:

```
def fakulteta(n):

:   

    if n <= 1:

    :   return 1

    else:

    :   return n * fakulteta(n - 1)
```

ali s pogojnim izrazom kot:

```
def fakulteta(n):

:   '''Vrne fakulteto naravnega števila n.''' return 1 if n == 0
    else n * fakulteta(n - 1)
```

```
>>> fakulteta(1) 1
>>> fakulteta(5) 120
>>> fakulteta(10)
3628800
```

Še en primer rekurzivne definicije so Fibonaccijeva števila. Velja $F_0 = 0$, $F_1 = 1$, za vse $n \ge 2$ pa velja in $F_{n} = F_{n - 1} + F_{n - 2}$. Funkcijo tedaj napišemo podobno na podoben način kot zgornjo: če je `n` enak 0, vrnemo 0, sicer pogledamo, ali je enak 1\. V tem primeru vrnemo 1\. Če pa tudi 1 ni enak, mora biti večji ali enak 2, zato se pokličemo rekurzivno.

```
def fibonacci(n):

:   

    if n == 0:

    :   return 0

    elif n == 1:

    :   return 1

    else:

    :   return fibonacci(n - 1) + fibonacci(n - 2)
```

```
>>> fibonacci(3) 2
>>> fibonacci(4) 3
>>> fibonacci(5) 5
>>>
fibonacci(20) 6765
```

Kaj se zgodi, če poskušate izračunati `fibonacci(35)`? Po nekaj časa res dobite pravilen odgovor 9227465, vendar to kaže, da nekaj ni v redu. Težava je, da se pri `fibonacci(35)` funkcija pokliče dvakrat: enkrat na 34 in enkrat na 33\. Tudi vsak od teh dveh klicov povzroči dva nadaljnja klica in tako naprej, vse dokler ne pridemo do 0 ali 1\. Bolje bi bilo, če bi jo zastavili malo drugače. Poleg Fibonaccijevega zaporedja, ki se začne s številoma 0 in 1, obstaja tudi splošno Fibonaccijevo zaporedje, ki se začne s poljubnima členoma $a$ in $b$:

$$a, b, a + b, b + (a + b) = a + 2 b, (a + b) + (a + 2 b) = 2 a + 3 b, \ldots$$

Vidimo, da je $n$. člen tega zaporedja ravno $n - 1$. člen zaporedja, ki se začne s členoma $b$ in $a + b$. Tedaj lahko definiramo:

```
def splosni_fibonacci(n, a, b):

:   

    if n == 0:

    :   return a

    elif n == 1:

    :   return b

    else:

    :   return splosni_fibonacci(n - 1, b, a + b)
```

Kot lahko sami preizkusimo, ta funkcija deluje veliko hitreje od prejšnje:

```
>>> splosni_fibonacci(35, 0, 1) 9227465
>>>
splosni_fibonacci(25, 1, -1) -28657
>>> splosni_fibonacci(25, 0, 2)
150050
>>> splosni_fibonacci(500, 0, 1)
139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125
```

Pomembno ni torej samo to, da naš program pravilno izračuna iskani rezultat, temveč tudi to, kako učinkovito ga izračuna.

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

Algoritem je zaporedje korakov, s katerimi dobimo iskani rezultat. Načeloma lahko pod besedo algoritem razumemo tudi zaporedje korakov, s katerimi si skuhamo jajca (vzemi posodo; odpri pipo; postavi posodo pod pipo; ko je posoda dovolj polna, zapri pipo; ...), ampak mi si jo bomo prihranili za postopke, s katerimi izračunamo želene vrednosti.

Za prvi algoritem se spodobi, da si pogledamo najstarejši znani algoritem in sicer Evklidov algoritem za iskanje navečjega skupnega delitelja dveh števil. Naj bo $d$ največji skupni delitelj števil $m$ in $n$. Pišimo $m = k \cdot n + o$, kjer je $0 \le o < n$. Torej: $o$ je ostanek pri deljenju števila $m$ z $n$. Ker e $d$ deli $n$, deli tudi $k \cdot n$. Poleg tega $d$ deli tudi $m$, zato deli tudi $o = m - k \cdot n$. Velja tudi obratno, če $d$ deli $n$ in $o$, potem deli tudi $m = k \cdot n + o$.

Zato lahko iskanje največjega skupnega delitelja števil $m$ in $n$ prevedemo na iskanje največjega skupnega delitelja števil $n$ in $o$. Videti je, kot da se vrtimo v krogu, vendar se ne. Poglejmo, kaj se zgodi:

1. Največji skupni delitelj števil $456$ in $123$ je enak največjemu skupnemu delitelju števil $123$ in $456 - 3 \cdot 123 = 87$.
2. Največji skupni delitelj števil $123$ in $87$ je enak največjemu skupnemu delitelju števil $87$ in $123 - 1 \cdot 87 = 36$.
3. Največji skupni delitelj števil $87$ in $36$ je enak največjemu skupnemu delitelju števil $36$ in $123 - 2 \cdot 36 = 15$.
4. Največji skupni delitelj števil $36$ in $15$ je enak največjemu skupnemu delitelju števil $15$ in $36 - 2 \cdot 15 = 6$.
5. Največji skupni delitelj števil $15$ in $6$ je enak največjemu skupnemu delitelju števil $6$ in $15 - 2 \cdot 6 = 3$.
6. Največji skupni delitelj števil $6$ in $3$ je enak največjemu skupnemu delitelju števil $3$ in $6 - 2 \cdot 3 = 0$.

Postopka ne moremo več nadaljevati, ker ne moremo deliti z nič. Kaj pa je največji skupni delitelj števil 3 in 0? Ja, 3 vendar. Torej, ko je drugo število enako 0, je prvo število ravno njun največji skupni delitelj, po vseh prejšnjih sklepih pa tudi največji skupni delitelj vseh prejšnjih parov vključno s prvim.

Evklidov algoritem je torej sledeč: če je $n = 0$, potem je največji skupni delitelj števil $m$ in $n$ enak kar $m$, sicer pa je enak največjemu skupnemu delitelju števil $n$ in $o$, kjer je $o$ ostanek pri deljenju $m$ z $n$. Ta postopek enostavno prevedemo v Python:

```
def gcd(m, n):

:   

    if n == 0:

    :   return m

    else:

    :   return gcd(n, m % n)
```

ali s pogojnim izrazom kot

```
def gcd(m, n):

:   '''Vrne največji skupni delitelj števil m in n.''' return m if
    n == 0 else gcd(n, m % n)
```

Pri tem je `gcd` (_greatest common divisor_) običajna oznaka za največjega skupnega delitelja.

`{code-cell}

> > > gcd(456, 123) 3`

Algoritem deluje tudi, kadar je $n < m$, saj je v tem primeru $n = 0 \cdot m + n$, zato v naslednjem koraku njuni mesti zamenjamo in nadaljujemo kot prej.
