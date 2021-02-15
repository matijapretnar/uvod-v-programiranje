# Od silicija do strojne kode

## Polprevodniški elementi

## Logična vezja

## Registrska arhitektura

Vsak računalnik je sestavljen iz _procesorja_, ki izvaja ukaze, in _pomnilnika_, v katerega procesor zapisuje podatke. Ker pa je pomnilnik počasen (s stališča procesorja, seveda), lahko procesor podatke shrani tudi v manjše število _registrov_. Pri našem simulatorju jih je šest:

- delovni registri `A`, `B`, `C` in `D` se uporabljajo za shranjevanje rezultatov operacij kot so seštevanje, primerjava ali branje iz pomnilnika.
- register `IP` (_instruction pointer_) kaže na del pomnilnika, v katerem je zapisan ukaz, ki ga je treba izvesti. Po opravljenem ukazu se vrednost registra `IP` poveča. Vrednost `IP` lahko tudi spremenimo, s čimer dosežemo, da procesor skoči na izvajanje drugega dela programa.
- register `SP` (_stack pointer_) pa kaže na _sklad_, to je del pomnilnika, na katerega zaporedoma nalagamo vrednosti. Vsakič, ko naložimo vrednost, se vrednost registra `SP` poveča.

Poleg registrov ima simulator še zastavice `Z` (_zero_), `C` (_carry_) in `F`, v katerih je spravljen samo en bit. Malo bolj podrobno jih bomo pogledali pri ukazih.

Vsebino registrov in pomnilnika lahko vidimo v razdelku **CPU & Memory**, ki zaseda glavni del desne strani. Naš procesor je 8-bitni, zato ima 256 spominskih celic. Zadnjih 24 celic, ki so obarvane sivo, je namenjenih izpisu: kar zapišete v njih, se bo prikazalo v razdelku **Output** zgoraj desno.

V razdelek **Code** na levi strani simulatorja boste pisali program, ki se bo nato prevedel v strojno kodo, ki se bo zapisala v pomnilnik. Da se boste lažje sklicevali na dele kode, jim boste pripisali oznake, ki so predstavljene v razdelku **Labels** spodaj desno.

Pod razdelkom **RAM** se _View_ splača nastaviti na _Decimal_, da bodo vrednosti v pomnilniku predstavljene z običajnim desetiškim zapisom.
