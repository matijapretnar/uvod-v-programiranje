Delo s Pythonom
===============

S Pythonom se najenostavneje pogovarjamo prek interaktivne konzole, do katere lahko dostopamo na več načinov: neposredno iz ukazne vrstice, z uporabo enostavnega okolja IDLE, ki je priloženo vsaki namestitvi Pythona, ali pa prek kakšnega od naprednejših razvijalskih okolij, na primer PyCharm. Za navodila, kako to storimo, si oglejte video `Namestitev Pythona pod Windowsi`__.

__ https://vimeo.com/156327496

V vseh primerih nas pozdravi približno tak izpis:

.. code::

    Python 3.5.1 (default, Jan 22 2016, 08:54:32) 
    [GCC 4.2.1 Compatible Apple LLVM 7.0.2 (clang-700.1.81)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

Na začetku natančno piše, katero različico Pythona uporabljamo, temu pa sledi nekaj kazalcev na osnovne informacije. Mi se bomo osredotočili na zadnjo vrstico, v kateri nam poziv ``>>>`` kaže, da je Python pripravljen na naš vnos.

.. caution::

    Pozorni bodite, da v prvi vrstici piše ``Python 3.x.x`` (zadnji dve številki nista tako ključni). Če tam piše ``Python 2.x.x``, uporabljate Python 2, starejšo, a še vedno precej razširjeno starejšo različico Pythona. Ob prehodu na Python 3 leta 2008 so razvijalci jezika naredili nekaj večjih sprememb, ki so jezik prečistile, vendar so zaradi njih nekateri programi, napisani v Pythonu 2, prenehali delovati. Razvijalci Pythona so upali, da bodo avtorji starih programov prešli na Python 3, vendar se to ni zgodilo dovolj hitro, tako da sta danes še vedno v uporabi obe različici. V tem učbeniku se bomo ukvarjali izključno s Pythonom 3.

Za začetek izračunajmo, koliko je 1 + 1. Vnesemo ``1 + 1`` ter pritisnimo znak za novo vrstico. Ob tem Python prebere naš vnos, ga izračuna in izpiše rezultat.


.. doctest::

    >>> 1 + 1
    2


Števila in aritmetične operacije
--------------------------------

Poleg seštevanja so nam na voljo tudi ostale osnovne računske operacije: ``-`` za odštevanje, ``*`` za množenje in ``**`` za potenciranje. Za deljenje Python pozna dve operaciji: običajno deljenje ``/`` in pa celoštevilsko deljenje ``//``, ki zavrže morebitni ostanek. Če želimo izračunati samo ostanek, uporabimo ``%``. Prioriteta operatorjev je določena tako kot običajno: najtesneje veže potenciranje, nato množenje in deljenji, nazadnje pa seštevanje in odštevanje. Če želimo vrstni red spremeniti, uporabimo običajne oklepaje. Še to: da je koda bolj berljiva, damo na vsaki strani operatorja po en presledek.

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

Vidimo, da velika števila Pythonu ne povzročajo velikih težav.


Uporaba vgrajenih funkcij
-------------------------

Na voljo so tudi osnovne funkcije, kot na primer ``max`` in ``min`` za izračun maksimuma in minimuma.

.. doctest::

    >>> max(3, 6)
    6
    >>> min(12, -5)
    -5
    >>> max(min(10, 20), 30 // 2)
    15

Matematične funkcije so na voljo v ločeni knjižnici ``math``. Do njih lahko dostopamo na dva osnovna načina:

1. Knjižnico uvozimo s stavkom ``import math``, nato pa do funkcij in konstant dostopamo tako, da dodamo ``math.`` pred vsako ime:

   .. doctest::

       >>> import math
       >>> math.sqrt(2) / 2
       0.7071067811865476
       >>> math.sin(math.pi / 4)
       0.7071067811865475
       >>> math.sin(math.pi)
       1.2246467991473532e-16

  V zadnjem ukazu nismo dobili pričakovanega odgovora 0. Računalnik namreč ne dela s čisto pravimi realnimi števili, temveč z njihovimi približki, ki jim pravimo *števila s plavajočo vejico*. Za ta števila običajno najprej zapišemo decimalke (ki jim pravimo *mantisa*), nato pa še eksponent. Število, ki smo ga dobili, je tako enako približno :math:`1{,}22 \cdot 10^{-16}`, saj ``e-16`` pomeni :math:`10^{-16}`. Na primer ``3.2445e2`` pa označuje število :math:`324{,}45 = 3{,}2445 \cdot 10^2`).

2. Iz knjižnice s stavkom ``from math import ...`` uvozimo posamezne vrednosti, nato pa do njih dostopamo direktno:

       >>> from math import sqrt, sin, pi
       >>> sqrt(2) / 2
       0.7071067811865476
       >>> sin(pi / 4)
       0.7071067811865475

Obstaja tudi tretji način, ko iz knjižnice s stavkom ``from math import *`` uvozimo vse naštete vrednosti, vendar je odsvetovan, ker potem nikoli ne vemo, kaj vse smo uvozili.


Napake
------

Pri programiranju dostikrat naredimo tudi kakšno napako. Načeloma lahko ločimo tri vrste napak:

1. **Sintaktične napake**, v katerih program napišemo drugače, kot določajo pravila. Na primer, če argumente funkcije ločimo s podpičjem namesto z vejico, ali pa če narobe pišemo oklepaje:

   .. doctest:: napake

      >>> max(2; 4)
      Traceback (most recent call last):
        ...
          max(2; 4)
               ^
      SyntaxError: invalid syntax

   .. doctest:: napake

      >>> max(2, 4))
      Traceback (most recent call last):
        ...
          max(2, 4))
                   ^
      SyntaxError: invalid syntax

   Na take napake nas Python opozori, še preden začne z izvajanjem programa, zato jih ne moremo zgrešiti.

