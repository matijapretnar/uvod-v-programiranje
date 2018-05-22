Uporaba izpeljanih seznamov
---------------------------

Seveda bi obe funkciji lepše napisali s pomočjo izpeljanih seznamov:

.. testcode::

    def pozitivni_elementi(seznam):
        '''Vrne seznam vseh pozitivnih elementov danega seznama.'''
        return [element for element in seznam if element > 0]

    def vsota_pozitivnih_elementov(seznam):
        '''Vrne seznam vseh pozitivnih elementov danega seznama.'''
        return sum([element for element in seznam if element > 0])
        # ali pa kar
        # return sum(pozitivni_elementi(seznam))


Namesto tega lahko uporabimo izpeljani seznam:

.. testcode::

    def identicna_matrika(n):
        '''Vrne identično matriko velikosti n x n.'''
        matrika = [n * [0] for _ in range(n)]
        for k in range(len(matrika)):
            matrika[k][k] = 1
        return matrika

.. doctest::

    >>> identicna_matrika(3)
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

Primer: smučarski skoki
-----------------------

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

Izračunajmo število točk zmagovalnega skoka `Petra Prevca na skakalnici v
Sapporu`__. Peter je skočil 138 metrov ter dobil sodniške ocene:
18,5, 18,5, 19,0, 19,0 in 19,0. Koliko točk je dobil za skok?
Kodo napišimo tako, da bo delovala tudi v primeru, ko za K-točko,
dolžino skoka, ocene sodnikov in izravnavo vnesemo druga števila. Kot vidimo,
potrebujemo pogojni stavek, v katerem ustrezno izračunamo točke za dolžino
skoka.

__ http://medias2.fis-ski.com/pdf/2017/JP/3906/2017JP3906RL.pdf

.. testcode::

    k_tocka = 123
    dolzina = 138.0
    slog_a = 18.5
    slog_b = 18.5
    slog_c = 19
    slog_d = 19
    slog_e = 19
    izravnava = -16.6

    # če je K-točka vsaj 170 metrov, gre za letalnico
    if k_tocka >= 170:
        osnovne_tocke = 120
        vrednost_metra = 1.2
    else:
        osnovne_tocke = 60
        vrednost_metra = 1.8
    tocke_dolzina = osnovne_tocke + vrednost_metra * (dolzina - k_tocka)

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
    126.9

Razširjeni pogojni stavek
-------------------------

V resnici tudi zgornja formula ni čisto natančna, saj obstajajo tudi male skakalnice,
na katerih je vrednost metra enaka 2. Tako bi morali točke za dolžino izračunati kot:


.. doctest::

    if k_tocka >= 170:
        osnovne_tocke = 120
        vrednost_metra = 1.2
    else:
        if k_tocka >= 100:
            osnovne_tocke = 60
            vrednost_metra = 1.8
        else:
            osnovne_tocke = 60
            vrednost_metra = 2

Zgornji pogojni stavek je malo nerodno zapisan. Ker se nam bo dostikrat zgodilo,
da se ne bomo odločali le med dvema primeroma, temveč med večimi, nam Python omogoča
splošnejše pogojne stavke oblike:

.. code::

    if pogoj1:
        stavki_ki_jih_izvedemo
        ko_pogoj1_drzi
    elif pogoj2:
        stavki_ki_jih_izvedemo
        ko_pogoj1_ne_drzi
        ampak_drzi_pogoj2
    elif pogoj3:
        stavki_ki_jih_izvedemo
        ko_tudi_pogoj2_ne_drzi
        ampak_drzi_pogoj3
    else:
        stavki_ki_jih_izvedemo
        ko_noben_od_pogojev_ne_drzi

Beseda ``elif`` je okrajšava za ``else``-``if``. Točke za razdaljo bi tako lepše zapisali kot:

.. doctest::

    if k_tocka >= 170:
        osnovne_tocke = 120
        vrednost_metra = 1.2
    elif k_tocka >= 100:
        osnovne_tocke = 60
        vrednost_metra = 1.8
    else:
        osnovne_tocke = 60
        vrednost_metra = 2

ali pa kot:

.. doctest::

    if k_tocka >= 170:
        osnovne_tocke = 120
    else:
        osnovne_tocke = 60

    if k_tocka >= 170:
        vrednost_metra = 1.2
    elif k_tocka >= 100:
        vrednost_metra = 1.8
    else:
        vrednost_metra = 2

