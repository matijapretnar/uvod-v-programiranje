Metode na nizih
---------------


- ``s.count(t)``
    Vrne število pojavitev podniza ``t`` v nizu ``s``. Klic ``s.count(t, i)``
    deluje podobno, le da začne šteti šele pri indeksu ``i``,
    klic ``s.count(t, i, j)`` pa konča šteti pri indeksu ``j``.

- ``s.find(t)``
    Vrne najmanjši indeks v nizu ``s``, kjer se niz ``t`` pojavi kot podniz.
    Podobno kot prej klic ``s.find(t, i)`` začne iskati pri indeksu ``i``,
    klic ``s.find(t, i, j)`` pa konča pri indeksu ``j``. Če niza ni,
    metoda vrne ``-1``. Metoda ``s.index`` se obnaša enako kot ``s.find``, le
    da v primeru, ko podniza ne najde, sproži napako.
    
- ``s.join(sez)``
    Z ločilom ``s`` skupaj stakne vse nize iz seznama ``sez``.

- ``s.replace(t1, t2)``
    Vrne kopijo niza ``s``, v katerem smo vse pojavitve podniza ``t1`` zamenjali s podnizi ``t2``.
    Klic ``s.replace(t1, t2, n)`` pa zamenja le prvih ``n`` pojavitev.

- ``s.strip()``
    Vrne kopijo niza ``s``, v katerem smo odstranili vse bele znake (presledki, tabulatorji, nove vrste)
    z začetka in konca.
    Klic ``s.strip(t)`` z začetka in konca odstrani vse znake iz niza ``t``.

- ``s.lower()`` / ``s.upper()`` / ``s.title()`` / ``s.capitalize()`` / ``s.swapcase()``
    Vrne kopijo niza ``s``, kjer:
    vse črke zamenjamo z malimi /
    vse črke zamenjamo z velikimi / 
    vsem besedam damo veliko začetnico /
    na začetku niza damo veliko začetnico /
    male črke zamenjamo z velikimi in obratno.

- ``s.split()``
    Vrne seznam besed v nizu ``s`` (ločene glede na bele znake). Klic ``s.split(t)``
    loči glede na podniz ``t``. Klic ``s.split(t, n)`` vrne niz razbit na prvih ``n``
    ločilih.

- ``s.isdigit()`` / ``s.isalpha()`` / ``s.islower()`` / ``s.isupper()`` / ``s.isalnum()`` / ``s.isspace()``
    Vrne ``True``, če je niz ``s`` neprazen in so vsi znaki:
    števke / črke / male črke / velike črke / črke ali številke / beli znaki.
