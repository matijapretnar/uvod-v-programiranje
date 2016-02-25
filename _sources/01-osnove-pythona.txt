Osnove Pythona
==============


Interaktivna konzola
--------------------

S Pythonom se najenostavneje pogovarjamo prek interaktivne konzole, do katere
lahko dostopamo na več načinov: neposredno iz ukazne vrstice, z uporabo
enostavnega okolja IDLE, ki je priloženo vsaki namestitvi Pythona, ali pa prek
kakšnega od naprednejših razvijalskih okolij, na primer PyCharm. Za navodila,
kako to storimo, si oglejte video `Namestitev Pythona pod Windowsi`__.

__ https://vimeo.com/156327496

V vseh primerih nas pozdravi približno tak izpis:

.. code::

    Python 3.5.1 (default, Jan 22 2016, 08:54:32) 
    [GCC 4.2.1 Compatible Apple LLVM 7.0.2 (clang-700.1.81)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

Na začetku natančno piše, katero različico Pythona uporabljamo, temu pa sledi
nekaj kazalcev na osnovne informacije. Mi se bomo osredotočili na zadnjo
vrstico, v kateri nam poziv ``>>>`` kaže, da je Python pripravljen na naš vnos.

.. caution::

    Pozorni bodite, da v prvi vrstici piše ``Python 3.x.x`` (zadnji dve številki
    nista tako ključni). Če tam piše ``Python 2.x.x``, uporabljate Python 2,
    starejšo, a še vedno precej razširjeno starejšo različico Pythona. Ob
    prehodu na Python 3 so razvijalci jezika naredili nekaj večjih sprememb, ki
    so jezik prečistile, vendar so zaradi njih nekateri programi, napisani v
    Pythonu 2, prenehali delovati. Razvijalci Pythona so upali, da bodo avtorji
    starih programov prešli na Python 3, vendar se to ni zgodilo dovolj hitro,
    tako da sta danes še vedno v uporabi obe različici. V tem učbeniku se bomo
    ukvarjali izključno s Pythonom 3.

Za začetek izračunajmo, koliko je 1 + 1. Vnesemo ``1 + 1`` ter
pritisnimo znak za novo vrstico. Ob tem Python prebere naš vnos, ga izračuna in
izpiše rezultat.


.. doctest::

    >>> 1 + 1
    2


Števila in aritmetične operacije
--------------------------------

Poleg seštevanja so nam na voljo tudi ostale osnovne računske operacije: ``-``
za odštevanje, ``*`` za množenje in ``**`` za potenciranje. Za deljenje Python
pozna dve operaciji: običajno deljenje ``/`` in pa celoštevilsko deljenje
``//``, ki zavrže morebitni ostanek. Če želimo izračunati samo ostanek,
uporabimo ``%``. Prioriteta operatorjev je določena tako kot običajno:
najtesneje veže potenciranje, nato množenje in deljenja, nazadnje pa seštevanje
in odštevanje. Če želimo vrstni red spremeniti, uporabimo običajne oklepaje. Še
to: da je koda bolj berljiva, damo na vsaki strani operatorja po en presledek.

.. doctest::

    >>> (1 + 5) * (9 - 2)
    42
    >>> 123 / 10
    12.3
    >>> 123 // 10
    12
    >>> 123 % 10
    3
    >>> 123 ** (45 + 67)
    1173201153236117392747457141184065170953567764283837482787268119007036898684512512556572577156186549602764788041495818311329933349581701014867937205332087819177539156963702612817234021747525564287508352993790061063457990401206082438721

Vidimo, da velika števila Pythonu ne povzročajo velikih težav. Na voljo so tudi
osnovne funkcije, kot na primer ``max`` in ``min`` za izračun maksimuma in
minimuma.

.. doctest::

    >>> max(3, 6)
    6
    >>> min(12, -5)
    -5
    >>> max(min(10, 20), 30 // 2)
    15

Matematične funkcije so na voljo v knjižnici `math`. Do njih lahko dostopamo
na dva osnovna načina:

1. Knjižnico uvozimo s stavkom ``import math``, nato pa do funkcij in konstant
   dostopamo tako, da dodamo ``math.`` pred vsako ime:

   .. doctest::

       >>> import math
       >>> math.sqrt(2) / 2
       0.7071067811865476
       >>> math.sin(math.pi / 4)
       0.7071067811865475

2. Iz knjižnice s stavkom ``from math import ...`` uvozimo posamezne vrednosti,
   nato pa do njih dostopamo direktno:

       >>> from math import sqrt, sin, pi
       >>> sqrt(2) / 2
       0.7071067811865476
       >>> sin(pi / 4)
       0.7071067811865475

Obstaja tudi tretji način, ko iz knjižnice s stavkom ``from math import *``
uvozimo vse naštete vrednosti, vendar ga ne priporočam, ker potem nikoli ne
veste, kaj vse ste uvozili.


Prirejanje vrednosti spremenljivkam
-----------------------------------

Izračunane vrednosti si lahko shranimo tudi v spremenljivke, ki jih potem
uporabljamo v kasnejših izračunih. Za to uporabimo *prireditveni stavek* oblike

.. code::

    ime_spremenljivke = vrednost_ki_jo_zelimo_shraniti

na primer:

.. doctest::

    >>> x = 3 + 3
    >>> 7 * x
    42
    >>> y = x + 8
    >>> y
    14

Če želimo, lahko hkrati priredimo tudi več vrednosti:

.. doctest::

    >>> x, y = 10, 15
    >>> x + y
    25
    >>> z = y - x
    >>> z
    5

Vrednost spremenljivke lahko tudi povozimo z novo vrednostjo:

.. doctest::

    >>> x = 10
    >>> x
    10
    >>> x = 25
    >>> x
    25
    >>> x = x + 5
    >>> x
    30

Kot vidimo, lahko novo vrednost spremenljivke ``x`` izračunamo iz stare
vrednosti. V programih bomo to dostikrat izkoristili. Na primer, ko bomo
prešteli vsa praštevila med 1 in 1000000, bomo imeli spremenljivko, ki bo imela
na začetku vrednost 0, nato pa jo bomo ob vsakem praštevilu povečali za 1. V ta
namen lahko uporabimo tudi operator ``+=``, ki spremenljivko na levi poveča za
vrednost na desni. Namesto ``x = x + 5`` bi lahko pisali tudi ``x += 5``. Tudi
za ostale operatorje obstajajo podobne bližnjice, na primer ``-=``, ``*=``,
``//=`` in tako naprej.

Vrstni red izvajanja ukazov je pomemben. Če bi enake stavke izvedli v drugačnem
vrstnem redu, bi bile tudi vrednosti drugačne:

    >>> x = 10
    >>> x
    10
    >>> x = x + 5
    >>> x
    15
    >>> x = 25
    >>> x
    25

Lahko se celo zgodi, da program ne bi deloval. Recimo, da poskusimo izvesti ``x
= x + 5`` še preden priredimo ``x = 10``.

.. testcode::
    :hide:
    
    del x

.. doctest::

    >>> x = x + 5
    Traceback (most recent call last):
      File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/doctest.py", line 1320, in __run
        compileflags, 1), test.globs)
      File "<doctest default[0]>", line 1, in <module>
        x = x + 5
    NameError: name 'x' is not defined
    >>> x
    Traceback (most recent call last):
      File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/doctest.py", line 1320, in __run
        compileflags, 1), test.globs)
      File "<doctest default[0]>", line 1, in <module>
        x
    NameError: name 'x' is not defined