Kot lahko vidite na `Wikipediji`__, je ocenjevanje še bolj zapleteno, vendar
pogojnemu stavku ne bomo dodajali še novih in novih vej, temveč bomo počakali na
to, da spoznamo malo boljšo rešitev.

__ https://en.wikipedia.org/wiki/Construction_point


Izrazi & stavki
---------------

V Pythonovih programih ločimo med *izrazi* in *stavki*. Izrazi so vse, kar
sestavimo iz funkcij in operacij ter uporabljamo kot argumente funkcij, desne
strani prireditvenih izrazov ali pogoje v pogojnih stavkih. Stavki pa so osnovni
gradniki Pythonovih programov in jih pišemo enega pod drugim. Zaenkrat smo
videli tri vrste stavkov: prva so bili prireditveni stavki, drugi pogojni stavki
(ki so potem spet sestavljeni iz gnezdenih stavkov), tretja in najmanj opazna pa
so bili izrazi. Običajne izraze lahko prav tako pišemo v programe, vendar ne bodo
imeli posebnega učinka. Če napišemo

.. testcode::

    x = 10
    10 + 10
    y = 20

se bo vsota ``10 + 10`` res izračunala, vendar se ne bo nikamor shranila in
Python bo na njo hitro pozabil. Kmalu pa bomo srečali tudi izraze, ki bodo imeli
vpliv na nadaljnje izvajanje programov.

Pogojni izraz
-------------

Python poleg pogojnih stavkov podpira tudi pogojne izraze, s katerimi nekatere stvari napišemo malo elegantneje. Na primer, zgornjo določitev osnovnih točk bi lahko pisali kot:

.. testcode::

    osnovne_tocke = 120 if k_tocka >= 170 else 60

Če bi na isti način želeli uporabiti pogojni stavek

.. code::

    osnovne tocke = if k_tocka >= 170:
        120
    else:
        60

bi dobili sintaktično napako, saj smo na mestu izraza uporabili stavek. V pogojnih izrazih moramo vedno napisati obe možnosti, prav tako pa ne moremo uporabiti ``elif``-a, zato spremenljivke ``vrednost_metra`` z njimi ne bi mogli nastaviti. No, načeloma bi jo lahko z

.. testcode::

    vrednost_metra = 1.2 if k_tocka >= 170 else 1.8 if k_tocka >= 100 else 2

samo to je preveč natlačeno, da bi bilo berljivo. Pogojni stavki so torej precej omejeni, ampak vseeno jih omenjamo, ker znajo včasih kakšno stvar narediti preglednejšo.



Pogojni izraz
-------------

ali s pogojnim izrazom kot:

.. testcode::

    def fakulteta(n):
        '''Vrne fakulteto naravnega števila n.'''
        return 1 if n == 0 else n * fakulteta(n - 1)

ali s pogojnim izrazom kot

.. testcode::

    def gcd(m, n):
        '''Vrne največji skupni delitelj števil m in n.'''
        return m if n == 0 else gcd(n, m % n)


Preostali argumenti
-------------------

S pomočjo vzorca za preostale argumente bi tako funkcijo napisali tako, da bi
najprej preverili, koliko argumentov smo dobili, nato pa ustrezno poiskali
maksimum:

.. testcode::

    def maksimum(*argumenti):
        '''
        Ob več argumentih vrne največjega.
        Ob enem argumentu vrne njegov največji element.
        '''
        if len(argumenti) == 0:       # Če nismo dobili nobenega argumenta,
            return None               # vrnemo None.
        if len(argumenti) == 1:       # Če smo dobili en argument,
            kandidati = argumenti[0]  # iščemo maksimum med njegovimi elementi.
        else:                         # Če smo dobili več argumentov,
            kandidati = argumenti     # iščemo maksimum med njimi.

        # Uporabimo znan postopek za iskanje največjega elementa.
        najvecji = None
        for kandidat in kandidati:
            if najvecji is None or najvecji < kandidat:
                najvecji = kandidat
        return najvecji


.. doctest::

    >>> maksimum([3, 5], [4, 1])
    [4, 1]
    >>> maksimum([3, 5, 4, 1])
    5
    >>> maksimum(3, 5, 4, 1)
    5


