Rekurzija in zanke
==================

Če za trenutek odmislimo, da od računalnikov pričakujemo tudi to, da kaj
preberejo s tipkovnice, kaj izrišejo na zaslon, ali pa se kaj pogovarjajo z
drugimi računalniki, lahko s tisto malega, kar smo spoznali v prejšnjem
poglavju, napišemo čisto vse, kar je računalnik sposoben izračunati. Tista
stvar, ki nam vse to omogoča je rekurzija.

Rekurzija
---------

Videli smo, da lahko iz funkcij kličemo tudi druge funkcije. Na primer, v
funkciji ``povrsina_tetraedra`` smo poklicali funkcijo ``ploscina_trikotnika``,
v tej pa vgrajeno funkcijo ``math.sqrt``. V resnici pa lahko v funkciji
pokličemo tudi funkcijo samo. Takemu klicu pravimo **rekurzivni klic**.
Poglejmo, kako bi izračunali :math:`n! = n \cdot (n - 1) \dots 3 \cdot 2 \cdot
1`. Kot vidimo velja :math:`n! = n \cdot (n - 1)!`, zato bomo :math:`n!`
izračunali tako, da bomo :math:`n` pomnožili z :math:`(n - 1)!`. Toda od kod
bomo dobili tega? Preprosto, :math:`n - 1` bomo pomnožili z :math:`(n - 2)!`. Od
kod pa tega? Ja iz :math:`(n - 3)!`. In tako naprej vse do :math:`2!`, ki ga
bomo dobili iz :math:`1!`, tega pa iz :math:`0!`, ki je po definiciji enak
:math:`1`.

Torej lahko funkcijo, ki računa fakulteto, napišemo tako, da najprej pogleda
svoj argument ``n``. Če je enak 1, vrne 1, sicer pa izračunamo tako, da ``n``
pomnožimo z rezultatom klica ``fakulteta(n - 1)``.

.. testcode::

    def fakulteta(n):
        '''Vrne fakulteto naravnega števila n.'''
        if n == 0:
            return 1
        else:
            return n * fakulteta(n - 1)

.. doctest::

    >>> fakulteta(1)
    1
    >>> fakulteta(5)
    120
    >>> fakulteta(10)
    3628800

Še en primer rekurzivne definicije so Fibonaccijeva števila. Velja :math:`F_0 = 0`,
:math:`F_1 = 1`, za vse :math:`n \ge 2` pa velja in :math:`F_{n} = F_{n - 1} + F_{n - 2}`.
Funkcijo tedaj napišemo podobno na podoben način kot zgornjo: če
je ``n`` enak 0, vrnemo 0, sicer pogledamo, ali je enak 1. V tem primeru vrnemo
1. Če pa tudi 1 ni enak, mora biti večji ali enak 2, zato se pokličemo
rekurzivno.

.. testcode::

    def fibonacci(n):
        if n == 0:
            return 0
        else:
            if n == 1:
                return 1
            else:
                return fibonacci(n - 1) + fibonacci(n - 2)

.. doctest::

    >>> fibonacci(3)
    2
    >>> fibonacci(4)
    3
    >>> fibonacci(5)
    5
    >>> fibonacci(20)
    6765

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

Beseda ``elif`` je okrajšava za ``else``-``if``. Zgornjo funkcijo bi tako lepše zapisali kot:

.. testcode::

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

Tudi ta funkcija ima še svoje težave, zato se je še ne naučite, vendar se bomo s
tem ukvarjali malo kasneje. Zdaj pa je že čas, da si pogledamo še naš prvi pravi
algoritem. Algoritem je zaporedje korakov, s katerimi dobimo iskani rezultat.
Načeloma lahko pod besedo algoritem razumemo tudi zaporedje korakov, s katerimi
si skuhamo jajca (vzemi posodo, odpri pipo, postavi posodo pod pipo, ko je
posoda dovolj polna, …), ampak ponavadi si jo prihranimo za postopke, s katerimi
izračunamo želene vrednosti.

Za prvi algoritem se spodobi, da si pogledamo najstarejši znani algoritem in
sicer Evklidov algoritem za iskanje navečjega skupnega delitelja dveh števil.

.. testcode::

    def gcd(m, n):
        '''Vrne največji skupni delitelj števil m in n.'''
        if n == 0:
            return m
        else:
            return gcd(n, m % n)
