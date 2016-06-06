Urejanje
========

Urejanje z izbiranjem
---------------------

.. testcode::

    def zamenjaj(seznam, i, j):
        seznam[i], seznam[j] = seznam[j], seznam[i]


    def uredi_z_izbiranjem(seznam):
        for prvi_ne_na_mestu in range(len(seznam)):
            najmanjsi = prvi_ne_na_mestu
            for k in range(prvi_ne_na_mestu + 1, len(seznam)):
                if seznam[k] < seznam[najmanjsi]:
                    najmanjsi = k
            zamenjaj(seznam, prvi_ne_na_mestu, najmanjsi)


Urejanje z vstavljanjem
-----------------------

.. testcode::

    def uredi_z_vstavljanjem(seznam):
        for prvi_neurejen in range(1, len(seznam)):
            for k in range(prvi_neurejen, 0, -1):
                if seznam[k - 1] > seznam[k]:
                    zamenjaj(seznam, k - 1, k)
                else:
                    break


Urejanje z mehurčki
-------------------

.. testcode::

    def uredi_z_mehurcki(seznam):
        for indeks_zadnjega_neurejenega in range(len(seznam) - 1, 0, -1):
            zamenjava = False
            for k in range(indeks_zadnjega_neurejenega):
                if seznam[k] > seznam[k + 1]:
                    zamenjaj(seznam, k, k + 1)
                    zamenjava = True
            if not zamenjava:
                break


Urejanje z zlivanjem
--------------------

.. testcode::

    def uredi_z_zlivanjem(seznam, zacetek=0, konec=None):
        if konec is None:
            konec = len(seznam)
        if konec - zacetek <= 1:
            return
        else:
            sre = (zacetek + konec) // 2
            uredi_z_zlivanjem(seznam, zacetek, sre)
            uredi_z_zlivanjem(seznam, sre, konec)
            zlij_na_mestu(seznam, zacetek, sre, konec)

    def zlij_na_mestu(seznam, zacetek, sre, konec):
        zliti_seznam = (konec - zacetek) * [None]
        levi, desni, cilj = zacetek, sre, 0
        while levi < sre or desni < konec:
            if levi == sre:
                zliti_seznam[cilj] = seznam[desni]
                desni += 1
            elif desni == konec:
                zliti_seznam[cilj] = seznam[levi]
                levi += 1
            elif seznam[levi] <= seznam[desni]:
                zliti_seznam[cilj] = seznam[levi]
                levi += 1
            else:
                assert seznam[levi] > seznam[desni]
                zliti_seznam[cilj] = seznam[desni]
                desni += 1
            cilj += 1
        seznam[zacetek:konec] = zliti_seznam



Hitro urejanje (Quicksort)
--------------------------

.. testcode::

    def premeci(seznam, zacetek, konec):
        assert konec - zacetek > 1
        pivot = zacetek
        zacetek += 1
        konec -= 1
        while zacetek < konec:
            while zacetek < konec and seznam[zacetek] <= seznam[pivot]:
                zacetek += 1
            while zacetek < konec and seznam[konec] > seznam[pivot]:
                konec -= 1
            zamenjaj(seznam, zacetek, konec)
        if seznam[zacetek] <= seznam[pivot]:
            novi_pivot = zacetek
        else:
            novi_pivot = zacetek - 1
        zamenjaj(seznam, pivot, novi_pivot)
        return novi_pivot


    def hitro_uredi(seznam, zacetek=0, konec=None):
        if konec is None:
            konec = len(seznam)
        if konec - zacetek <= 1:
            return
        else:
            pivot = premeci(seznam, zacetek, konec)
            hitro_uredi(seznam, zacetek, pivot)
            hitro_uredi(seznam, pivot + 1, konec)