Opozorila o napakah si bomo še ogledali bolj podrobno, zaenkrat pa si zapomnimo
le, da je ključna informacija o napaki v zadnji vrstici opozorila. V našem
primeru Python javi dve napaki. Najprej se pritoži ob izvajanju stavka ``x = x +
5``, saj spremenljivka ``x``, ki jo potrebuje za izračun vrednosti ``x + 5``, ni
definirana. Drugo napako pa javi ob izvajanju ``x``, saj kljub prireditvenemu
stavku v prejšnji vrstici ``x`` še vedno ni definiran, ker se ta stavek ni
uspešno izvedel.

Shranjevanje programov v datoteke
---------------------------------

Interaktivna konzola je uporabna za krajše programe, daljše pa raje shranimo v
datoteko. S tem preprečimo, da izgubili vse svoje delo, pa tudi lažje
popravljamo napake, saj nam ni treba vsega ponovno vnašati. Pythonove programe
shranjujemo v običajne tekstovne datoteke, kar pomeni, da jih lahko odpremo s
katerim koli urejevalnikom besedila, na primer *Notepad*, *Notepad++*, *Emacs*
ali *Vi*. Pythonovim datotekam običajno damo končnico ``.py``. Za natančnejša
navodila si oglejte video `Nalaganje programov iz datotek`__.

