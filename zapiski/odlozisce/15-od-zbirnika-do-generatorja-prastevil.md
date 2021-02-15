# Od zbirnika do generatorja praštevil

## Zbirnik

Tudi, če se vam ni zdelo, smo v Pythonu programe pisali na človeku izjemno prijazen način. Tokrat bomo spoznali še drugo stran programiranja, saj bomo pisali programe, ki neposredno dostopajo do računalnika.

Računalnik sicer izvaja strojno kodo, ki je sestavljena le iz ničel in enic, mi pa bomo uporabljali _zbirnik_ (_assembler_), ki nam omogoča, da programe pišemo v zelo okrnjenem jeziku, ki se nato prevede v strojno kodo. V zbirniku običajno pišemo programe, za katere želimo, da so izjemno hitri, npr. gonilnike za grafične kartice.

Pri tem bomo uporabljali [simulator 8-bitnega računalnika](http://schweigi.github.io/assembler-simulator/), ki precej dobro zajame osnovne ideje običajnih računalnikov.

Vsak ukaz zbirnika je oblike

```
neobvezna_oznaka:
        IME_UKAZA argumenti         ; neobvezen komentar
```

Če pred ukazom napišete neobvezno oznako, se boste prek nje kasneje lahko sklicevali na del pomnilnika, v katerem se nahaja ukaz. Za imenom ukaza naštejete argumente. Odvisno od ukaza je teh lahko 0, 1 ali 2\. Za ukazom se vam splača napisati komentar, v katerem lahko po človeško napišete, kaj ukaz počne.

Vseh ukazov, ki jih nudi simulator, ne bomo uporabljali, temveč se bomo zadovoljili s sledečimi ukazi, v katerih bomo z `reg` označili imena delovnih registrov (`A`, `B`, `C`, `D`), s `konst` pa konstante (`0`, `1`, `7`, `42`, ...).

- `ADD reg1, reg2` vrednosti registra `reg1` prišteje vrednost registra `reg2`
- `ADD reg1, konst` vrednosti registra `reg1` prišteje konstanto `konst`

Dostikrat lahko ukaz za argument sprejme bodisi register bodisi konstanto. Take argumente bomo od sedaj naprej pisali kar kot `reg/konst`. Torej:

- `ADD reg1, reg2/konst` vrednosti registra `reg1` prišteje `reg2/konst`.
- `SUB reg1, reg2/konst` od vrednosti registra `reg1` odšteje `reg2/konst`.
- `MOV reg1, reg2/konst` v register `reg1` zapiše `reg2/konst`.
- `MUL reg/konst` vrednost registra `A` pomnoži z `reg/konst`.
- `INC reg` poveča vrednost registra `reg` za 1.
- `DEC reg` zmanjša vrednost registra `reg` za 1.
- `DIV reg/konst` vrednost registra `A` celoštevilsko deli z `reg/konst`.
- `CMP reg1 reg2/konst` primerja vrednosti registra `reg1` z `reg2/konst2`.
- `JMP label` skoči na izvajanje ukaza, označenega z `label` (torej register `IP` nastavi na del pomnilnika, na katerega kaže `label`).
- `JA label` skoči na ukaz, označen z `label`, če je bil v zadnji primerjavi levi člen večji. Sicer nadaljuje izvajanje z naslednjim ukazom.
- `JB label` skoči na ukaz, označen z `label`, če je bil v zadnji primerjavi levi člen manjši. Sicer nadaljuje izvajanje z naslednjim ukazom.
- `JE label` skoči na ukaz, označen z `label`, če skoči, če sta bila v zadnji primerjavi člena enaka.
- `PUSH reg/konst` postavi vrednost `reg/konst` na sklad (in ustrezno poveča `SP`).
- `POP reg` vrednost vrhnjega elementa sklada shrani v `reg` (in ustrezno zmanjša `SP`).
- `HLT` konča z izvajanjem programa.

Če želite izvedeti več, si poglejte stran [Instruction Set](http://schweigi.github.io/assembler-simulator/instruction-set.html).

## Delo s skladom

## Klici funkcij