2. **Napake ob izvajanju**, v katerih program napišemo sintaktično pravilno, vendar uporabimo neveljavno operacijo:

   .. doctest:: napake

       >>> 1 / 0
       Traceback (most recent call last):
         ...
       ZeroDivisionError: division by zero

   .. doctest:: napake

       >>> mix(3, 5)
       Traceback (most recent call last):
         ...
       NameError: name 'mix' is not defined

   Opozorila o napakah si bomo še ogledali bolj podrobno, zaenkrat pa si zapomnimo le, da je ključna informacija o napaki v zadnji vrstici opozorila. V prvem primeru je bila napaka deljenje z 0, v drugem pa to, da ime ``mix`` ni definirano.

   Take napake se pojavijo šele ob izvajanju programa, in izvajanje tudi prekinejo. To zna biti nerodno, kadar gre za kritično pomemben program (npr. za nadzor jedrskega reaktorja) ali pa kadar s tem izgubimo veliko dela (recimo, da se računalnik po 10-urnem izračunu ustavi, preden izpiše rezultat). Lahko se tudi zgodi, da do napak pride šele ob kakšnih robnih pogojih, zato jih lahko precej časa sploh ne opazimo. Vseeno pa je njihova prednost vsaj ta, da jih opazimo, kadar se zgodijo (kot bomo videli, jih lahko včasih tudi naknadno rešimo).

3. **Vsebinske napake**, pri katerih program navidez deluje brez težav, vendar izračuna napačen odgovor, ker smo mu dali napačna navodila. Recimo, da želimo izračunati razdaljo med točkama (2, 3) in (5, 7):

   .. doctest::

       >>> ((2 - 5) ** 2 + (3 - 7) ** 2) ** 1 / 2
       12.5

   Program smo napisali brez sintaktičnih napak in izvajanje je uspešno vrnilo rezultat, ki pa je žal napačen, ker nismo potencirali na 1/2, temveč potencirali na 1 in delili z 2, saj ima potenciranje prednost pred deljenjem. Take napake so še posebej zlobne, ker jih lahko precej dolgo časa ne opazimo. Znan primer te napake je `Mars Climate Orbiter`__, ki je po devetih mesecih potovanja proti Marsu prehitro vstopil v atmosfero in razpadel. Vzrok je bil v tem, da je del kode delal s SI merskimi enotami, del kode pa z imperialnimi. Škode je bilo za 300 milijonov dolarjev.

    __ https://en.wikipedia.org/wiki/Mars_Climate_Orbiter


