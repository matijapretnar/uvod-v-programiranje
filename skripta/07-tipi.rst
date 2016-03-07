Osnovni tipi
============

Vsaka vrednost v Pythonu ima svoj *tip* oziroma *razred* (ti dve besedi sta
včasih v Pythonu imeli različna pomena, zdaj pa pomenita isto reč), ki opisuje
njene osnovne lastnosti.

Tipi števil ``int`` in ``float``
--------------------------------

Videli smo že, da zna Python računati tako s celimi števil kot s števili s
plavajočo vejico. Prva pripadajo tipu ``int`` (*integer*), druga pa tipu
``float`` (*floating point number*). Razlika med njimi je vidna že na pogled,
saj se druga prikazujejo z decimalno piko. Če želimo, lahko tip ugotovimo tudi
s funkcijo ``type``:

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

Število, v katerem uporabimo decimalno piko, je tipa ``float`` tudi takrat,
ko so vse decimalke enake nič. Če računamo s celimi števili, vedno uporabljamo
vrednosti tipa ``int``, saj pri tipu ``float`` prihaja do zaokrožitvenih napak:

.. doctest::

    >>> 7.0 ** 360 / 7.0 ** 342
    1628413597910448.8
    >>> 7 ** 18
    1628413597910449

Pri zgornjem primeru smo res uporabili zelo velika števila, da smo dobili majhno
napako, vendar je to zaradi tega, da smo imeli enostaven primer. Običajni
izračuni so daljši, zato se tudi napake začnejo hitreje nabirati.


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
    >>> 2.718281828459045 ** 3.141592653589793j + 1
    1.2246467991473532e-16j

V zadnjih dveh primerih vidimo, da tudi pri kompleksnih številih prihaja do
zaokrožitvenih napak (prva vrednost bi morala biti ``1j``, druga pa ``1+0j``),
saj Python kompleksna števila predstavi s parom števil s plavajočo vejico. Tako
kot pri tipu ``float`` tudi pri kompleksnih številih Python vse ostale vrednosti
v računu, v katerem se pojavi kakšno kompleksno število, pretvori v tip
``complex``. Tako kot deljenje ``/``, ki dve celi števili pretvori v ``float``,
tudi potenciranje na negativnego število samodejno ustvari kompleksna števila:

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

Tip logičnih vrednosti ``bool``
-------------------------------

Logični vrednosti ``True`` in ``False``, ki sta tipa ``bool`` (*boolean*
oz. Booleovi števili) že poznamo. Pretvorbe v logične vrednosti so malo bolj
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


Tip tipov ``type``
------------------

Srečali smo že funkcijo ``type``, ki vrne tip dane vrednosti.


.. doctest::

    >>> type(3)
    <class 'int'>
    >>> type('abc')
    <class 'str'>
    >>> type(None)
    <class 'NoneType'>

V resnici funkcija vrača vrednosti, ki predstavljajo tipe. Do teh vrednosti
lahko dostopamo tudi direktno prek vgrajenih konstant ``int``, ``str``, …

.. doctest::

    >>> type(3) == int
    True
    >>> type(3.0) == bool
    False

Te vgrajene konstante so posebne, saj se hkrati obnašajo kot tipi in kot vrednosti

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
