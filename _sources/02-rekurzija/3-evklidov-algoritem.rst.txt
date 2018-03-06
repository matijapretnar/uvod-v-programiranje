Evklidov algoritem
==================

Algoritem je zaporedje korakov, s katerimi dobimo iskani rezultat. Načeloma lahko pod besedo algoritem razumemo tudi zaporedje korakov, s katerimi si skuhamo jajca (vzemi posodo; odpri pipo; postavi posodo pod pipo; ko je posoda dovolj polna, zapri pipo; …), ampak mi si jo bomo prihranili za postopke, s katerimi izračunamo želene vrednosti.

Za prvi algoritem se spodobi, da si pogledamo najstarejši znani algoritem in sicer Evklidov algoritem za iskanje navečjega skupnega delitelja dveh števil. Naj bo :math:`d` največji skupni delitelj števil :math:`m` in :math:`n`. Pišimo :math:`m = k \cdot n + o`, kjer je :math:`0 \le o < n`. Torej: :math:`o` je ostanek pri deljenju števila :math:`m` z :math:`n`. Ker e :math:`d` deli :math:`n`, deli tudi :math:`k \cdot n`. Poleg tega :math:`d` deli tudi :math:`m`, zato deli tudi :math:`o = m - k \cdot n`. Velja tudi obratno, če :math:`d` deli :math:`n` in :math:`o`, potem deli tudi :math:`m = k \cdot n + o`.

Zato lahko iskanje največjega skupnega delitelja števil :math:`m` in :math:`n` prevedemo na iskanje največjega skupnega delitelja števil :math:`n` in :math:`o`. Videti je, kot da se vrtimo v krogu, vendar se ne. Poglejmo, kaj se zgodi:

1. Največji skupni delitelj števil :math:`456` in :math:`123` je enak
   največjemu skupnemu delitelju števil :math:`123` in :math:`456 - 3 \cdot 123 = 87`.
2. Največji skupni delitelj števil :math:`123` in :math:`87` je enak
   največjemu skupnemu delitelju števil :math:`87` in :math:`123 - 1 \cdot 87 = 36`.
3. Največji skupni delitelj števil :math:`87` in :math:`36` je enak
   največjemu skupnemu delitelju števil :math:`36` in :math:`123 - 2 \cdot 36 = 15`.
4. Največji skupni delitelj števil :math:`36` in :math:`15` je enak
   največjemu skupnemu delitelju števil :math:`15` in :math:`36 - 2 \cdot 15 = 6`.
5. Največji skupni delitelj števil :math:`15` in :math:`6` je enak
   največjemu skupnemu delitelju števil :math:`6` in :math:`15 - 2 \cdot 6 = 3`.
6. Največji skupni delitelj števil :math:`6` in :math:`3` je enak
   največjemu skupnemu delitelju števil :math:`3` in :math:`6 - 2 \cdot 3 = 0`.

Postopka ne moremo več nadaljevati, ker ne moremo deliti z nič. Kaj pa je največji skupni delitelj števil 3 in 0? Ja, 3 vendar. Torej, ko je drugo število enako 0, je prvo število ravno njun največji skupni delitelj, po vseh prejšnjih sklepih pa tudi največji skupni delitelj vseh prejšnjih parov vključno s prvim.

Evklidov algoritem je torej sledeč: če je :math:`n = 0`, potem je največji skupni delitelj števil :math:`m` in :math:`n` enak kar :math:`m`, sicer pa je enak največjemu skupnemu delitelju števil :math:`n` in :math:`o`, kjer je :math:`o` ostanek pri deljenju :math:`m` z :math:`n`. Ta postopek enostavno prevedemo v Python:

.. testcode::

    def gcd(m, n):
        if n == 0:
            return m
        else:
            return gcd(n, m % n)

Pri tem je ``gcd`` (*greatest common divisor*) običajna oznaka za največjega skupnega delitelja.

.. doctest::

    >>> gcd(456, 123)
    3

Algoritem deluje tudi, kadar je :math:`n < m`, saj je v tem primeru :math:`n = 0 \cdot m + n`, zato v naslednjem koraku njuni mesti zamenjamo in nadaljujemo kot prej.