Osnovni vgrajeni tipi
=====================

Vsaka vrednost v Pythonu ima svoj *tip* oziroma *razred* (ti dve besedi sta
včasih v Pythonu imeli različna pomena, zdaj pa pomenita isto reč), ki opisuje
njene osnovne lastnosti.

Tipi števil ``int`` in ``float``
--------------------------------

Videli smo že, da zna Python računati tako s celimi števil kot s števili s
plavajočo vejico. Prva pripadajo tipu ``int`` (*integer*), druga pa tipu
``float`` (*floating point number*). Razlika med njimi je vidna že na pogled,
saj se druga prikazujejo z decimalno piko. Število, v katerem uporabimo
decimalno piko, je tipa ``float`` tudi takrat, ko so vse decimalke enake nič. Če
računamo s celimi števili, vedno uporabljamo vrednosti tipa ``int``, saj pri
tipu ``float`` prihaja do zaokrožitvenih napak:

.. doctest::

    >>> 7.0 ** 360 / 7.0 ** 342
    1628413597910448.8
    >>> 7 ** 18
    1628413597910449

Pri zgornjem primeru smo res uporabili zelo velika števila, da smo dobili majhno
napako, vendar je to zaradi tega, da smo imeli enostaven primer. Običajni
izračuni so daljši, zato se tudi napake začnejo hitreje nabirati.


Tip kompleksnih števil ``complex``
----------------------------------

Python pozna tudi kompleksna števila tipa ``complex``, ki jih pišemo tako, da
za vrednostjo imaginarnega dela napišemo črko ``j`` (črko ``i`` v programiranju
raje uporabljamo za indekse). Običajno tudi ``+`` med realnim in imaginarnim
delom pišemo brez presledka:

.. doctest::

    >>> 2 + 3j
    (2+3j)
    >>> (1 + 1j) * (1 - 1j)
    (2+0j)
    >>> (-1 + 0j) ** 0.5
    (6.123233995736766e-17+1j)
    >>> import math
    >>> math.e ** (math.pi * 1j) + 1
    1.2246467991473532e-16j

V zadnjih dveh primerih vidimo, da tudi pri kompleksnih številih prihaja do
zaokrožitvenih napak (prva vrednost bi morala biti ``1j``, druga pa ``0+0j``),
saj Python kompleksna števila predstavi s parom števil s plavajočo vejico. Tako
kot pri tipu ``float`` tudi pri kompleksnih številih Python vse ostale vrednosti
v računu, v katerem se pojavi kakšno kompleksno število, pretvori v tip
``complex``. Tako kot deljenje ``/``, ki dve celi števili pretvori v ``float``,
tudi potenciranje na negativno število samodejno ustvari kompleksna števila:

.. doctest::

    >>> (-1) ** 0.5
    (6.123233995736766e-17+1j)    

Kompleksna števila lahko ustvarimo tudi s funkcijo ``complex``, ki ji lahko
podamo tudi dva argumenta, da povemo obe komponenti:


.. doctest::

    >>> complex(3)
    (3+0j)
    >>> complex(3, 4)
    (3+4j)

Tip logičnih vrednosti ``bool``
-------------------------------

Logični vrednosti ``True`` in ``False``, ki sta tipa ``bool`` (*boolean*
oz. Booleovi števili) že poznamo.

Tip ničelne vrednosti ``NoneType``
----------------------------------

Tudi vrednost ``None``, ki smo jo srečali takrat, kadar smo v funkciji pozabili
napisati ``return``, ima svoj tip, ki mu rečemo ``NoneType``. Zdaj lahko tudi
razumemo napako, ki smo jo dobili, ko smo ``None`` želeli uporabiti v računu:


.. testcode::

    def f(x):
        x + 1

.. doctest::

    >>> 3 * f(2)
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

Napaka ``TypeError`` nam pravi, da smo nekje zamešali tipe. V tem primeru smo z
operacijo ``*`` poskušali pomnožiti ``int`` in ``NoneType``, torej neko celo
število in vrednost ``None`` (saj je to edina vrednost tipa ``NoneType``).
Rezultat klica ``f(2)`` je torej ``None``, zato smo verjetno pozabili na
``return``.


Pretvorbe med tipi
------------------