__ https://vimeo.com/156465707

Za primer daljšega programa si oglejmo `Fermijevo oceno`__ števila učiteljev
matematike v slovenskih osnovnih šolah. Sledeče stavke vpišite v datoteko
``fermi.py``:

.. testcode::

    stevilo_slovencev = 2000000
    pricakovana_zivljenska_doba = 75
    velikost_generacije = stevilo_slovencev / pricakovana_zivljenska_doba
    stevilo_osnovnosolcev = 9 * velikost_generacije
    stevilo_razredov = stevilo_osnovnosolcev / 25
    stevilo_ur_matematike_na_teden = 4.5 * stevilo_razredov
    stevilo_uciteljev_matematike = stevilo_ur_matematike_na_teden / 20

__ https://sl.wikipedia.org/wiki/Fermijev_problem

Ko datoteko naložimo, lahko vidimo, da bi moralo v Sloveniji biti približno 2000
učiteljev matematike:

.. doctest::

    >>> stevilo_uciteljev_matematike
    2160.0

Vidimo, da lahko imena spremenljivk vsebujejo več kot eno črko, česar smo
navajeni v matematiki. V programiranju je zelo pomembno, da so imena čimbolj
opisna, saj tako hitreje razumemo, kaj počne program. V Pythonu imena
spremenljivk pišemo z malimi črkami, posamezne besede pa ločimo z znakom ``_``.

Računalnik bi razumel tudi sledeč program in izračunal enak odgovor, vendar
vidimo, da smiselna imena in presledki kodo naredijo veliko bolj berljivo.

.. testcode::

    s,z=2000000,75
    g=s/z
    o=9*g
    r=o/25
    m=4.5*r
    u=m/20

.. doctest::

    >>> u
    2160.0


Logične vrednosti
-----------------

Poleg števil Python pozna tudi logični vrednosti ``True`` in ``False``, ki
označujeta resnico in neresnico. Logične vrednosti ponavadi dobimo kot rezultat
primerjav, kot so enakost ``==``, neenakost ``!=`` ali urejenostne relacije
``<``, ``>``, ``<=``, ``>=``, ter prek logičnih operacij ``and``, ``or`` in
``not``.

.. doctest::

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

Logične vrednosti uporabimo v *pogojnih stavkih* (oziroma ``if``-stavkih) oblike

.. code::

    if pogoj:
        stavki_ki_jih_izvedemo
        ko_pogoj_drzi
    else:
        stavki_ki_jih_izvedemo
        ko_pogoj_ne_drzi

Ključnima besedama ``if``/``else`` in pripadajočim stavkom pravimo tudi *veje
pogojnega stavka*. Stavke v obeh vejah moramo zamakniti za štiri presledke,
da se jasno vidi, kam spadajo.

Na primer, če izvedemo program

.. testcode::

    x = 5
    if x < 10:
        x *= 2
    else:
        x = 3 * x
        x -= 1
    x += 7

se bo izvedla veja ``if``, zato bo ``x`` na koncu enak 17. V primeru, da bi bila
začetna vrednost ``x = 12``, pa bi se izvedla veja ``else`` in vrednost ``x`` bi
na koncu bila 42.

Za primer iz rezultatov smučarskega skoka, torej dolžine in ocen sodnikov,
izračunajmo skupne točke. Vsaka skakalnica ima določeno K-točko, ki določa
velikost skakalnice. Skok za dolžino v osnovi dobi 60 točk (za letalnice 120),
nato pa vsak meter nad ali pod K-točko prinese oziroma odnese 1,8 točke (za
letalnice 1,2).