Prirejanje vrednosti spremenljivkam
-----------------------------------

Izračunane vrednosti si lahko shranimo tudi v spremenljivke, ki jih potem uporabljamo v kasnejših izračunih. Za to uporabimo *prireditveni stavek* oblike

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

Vrednost spremenljivke lahko tudi povozimo z novo vrednostjo, vendar to na preostale spremenljivke ne vpliva, saj se vedno shrani tista vrednost, ki smo jo podali v prireditvenem stavku.

.. doctest::

    >>> x = 10
    >>> y = x + 3
    >>> y
    13
    >>> x = 25
    >>> y
    13

Ko smo v ``x`` shranili novo vrednost, se vrednost ``y`` ni spremenila, saj je prireditveni stavek ``y = x + 3`` najprej izračunal vrednost desne strani, torej ``13``, in v ``y`` shranil samo število.


Shranjevanje programov v datoteke
---------------------------------

Interaktivna konzola je uporabna za krajše programe, daljše pa raje shranimo v datoteko. S tem preprečimo, da bi izgubili vse svoje delo, pa tudi lažje popravljamo napake, saj nam ni treba vsega ponovno vnašati. Pythonove programe shranjujemo v običajne tekstovne datoteke, kar pomeni, da jih lahko odpremo s katerim koli urejevalnikom besedila, na primer *Notepad*, *Notepad++*, *Emacs* ali *Vi*. Pythonovim datotekam običajno damo končnico ``.py``. Za natančnejša navodila si oglejte video `Nalaganje programov iz datotek`__.

__ https://vimeo.com/156465707

Za primer daljšega programa si oglejmo `Fermijevo oceno`__ števila učiteljev matematike v slovenskih osnovnih šolah. Sledeče stavke vpišite v datoteko ``fermi.py``:

.. testcode::

    stevilo_slovencev = 2000000
    pricakovana_zivljenska_doba = 75
    velikost_generacije = stevilo_slovencev / pricakovana_zivljenska_doba
    stevilo_osnovnosolcev = 9 * velikost_generacije
    stevilo_razredov = stevilo_osnovnosolcev / 25
    stevilo_ur_matematike_na_teden = 4.5 * stevilo_razredov
    stevilo_uciteljev_matematike = stevilo_ur_matematike_na_teden / 20

__ https://sl.wikipedia.org/wiki/Fermijev_problem

Ko datoteko naložimo, lahko vidimo, da bi moralo v Sloveniji biti približno 2000 učiteljev matematike:

.. doctest::

    >>> stevilo_uciteljev_matematike
    2160.0


Pisanje preglednih programov
----------------------------

Vidimo, da lahko imena spremenljivk vsebujejo več kot eno črko, česar smo navajeni v matematiki. V programiranju je zelo pomembno, da so imena čimbolj opisna, saj tako hitreje razumemo, kaj počne program. Računalnik bi razumel tudi sledeč program in izračunal enak odgovor, vendar vidimo, da smiselna imena in presledki kodo naredijo veliko bolj berljivo.

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

Zato se bomo držali sledečih pravil:

- Na vsaki strani dvomestne operacije (``=``, ``+``, ``**``, …) pišemo presledek.
- Za ločili (na primer ``,``) pišemo presledek, pred njimi pa ne.
- Spremenljivkam dajemo opisna imena, ki jih pišemo z malimi črkami. Posamezne besede ločimo z znakom ``_``.
