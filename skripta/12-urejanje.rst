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

    def uredi_z_zlivanjem(seznam, zac=0, kon=None):
        if kon is None:
            kon = len(seznam)
        if kon - zac <= 1:
            return
        else:
            sre = (zac + kon) // 2
            uredi_z_zlivanjem(seznam, zac, sre)
            uredi_z_zlivanjem(seznam, sre, kon)
            zlij_na_mestu(seznam, zac, sre, kon)

    def zlij_na_mestu(seznam, zac, sre, kon):
        zliti_seznam = (kon - zac) * [None]
        levi, desni, cilj = zac, sre, 0
        while levi < sre or desni < kon:
            if levi == sre:
                zliti_seznam[cilj] = seznam[desni]
                desni += 1
            elif desni == kon:
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
        seznam[zac:kon] = zliti_seznam



Hitro urejanje (Quicksort)
--------------------------

.. testcode::

    def premeci(seznam, zac, konec):
        assert konec - zac > 1
        pivot = zac
        zac += 1
        konec -= 1
        while zac < konec:
            while zac < konec and seznam[zac] <= seznam[pivot]:
                zac += 1
            while zac < konec and seznam[konec] > seznam[pivot]:
                konec -= 1
            zamenjaj(seznam, zac, konec)
        if seznam[zac] <= seznam[pivot]:
            novi_pivot = zac
        else:
            novi_pivot = zac - 1
        zamenjaj(seznam, pivot, novi_pivot)
        return novi_pivot


    def hitro_uredi(seznam, zac=0, kon=None):
        if kon is None:
            kon = len(seznam)
        if kon - zac <= 1:
            return
        else:
            pivot = premeci(seznam, zac, kon)
            hitro_uredi(seznam, zac, pivot)
            hitro_uredi(seznam, pivot + 1, kon)
