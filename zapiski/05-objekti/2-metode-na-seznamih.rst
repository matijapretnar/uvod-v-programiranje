Metode na seznamih
==================

Za večino pogosto uporabljanih stvari na seznamih obstajajo že vgrajene metode. Te povečini ne vračajo ničesar, temveč le spremenijo dani seznam. Izjemi sta metodi ``index`` in ``count``, ki vrneta vrednost in seznam pustita pri miru, ter metoda ``pop`` ki tako spremeni seznam kot vrne vrednost.

* ``sez.append(x)``
    Dodaj element `x` na konec seznama ``sez``.

* ``sez.extend(sez2)``
    Na konec seznama ``sez`` dodaj vse elemente iz seznama ``sez2``.

* ``sez.insert(i, x)``
    Pred element na mestu ``i`` v seznamu ``sez`` vstavi element ``x``.

* ``sez.remove(x)``
    Iz seznama ``sez`` odstrani prvo pojavitev vrednosti ``x``.

* ``sez.pop(i=-1)``
    Vrni element na mestu ``i`` v seznamu ``sez`` in odstrani ta element iz seznama.
    Če indeksa ``i`` ne podamo, metoda odstrani zadnji element.

* ``sez.clear()``
    Iz seznama ``sez`` pobriši vse elemente.

* ``sez.index(x)``
    Vrni prvo mesto, na katerem se v seznamu ``sez`` nahaja vrednost ``x``.

* ``sez.count(x)``
    Vrni število pojavitev vrednosti ``x`` v seznamu ``sez``.

* ``sez.sort(key=None, reverse=False)``
    Na mestu uredi seznam glede na vrednosti funkcije ``key``. Če parameter
    ``reverse`` nastavimo na ``True``, bo seznam urejen padajoče.

* ``sez.reverse()``
    Obrni seznam ``sez`` na glavo.

Primer uporabe:

.. doctest::

    >>> sez = [66.25, 333, 333, 1, 1234.5]
    >>> (sez.count(333), sez.count(66.25), sez.count('x'))
    (2, 1, 0)
    >>> sez.insert(2, -1)
    >>> sez.append(333)
    >>> sez
    [66.25, 333, -1, 333, 1, 1234.5, 333]
    >>> sez.index(333)
    1
    >>> sez.remove(333)
    >>> sez
    [66.25, -1, 333, 1, 1234.5, 333]
    >>> sez.reverse()
    >>> sez
    [333, 1234.5, 1, 333, -1, 66.25]
    >>> sez.sort()
    >>> sez
    [-1, 1, 66.25, 333, 333, 1234.5]
    >>> sez.pop()
    1234.5
    >>> sez
    [-1, 1, 66.25, 333, 333]

Metodo ``append`` pogosto uporabljamo za izračun seznama ustreznih elementov. To storimo tako, da ustvarimo prazen seznam, nato pa vanj z metodo ``append`` dodamo vsak ustrezen element. To je podoben postopek kot pri izračunu vsote ustreznih elementov, kjer smo ustvarili spremenljivko z začetno vrednostjo 0, nato pa ji prištevali ustrezne elemente.

.. testcode::

    def vsota_pozitivnih_elementov(seznam):
        '''Vrne vsoto vseh pozitivnih elementov danega seznama.'''
        vsota = 0
        for element in seznam:
            if element > 0:
                vsota += element
        return vsota

    def pozitivni_elementi(seznam):
        '''Vrne seznam vseh pozitivnih elementov danega seznama.'''
        pozitivni = []
        for element in seznam:
            if element > 0:
                pozitivni.append(element)
        return pozitivni


.. doctest::

    >>> vsota_pozitivnih_elementov([1, -5, 2, 3])
    6
    >>> pozitivni_elementi([1, -5, 2, 3])
    [1, 2, 3]