Točke za slog pa dobimo tako, da seštejemo vse ocene sodnikov razen najnižje in
najvišje. To najenostavneje izračunamo tako, da seštejemo vse ocene, nato pa
odštejemo najnižjo in najvišjo, ki ju dobimo s pomočjo vgrajenih funkcij ``min``
in ``max``. Skupno oceno dobimo tako, da seštejemo točke za dolžino, točke za
slog in točke za izravnavo vetra in zaletišča.

Izračunajmo število točk zmagovalnega skoka `Petra Prevca na letalnici v
Vikersundu`__. Peter je skočil 249 metrov, vendar padel, zaradi česar je dobil
bolj slabe sodniške ocene: 15,0, 12,5, 14,0, 13,5 in 11,0. Koliko točk je dobil
za skok? Kodo napišimo tako, da bo delovala tudi v primeru, ko za K-točko,
dolžino skoka, ocene sodnikov in izravnavo vnesemo druga števila. Kot vidimo,
potrebujemo pogojni stavek, v katerem ustrezno izračunamo točke za dolžino
skoka.

__ http://medias3.fis-ski.com/pdf/2016/JP/3815/2016JP3815RL.pdf

.. testcode::

    k_tocka = 200
    dolzina = 249.0
    slog_a = 15
    slog_b = 12.5
    slog_c = 14
    slog_d = 13.5
    slog_e = 11
    izravnava = 6.4

    # če je K-točka vsaj 185 metrov, gre za letalnico
    if k_tocka < 185:
        osnovne_tocke = 60
        vrednost_metra = 1.8
    else:
        osnovne_tocke = 120
        vrednost_metra = 1.2
    tocke_dolzina = 120 + vrednost_metra * (dolzina - k_tocka)

    min_slog = min(slog_a, slog_b, slog_c, slog_d, slog_e)
    max_slog = max(slog_a, slog_b, slog_c, slog_d, slog_e)
    tocke_slog = (slog_a + slog_b + slog_c + slog_d + slog_e) - min_slog - max_slog

    skupne_tocke = tocke_dolzina + tocke_slog + izravnava

Poleg že znanih ukazov v zgornji kodi vidimo tudi *komentar*. Ko Python v kodi
vidi lojtro ``#``, preostanek vrstice ignorira. Namen komentarjev je, da po
človeško razložimo tiste dele kode, ki niso očitni. Ker so programi v Pythonu
precej razumljivi (sploh, ker uporabljamo opisna imena spremenljivk), ponavadi
ni treba pisati veliko komentarjev.

Poglejmo, koliko točk je bil vreden skok:

.. doctest::

    >>> skupne_tocke
    225.20000000000002

Skok je bil v resnici vreden natanko 225,2 točk. Vse dodatne decimalke pa so
posledica zaokrožitvenih napak. Računalnik namreč ne računa s pravimi realnimi
števili, temveč z njihovimi približki, ki jim pravimo *števila s plavajočo
vejico*.

Funkcije
--------

Ploščino trikotnika s stranicami :math:`a, b, c` lahko izračunamo po Heronovi
formuli

.. math::
    \sqrt{s (s - a) (s - b) (s - c)}

kjer je :math:`s = (a + b + c) / 2`. Ploščino trikotnika s stranicami 4, 13 in 15
bi v Pythonu lahko torej izračunali s programom:

.. testcode::

    a, b, c = 4, 13, 15
    s = (a + b + c) / 2
    ploscina = (s * (s - a) * (s - b) * (s - c)) ** 0.5

Tedaj je

.. doctest::

    >>> ploscina
    24.0

Kako pa bi izračunali površino tetraedra, ki ima za lica štiri trikotnike?
Načeloma bi lahko pisali:

.. testcode::

    a, b, c, d, e, f = 896, 1073, 1073, 990, 1073, 1073
    s_abc = (a + b + c) / 2
    ploscina_abc = (s_abc * (s_abc - a) * (s_abc - b) * (s_abc - c)) ** 0.5
    s_aef = (a + e + f) / 2
    ploscina_aef = (s_aef * (s_aef - a) * (s_aef - e) * (s_aef - f)) ** 0.5
    s_bdf = (b + d + f) / 2
    ploscina_bdf = (s_bdf * (s_bdf - b) * (s_bdf - d) * (s_bdf - f)) ** 0.5
    s_cde = (c + d + e) / 2
    ploscina_cde = (s_cde * (s_cde - c) * (s_cde - d) * (s_cde - e)) ** 0.5
    povrsina = ploscina_abc + ploscina_aef + ploscina_bdf + ploscina_cde