V zgornjih računih vidimo, da Python števila avtomatično pretvori na skupni
imenovalec. Na primer, če število tipa ``int`` pomnožimo s številom tipa
``float``, bo končni rezultat vedno ``float``:

.. doctest::

    >>> 2 * 3.0
    6.0

Pretvorbo lahko opravimo tudi sami s pomočjo funkcij ``int`` in ``float``:

.. doctest::

    >>> float(2)
    2.0
    >>> int(3.1415)
    3

Funkcijo ``int`` bomo pogosto uporabili za to, da danemu število s plavajočo
vejico odbijemo decimalke in ga s tem pretvorimo v celo število. Pozor, ta
funkcija niti ne zaokroži na najbližje celo število, niti ne zaokroži:


.. doctest::

    >>> int(3.999)
    3
    >>> int(-3.1)
    -3
    >>> int(-3.9999)
    -3


 Pretvorbe v logične vrednosti so malo bolj
posebne: vsa neničelna števila in vsi neprazni nizi se pretvorijo v ``True``,
ničla in prazen niz pa v ``False``.

    >>> bool(4)
    True
    >>> bool(0)
    False
    >>> bool(0.00000001)
    True
    >>> bool('False')
    True
    >>> bool('')
    False

Tudi v drugo smer so pretvorbe malo posebne: ``True`` se pretvori v število 1
ali pa niz ``'True'``, ``False`` pa v število 0 oziroma niz ``'False'``.

    >>> int(True)
    1
    >>> float(False)
    0.0
    >>> str(False)
    'False'
    >>> bool(str(False))
    True

Pretvorbe v logične vrednosti se v pogojnih stavkih izvajajo avtomatično.
Evklidov algoritem bi lahko zato, če bi želeli, pisali tudi kot:

.. testcode::

    def gcd(m, n):
        if n:
            return gcd(n, m % n)
        else:
            return m


Tip nizov ``str``
-----------------

Nizi v Pythonu so tipa ``str`` (*string*). Druge vrednosti lahko pretvorimo v
nize s pomočjo funkcije ``str``:

.. doctest::

    >>> str(1234)
    '1234'
    >>> str(1 / 3)
    '0.3333333333333333'
    >>> str(2 < 3)
    'True'

Pretvorbe lahko naredimo tudi v drugo smer, če le napišemo ustrezen niz:

.. doctest::

    >>> int('123')
    123
    >>> float('3.14')
    3.14
    >>> int('12 + 34')
    Traceback (most recent call last):
      ...
    ValueError: invalid literal for int() with base 10: '12 + 34'

Zadnja napaka pravi, da niz ``12 + 34`` ni veljaven zapis celega števila v
desetiškem sistemu.


Tip tipov ``type``
------------------

Če želimo, lahko tip ugotovimo tudi s funkcijo ``type``:

.. doctest::

    >>> type(3)
    <class 'int'>
    >>> type(3.14)
    <class 'float'>
    >>> type(3.0)
    <class 'float'>
    >>> type(10 // 2)
    <class 'int'>
    >>> type(10 / 2)
    <class 'float'>
    >>> type('abc')
    <class 'str'>
    >>> type(None)
    <class 'NoneType'>

Ta funkcija vrača vrednosti, ki predstavljajo tipe. Do teh vrednosti
lahko dostopamo tudi direktno prek vgrajenih konstant ``int``, ``str``, …

.. doctest::

    >>> type(3) == int
    True
    >>> type(3.0) == bool
    False

Te vgrajene konstante so posebne, saj se hkrati obnašajo kot tipi in kot funkcije, ki pretvarjajo v dane tipe:

.. doctest::

    >>> type(int('123')) == int
    True
    >>> type(str(3.14)) == float
    False

Kot smo povedali na začetku, imajo vse vrednosti v Pythonu svoj tip. Tako ga
imajo tudi vrednosti, ki predstavljajo tipe, in sicer tip ``type``. Vrednost
``type``, ki predstavlja ta tip tipov, pa ima spet tip ``type``, s čimer se
zgodba zaključi.

.. doctest::

    >>> type(3)
    <class 'int'>
    >>> type(type(3))
    <class 'type'>
    >>> type(int)
    <class 'type'>
    >>> type(type)
    <class 'type'>


