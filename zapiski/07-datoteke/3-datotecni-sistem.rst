Datotečni sistem
================

Tako, kot si daljše programe shranjujemo v datoteke, si tudi večje količine podatkov shranimo v datoteke. Poglejmo si najprej, kako so datoteke na računalniku sploh organizirane. Vsak nosilec podatkov (trdi disk, SSD, DVD, USB ključek) ima podatke zapisane v določenem datotečnem sistemu, ki je odvisen od vrste nosilca in operacijskega sistema. Na primer, trdi diski pod Windowsi so običajno formatirani v sistemu NTFS, pod Linuxom v sistemu Ext, na Macintoshu pa v sistemu HFS. USB ključki so zaradi lažje prenosljivosti ponavadi vsi formatirani v sistemu FAT (ki se je včasih uporabljal pod Windowsi). Če želimo, lahko na nosilcu naredimo več particij in vsako od njih ločeno formatiramo s svojim datotečnim sistemom.

Datotečni sistem določa, v kakšni obliki je na nosilcu shranjena vsebina datotek in v kakšni obliki je predstavljena uporabniku. S prvim se ne bomo ukvarjali, pri drugem pa je pomembna le razlika med operacijskim sistemom Windows in sistemi, osnovanimi na UNIXu (torej Linux ali OS X).

Datotečni sistem vsebuje datoteke, razporejene po mapah (oz. direktorijih), ki so lahko tudi gnezdene. Na vrhu imamo korensko mapo, ki jo v operacijskih sistemih, osnovanih na UNIXu, označujemo z ``/``, na operacijskem sistemu Windows pa z ``C:\``, kjer je ``C`` ime particije: ``C`` običajno označuje glavni pogon, ``D`` drugi pogon ali CD/DVD/BlueRay enoto, ``A`` in ``B`` sta se uporabljali za diskete, kasnejše črke pa se uporabljajo za USB ključke in podobno.

Za primer vzemimo datotečni sistem s sledečimi mapami in datotekami::

    /
        uvp
            datoteke
                vhodna.txt
                izhodna.txt
            funkcije.py
            seznami.py
            slovarji.py
            zanke.py
        praktikum
            latex
                pismo.tex
                pismo.pdf
                pismo.aux
            mathematica
                grafi.nb
                kolokvij.nb
        analiza
            plonkec.tex


Relativne in absolutne poti
---------------------------

Delo z datotečnim sistemom v Pythonu
------------------------------------


- ``os.listdir(pot)``
    Vrne imena vseh datotek v mapi s potjo ``pot``.

- ``os.path.jon(pot1, pot2)``
    Stakne poti ``pot1`` in ``pot2``, pri čemer ustrezno poskrbi za prava ločila
    glede na operacijski sistem.
    
- ``os.path.isdir(pot)``
    Vrne ``True``, kadar ``pot`` vodi do mape.

- ``os.path.exists(pot)``
    Vrne ``True``, kadar ``pot`` obstaja v datotečnem sistemu.

- ``os.path.splitext(pot)``
    Večina datotek ima končnico, ki se začne z znakom ``.`` in označuje tip
    datoteke (``.jpg`` za JPEG slike, ``.docx`` za Wordove dokumente, …).
    Metoda dano ``pot`` loči na del pred končnico in na končnico.

- ``os.path.split(pot)``
    Dano pot loči na pot do zadnje mape in na ime datoteke.
    Do prve komponente lahko dostopamo tudi z metodo ``os.path.dirname(pot)``,
    do druge pa z metodo ``os.path.basename(pot)``.

- ``os.mkdir(pot)``
    Naredi mapo z dano potjo.

- ``os.makedirs(pot, exist_ok=False)``
    Naredi mapo z dano potjo in vse vmesne imenike. Če je argument ``exist_ok`` nastavljen na ``True``,
    ne javi napake, če ciljna mapa že obstaja.

- ``os.rename(stara_pot, nova_pot)``
    Datoteko ali mapo s potjo ``stara_pot`` preimenuje v ``nova_pot``.

- ``os.remove(pot)``
    Pobriše datoteko z dano potjo.

- ``os.rmdir(pot)``
    Pobriše mapo z dano potjo.

- ``os.removedirs(pot)``
    Pobriše mapo z dano potjo in vse vmesne imenike.

- ``os.path.normpath(pot)``
    Vrne počiščeno različico dane poti.

- ``os.path.abspath(pot)``
    Vrne počiščeno absolutno pot dane poti.

- ``os.chdir(pot)``
    Delovni imenik nastavi na ``pot``.

- ``os.getcwd()``
    Vrne trenutni delovni imenik.