Kot vidimo, to ni najbolj pregledno. V taki kodi z veliko verjetnostjo naredimo
kakšno napako. Bolje je, da uporabimo funkcije. Že prej smo uporabili nekaj
vgrajenih funkcij, na primer ``min`` in ``max``. Python pa nam omogoča, da si
funkcije definiramo tudi sami.


Definicija funkcije, ki izračuna ploščino trikotnika, je sledeča:

.. testcode::

    def ploscina_trikotnika(a, b, c):
        '''Vrne ploščino trikotnika z danimi stranicami.'''
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

Oglejmo si njene sestavne dele. Vsaka definicija funkcije se začne s ključno
besedo ``def``, ki ji sledi ime funkcije, v našem primeru
``ploscina_trikotnika``, tej pa v oklepajih našteti argumenti, ki jih funkcija
sprejme. Funkcije lahko sprejmejo različno število argumentov. Naša sprejme tri
argumente, ki jih bomo shranili v spremenljivke ``a``, ``b`` in ``c``. V drugi
vrstici sledi za štiri presledke zamaknjeni *dokumentacijski niz* oziroma
*docstring*. Ta niz ponavadi zapišemo med trojne enojne navednice, v njem pa na
kratko opišemo, kaj funkcija počne. Ta vrstica ni obvezna, je pa koristna, saj
lahko uporabnik, ki ne ve, kaj funkcija počne, to pogleda s pomočjo funkcije
``help``.

.. doctest::

    >>> help(ploscina_trikotnika)
    Help on function ploscina_trikotnika:
    <BLANKLINE>
    ploscina_trikotnika(a, b, c)
        Vrne ploščino trikotnika z danimi stranicami.
    <BLANKLINE>

Nato sledi *telo funkcije*, torej ukazi, ki naj se izvedejo, ko funkcijo
pokličemo. Tako kot veje pogojnega stavka zamaknemo tudi celotno telo funkcije,
da se jasno vidi, kaj vse spada v definicijo funkcije. Tretjo vrstico smo že
videli, v četrti vrstici pa z ukazom ``return`` povemo, katero vrednost naj vrne
funkcija. Tako definirano funkcijo potem kličemo na enak način kot vgrajene
funkcije.

.. doctest::

    >>> ploscina_trikotnika(4, 13, 15)
    24.0

S pomočjo funkcije ``ploscina_trikotnika`` lahko tudi na veliko bolj pregleden
način zapišemo funkcijo za izračun površine tetraedra:

.. testcode::

    def povrsina_tetraedra(a, b, c, d, e, f):
        '''Vrne površino tetraedra z danimi stranicami.'''
        povrsina = 0
        povrsina += ploscina_trikotnika(a, b, c)
        povrsina += ploscina_trikotnika(a, e, f)
        povrsina += ploscina_trikotnika(b, d, f)
        povrsina += ploscina_trikotnika(c, d, e)
        return povrsina

.. doctest::

    >>> povrsina_tetraedra(896, 1073, 1073, 990, 1073, 1073)
    1816080.0

V telesu funkcij lahko pišemo poljubne stavke. Na primer, funkcijo, ki računa
absolutno vrednost, lahko s pomočjo pogojnega stavka napišemo kot:

.. testcode::

    def absolutna_vrednost(x):
        '''Vrne absolutno vrednost števila x.'''
        if x >= 0:
            return x
        else:
            return -x

.. doctest::

    >>> absolutna_vrednost(-5)
    5
    >>> absolutna_vrednost(3)
    3

Če veje ``else`` ne napišemo, se ob neresnični vrednosti ne zgodi nič. Na ta
način bi lahko funkcijo ``absolutna_vrednost`` definirali tudi kot:

.. testcode::

    def absolutna_vrednost(x):
        '''Vrne absolutno vrednost števila x.'''
        if x < 0:
            x *= -1
        return x

Torej, če je število negativno, ga pomnožimo z -1, preden ga vrnemo, sicer pa
ga vrnemo nespremenjenega.
